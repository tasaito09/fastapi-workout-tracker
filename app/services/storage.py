import json

def load_workouts():
    try:
        with open("workouts.json", "r") as file:
            return json.load(file)
    
    except FileNotFoundError:
        return []


def save_workouts(workouts):
    with open("workouts.json", "w") as file:
        json.dump(workouts, file)