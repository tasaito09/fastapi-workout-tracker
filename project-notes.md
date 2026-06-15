# Project Notes

## How to setup a project
cd ~/projects -> Go into my "projects" file
mkdir <new-project> -> Create folder for new project
python3 -m venv venv -> Create virutal environment
source venv/bin/activate -> Activate virtual environment
which python -> Verify venv is working

## File operations
rm -rf venv -> Delete venv
touch main.py -> Create new file named "main.py"
code . -> Open folder in VS Code

## 5-20-26
- folder setup
- installed fastapi
- file setup

For every project I create from here on out, I should always have these files:
- project-notes.md
- mistake-logs.md
- README.md

- installed fastapi uvicorn

## 5-21-26
@app.get("/") -> when someone sends a GET request to '/', run this function
uvicorn app.main:app --reload -> run the terminal
http://127.0.0.1:8000/docs -> fastapi lets you test the api directly from browser

class Workout(BaseModel): -> defines shape of workout data
@app.post("/workouts") -> this api endpoint accepts incoming workout data
/workouts/{workout_id} -> dynamic url value

CRUD
- create -> POST endpoint
- read -> GET endpoint
- delete -> DELETE endpoint

## 5-22-26
### Separation of Concerns
Doing 1. Request handling, 2. Business logic, and 3. Data storage all together becomes a disaster in bigger apps
Create helper functions like:
    def load_workout():
    def save_workouts():
which will get called by the endpoints
#### Ideal Architecture
API endpoint
↓
Modify data
↓
Save to file

### Linux controls
mkdir app -> create new folder "app/"
mv main.py app/ -> move file "main.py" into folder "app/"

### Fundamentals
Models -> what my data looks like; the blueprint
ex: 
    class Workout(BaseModel)
        exercise: str
        sets: int
        reps: int
        weight: int
        date: str

Routes -> what users can do with the app; the API endpoints
ex:
    @app.get("/workouts")

Separating files gives one job to EACH file

### Backend App Composition
Request
    ↓
Route
    ↓
Logic
    ↓
Model/Data
    ↓
Response

## 5-26-26
### Frontend and backend separation
Webpage should be its own file -> think about maintainability
Backend API routes are useful by themselves -> the frontend should consume, not replace them
Which means the frontend should be making requests TO those endpoints
Remember: "frontend talks to the backend"

### Mental Model

Browser
    ↓
Loads index.html
    ↓
JavaScript inside page talks to FastAPI
    ↓
FastAPI returns JSON
    ↓
JavaScript updates webpage
---
Fn + F12 -> open DevTools in browser

## 5-27-26
### Separating webpage and API data routes
I need to have separate routes: one route for webpage AND another route for API data.
Webpage route: "give browser the actual webpage" -> Returns: html
API route: "Give frontend workout data" -> Returns: JSON

Note: The browser loads 'index.html' ONLY ONCE initially. (It's the home page)

### fetch() doesn't change pages automatically
Thing                   Purpose
---
Browser navigation  |   changes pages
fetch()             |   background HTTP request
FileResponse        |   sends file
JSON API            |   sends data
DOM manipulation    |   updates page dynamically

### fetch("/workouts/")
means "Browser: send an HTTP GET request to this URL path on the current server"

## 6-8-26
### How does fetch("/workouts/") know to trigger te GET endpoint in workouts.py?
Because: 

In main.py, app.include_router(router) registers all routes from:

router = APIRouter(prefix="/workouts"), in workouts.py, which creates:

'/workouts/', and FastAPI matches incoming URLs against its routing table

fetch("/workouts/") sends a GET request to the FastAPI endpoint at '/workouts/'

@router.get("/") inside router = APIRouter(prefix="/workouts") creates the route 'GET /workouts/'

'/' serves the webpage. '/workouts/' serves the JSON data for the webpage to use

## 6-15-26
### Promise chaining
    
    fetch("/workouts/")                     // sends HTTP request to server
        .then(response => response.json())  // when response arrives, parse it as JSON. .json() also returns a Promise
        .then(data => console.log(data))    // when parsing is done, log the actual data

What's really going on here is something like this:
1. Send the request (and don't wait)
2. When the response arrives -> parse it as JSON (and don't wait)
3. When parsing is done -> use the data
