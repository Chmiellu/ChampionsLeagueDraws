from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Tuple
from model.team import Team
from services.draw_service import generate_pairs
from model.team import teams

app = FastAPI()


#@app.post("/drawpairs", response_model=List[Tuple[Team, Team]])
@app.get("/drawpairs", response_model=List[Tuple[str, str]])
def get_pairs() -> List[Tuple[str, str]]:
    pairs = generate_pairs(teams)
    return pairs
