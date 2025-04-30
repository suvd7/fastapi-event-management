from fastapi import APIRouter, HTTPException
from typing import List
from .file_storage import EventFileManager
from .models import Event
from .event_analyzer import EventAnalyzer

router = APIRouter()

@router.get("/events", response_model=List[Event])
async def get_all_events():
    events = EventFileManager.read_events_from_file()
    return events

@router.get("/events/filter", response_model=List[Event])
async def get_events_by_filter(date: str = None, organizer: str = None, status: str = None, event_type: str = None):
    events = EventFileManager.read_events_from_file()
    if date:
        events = [e for e in events if e.date == date]
    if organizer:
        events = [e for e in events if e.organizer.name == organizer]
    if status:
        events = [e for e in events if e.status == status]
    if event_type:
        events = [e for e in events if e.type == event_type]
    return events

@router.get("/events/{event_id}", response_model=Event)
async def get_event_by_id(event_id: int):
    events = EventFileManager.read_events_from_file()
    event = next((e for e in events if e.id == event_id), None)
    
    if not event:
        raise HTTPException(status_code=404, detail="event not found")
    
    return event

@router.post("/events", response_model=Event)
async def create_event(event: Event):
    events = EventFileManager.read_events_from_file()

    if any(e.id == event.id for e in events):
        raise HTTPException(status_code=400, detail="event ID already exists")
    events.append(event)
    EventFileManager.write_events_to_file(events)
    return event

@router.put("/events/{event_id}", response_model=Event)
async def update_event(event_id: int, event: Event):
    events = EventFileManager.read_events_from_file()
    event_to_update = next((e for e in events if e.id == event_id), None)
    
    if event_to_update is None:
        raise HTTPException(status_code=404, detail="event not found")
    event_to_update.date = event.date
    event_to_update.organizer = event.organizer
    event_to_update.status = event.status
    event_to_update.max_attendees = event.max_attendees
    event_to_update.joiners = event.joiners
    
    EventFileManager.write_events_to_file(events)
    return event_to_update

@router.delete("/events/{event_id}")
async def delete_event(event_id: int):
    events = EventFileManager.read_events_from_file()
    event_to_delete = next((e for e in events if e.id == event_id), None)
    
    if event_to_delete is None:
        raise HTTPException(status_code=404, detail="event not found")
    events = [e for e in events if e.id != event_id]
    EventFileManager.write_events_to_file(events)
    
    return {"message": "event deleted"}

@router.get("/events/joiners/multiple-meetings")
async def get_joiners_multiple_meetings():
    events = EventFileManager.read_events_from_file()
    event_analyzer = EventAnalyzer()
    joiners = event_analyzer.get_joiners_multiple_meetings(events)
    
    if not joiners:
        raise HTTPException(status_code=404, detail="no joiners attending at least 2 meetings")
    return joiners
