from typing import List, Tuple
from random import shuffle
from model.team import Team


def generate_pairs(teams: List[Team]) -> List[Tuple[str, str]]:
    teams_grouped_by_country = {}
    teams_grouped_by_group = {}

    for team in teams:
        if team.country not in teams_grouped_by_country:
            teams_grouped_by_country[team.country] = []
        teams_grouped_by_country[team.country].append(team)

        if team.group_letter not in teams_grouped_by_group:
            teams_grouped_by_group[team.group_letter] = []
        teams_grouped_by_group[team.group_letter].append(team)

    pairs = []
    for letter in set([team.group_letter for team in teams]):
        group_teams = teams_grouped_by_group[letter]
        shuffle(group_teams)

        teams_1st_place = [team for team in group_teams if team.group_rank == 1]
        teams_1st_place_shuffled = list(teams_1st_place)
        shuffle(teams_1st_place_shuffled)

        teams_2nd_place = [team for team in group_teams if team.group_rank == 2]
        shuffle(teams_2nd_place)

        for team1 in teams_1st_place_shuffled:
            possible_opponents = [team for team in teams if team.group_rank == 2 and team.country != team1.country and team.group_letter != team1.group_letter]
            shuffle(possible_opponents)

            if possible_opponents:
                team2 = possible_opponents[0]
                pairs.append((team1.name, team2.name))
                if team2 in teams_2nd_place:
                    teams_2nd_place.remove(team2)

    return pairs