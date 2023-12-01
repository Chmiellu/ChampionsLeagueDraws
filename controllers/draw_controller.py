from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import List, Tuple
from model.team import Team
from services.draw_service import generate_pairs
from model.team import teams

app = FastAPI()

@app.get("/drawpairsJSON", response_model=List[Tuple[str, str]])
def get_pairs() -> List[Tuple[str, str]]:
    pairs = generate_pairs(teams)
    return pairs

@app.get("/results", response_class=HTMLResponse)
def get_pairs() -> str:
    pairs = generate_pairs(teams)
    html_response = f"""
    <html>
    <head>
        <style>
            body {{
                font-size: 20px;
                font-family: Arial, sans-serif;
            }}
            h1 {{
                text-align: left;
                color: #3366cc;
                margin-left: 40px;
                margin-top: 20px;
            }}
            .pair {{
                margin-bottom: 20px;
                margin-left: 40px;
            }}
        </style>
    </head>
    <body>
        <h1>DRAW RESULTS</h1>
        {generate_html_pairs(pairs)}
    </body>
    </html>
    """

    return HTMLResponse(content=html_response)

def generate_html_pairs(pairs: List[Tuple[str, str]]) -> str:
    html_pairs = ""
    for pair in pairs:
        html_pairs += f"<div class='pair'>{pair[0]} vs {pair[1]}</div>"
    return html_pairs
