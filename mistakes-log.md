# Mistakes

## apt install python issue
Problem:
tried installing python3-venv package as user instead of apt

Fix:
sudo apt update
sudo apt install python3-venv

## issue importing fastapi into main.py
Problem:
i had setup venv folder as "venv" instead of ".venv"

Fix: 
rm -rf venv
python3 -m venv .venv
source .venv/bin/activate
python -m install --upgrade pip
pip install fastapi uvicorn

## issue importing fastapi into main.py (part 2)
Problem:
Import "fastapi" could not be resolved

Fix: 
ctrl + shift + p, Python:Select Interpreter
Enter interpreter path
//wsl.localhost/Ubuntu/home/sata/projects/workout-tracker/.venv/bin/python
ctrl + shift + p, Reload Window
make sure fastapi is installed too


## Stuck on PUT method for updating workout
Problem: 
I wasn't telling fastapi to receive updated workout JSON from the request body.
I was also trying to use insert() to update the workout JSON, but i can just update each key-value pair directly.

Original:
@app.put("/workouts/{workout_id}") 
def update_workout(workout_id: int): 
    updated_workout = { 
        "exercise": workout.exercise, 
        "sets": workout.sets, 
        "reps": workout.reps, 
        "weight": workout.weight, 
        "date": workout.date 
    } 
    for workout in workouts: 
        if workout["id"] == workout_id: 
            workouts.remove(workout) 
            workouts.insert(updated_workout) 
            return {"message": "Workout Updated"} 
    return {"message": "Workout Not Found"}

Fixed:
@app.put("/workouts/{workout_id}") 
def update_workout(workout_id: int, workout: Workout):
    for existing_workout in workouts:
        existing_workout["exercise"] = workout.exercise
        existing_workout["sets"] = workout.sets
        existing_workout["reps"] = workout.reps
        existing_workout["weight"] = workout.weight
        existing_workout["date"] = workout.date

        return {
            "message": "Workout Updated",
            "workout": existing_workout
        }
return {"Workout Not Found"}

## trying to load JSON file every time I access the 'workouts' list
Problem: 
I was running load_workouts() inside every API request, whenever I needed to access the workouts list. 

Fix:
I ran it once at the top of main.py, and loaded (cached) it as a global component. 

## error importing router in main.py
Problem:
from routes.workouts import router >> ModuleNotFoundError: No module named 'routes'

Fix:
from app.routes.workouts import router

## Unable to import function dependency
Problem:
I tried importing 'workouts' from workouts.py into storage.py but couldn't.
So I thought moving save_workouts to workouts.py would be the fix.
Issue -> save_workouts and load_workouts should be in the same file for a cleaner structure. 

Fix:
Keep save_workouts() in storage.py. 
Modify save_workouts() to take 'workouts' as a parameter.