from typing import List, Tuple
from random import shuffle
from model.team import Team, teams

def generate_pairs(teams: List[Team]) -> List[Tuple[str, str]]:
    original_first_place_teams = [team for team in teams if team.group_rank == 1]
    original_second_place_teams = [team for team in teams if team.group_rank == 2]

    while True:
        pairs = []
        first_place_teams = original_first_place_teams.copy()
        second_place_teams = original_second_place_teams.copy()
        shuffle(first_place_teams)
        shuffle(second_place_teams)
        sum = 0
        next_draw = False

        for team1 in first_place_teams:
            team2 = None
            i = 0
            while i < len(second_place_teams):
                candidate_team = second_place_teams[i]
                if candidate_team.country != team1.country and candidate_team.group_letter != team1.group_letter:
                    team2 = candidate_team
                    del second_place_teams[i]
                    break
                else:
                    i += 1
                    if len(second_place_teams) == i:
                        next_draw = True
            if next_draw:
                break

            if team2 is not None:
                pairs.append((team1.name, team2.name))
                sum += 1

        if sum == 8:
            break

    return pairs

print(generate_pairs(teams))
