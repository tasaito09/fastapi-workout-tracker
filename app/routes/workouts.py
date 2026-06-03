from fastapi import APIRouter
from app.models import Workout
from app.services.storage import load_workouts, save_workouts

from fastapi.responses import FileResponse


router = APIRouter(prefix="/workouts")

workouts = load_workouts()


@router.get("/")
def get_workouts():
    return workouts


@router.get("/{workout_id}")
def get_workout(workout_id: int):

    for workout in workouts:
        if workout["id"] == workout_id:
            return workout


@router.post("/")
def add_workout(workout: Workout):

    new_workout = {
        "id": len(workouts) + 1,
        "exercise": workout.exercise,
        "sets": workout.sets,
        "reps": workout.reps,
        "weight": workout.weight,
        "date": workout.date
    }

    workouts.append(new_workout)

    save_workouts(workouts)

    return {
        "message": "Workout added",
        "workout": new_workout
    }


@router.delete("/{workout_id}")
def delete_workout(workout_id: int):

    for workout in workouts:
        if workout["id"] == workout_id:
            workouts.remove(workout)
            save_workouts(workouts)
            return {"message": "Workout deleted"}
        
    return {"error": "Workout not found"}


@router.put("/{workout_id}")
def update_workout(workout_id: int, workout: Workout):

    for existing_workout in workouts:
        if existing_workout["id"] == workout_id:

            existing_workout["exercise"] = workout.exercise
            existing_workout["sets"] = workout.sets
            existing_workout["reps"] = workout.reps
            existing_workout["weight"] = workout.weight
            existing_workout["date"] = workout.date

            save_workouts(workouts)

            return {
                "message": "Workout Updated",
                "workout": existing_workout
            }

    return {"message": "Workout Not Found"}