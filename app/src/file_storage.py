import json
import os
from typing import List
from .models import Event

class EventFileManager:
    FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'event.json')

    @classmethod
    def read_events_from_file(cls) -> List[Event]:
        try:
            with open(cls.FILE_PATH, 'r') as f:
                events_data = json.load(f)
                events = [Event(**event) for event in events_data]
                return events
        except FileNotFoundError:
            print(f"Error: {cls.FILE_PATH} not found.")
            return [] 
        except json.JSONDecodeError:
            print("error: decode JSON")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return [] 

    @classmethod
    def write_events_to_file(cls, events: List[Event]) -> None:
        try:
            events_data = [event.dict() for event in events]
            with open(cls.FILE_PATH, "w") as f:
                json.dump(events_data, f, indent=4)
        except Exception as e:
            print(f"error: failed {cls.FILE_PATH}: {e}")
