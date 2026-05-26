from fastapi import FastAPI
from app.routes.workouts import router


app = FastAPI()


app.include_router(router)