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
uvicorn main:app --reload -> run the terminal
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
