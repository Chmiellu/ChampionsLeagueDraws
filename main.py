from fastapi import FastAPI
from controllers.draw_controller import app as controllers_app
from model.team import teams
from services.draw_service import generate_pairs

app = FastAPI()

app.include_router(controllers_app.router)

print(generate_pairs(teams))
