from pydantic import BaseModel

class Team(BaseModel):
    name: str
    country: str
    group_rank: int
    group_letter: str

team1 = Team(name="Manchester City", country="EN", group_rank=1, group_letter="A")
team2 = Team(name="Paris Saint-Germain", country="FR", group_rank=2, group_letter="A")
team3 = Team(name="Liverpool", country="EN", group_rank=1, group_letter="B")
team4 = Team(name="Atlético Madryt", country="ES", group_rank=2, group_letter="B")
team5 = Team(name="AJAX", country="NED", group_rank=1, group_letter="C")
team6 = Team(name="Sporting CP", country="POR", group_rank=2, group_letter="C")
team7 = Team(name="Real Madryt", country="ES", group_rank=1, group_letter="D")
team8 = Team(name="Inter Mediolan", country="IT", group_rank=2, group_letter="D")
team9 = Team(name="Bayern Monachium", country="DE", group_rank=1, group_letter="E")
team10 = Team(name="SL Benfica", country="POR", group_rank=2, group_letter="E")
team11 = Team(name="Manchester United", country="EN", group_rank=1, group_letter="F")
team12 = Team(name="Villarreal CF", country="ES", group_rank=2, group_letter="F")
team13 = Team(name="Lille OSC", country="FR", group_rank=1, group_letter="G")
team14 = Team(name="Red Bull Salzburg", country="AU", group_rank=2, group_letter="G")
team15 = Team(name="Juventus", country="IT", group_rank=1, group_letter="H")
team16 = Team(name="Chelsea", country="EN", group_rank=2, group_letter="H")

teams = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12, team13, team14, team15, team16]