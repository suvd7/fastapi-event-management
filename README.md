# FastAPI Event Management Project
This is a FastAPI-based backend server for event management. The project provides endpoints to manage events, including CRUD operations (Create, Read, Update, Delete), filtering, and retrieving events. It uses a simple JSON file (events.json) as a storage mechanism instead of a database, making it easy to deploy and use for small-scale applications or prototypes.

# Features 
Create, Read, Update, Delete Events: Full event management functionality through API endpoints.
Event Filtering: Filter events based on attributes such as date, organizer, status, and event type.
Joiner Analysis: Retrieve events attended by joiners attending at least 2 meetings.

# Installation
To run this project locally, you need to have Python and pip installed on your machine.

1. Clone this repository:
```bash
  git clone https://github.com/frdayvz85/assignment1.git
  or
  git@github.com:frdayvz85/assignment1.git
```   
2. Navigate into the project directory:
```bash
  cd assignment1
```   
3. Create a virtual enviroment:
```bash
  python -m venv venv
  or
  py -m venv venv
  or
  py3 -m venv venv
```
4. Active a virtualenv
```bash
  Windows users from CMD run this command:
  .\venv\Scripts\activate.bat

  Windows users from PowerShell run this command:
  .\venv\Scripts\Activate.ps1

  Linux or Mac users run this command:
  source venv/bin/activate
```  
5. Install the requirements in the current environment:
```bash
  pip install -r requirements.txt
```  
6. Last step run the following command:
```bash
  py app/main.py
```  

# Testing APIs 🚀:
FastAPI generates interactive API documentation for easy testing of endpoints. You can test and explore your API directly from a browser.

Accessing interface use following link:
```bash
  http://127.0.0.1:8000/docs
```  
# Testing the Endpoints
Root Endpoint:
The "Root" section provides basic information about the API.
You can test the "GET" request to check if the server is up and running.

Event Endpoints:
The "Event" section provides endpoints for:
Get All Events: Retrieve all events stored in the events.json file.
Filter Events: Filter events by attributes like date, organizer, status, or event type.
Get Event by ID: Retrieve an event using its unique ID.
Create Event: Add a new event to the system.
Update Event: Modify an existing event by its ID.
Delete Event: Remove an event by its ID.

# Project Structure
app/
main.py: The main entry point for running the FastAPI application.
src/
app.py: Contains FastAPI application setup and route definitions.
event_analyzer.py: Contains logic for analyzing event data, e.g., finding joiners attending multiple events.
file_storage.py: Handles reading and writing events to/from the events.json file.
models.py: Defines the Event model used for data validation.
routes.py: Contains route definitions for handling different API requests.
events.json: The file where events data is stored.
requirements.txt: The file that lists all Python dependencies.



