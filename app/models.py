from pydantic import BaseModel


class Workout(BaseModel):
    exercise: str
    sets: int
    reps: int
    weight: int
    date: str