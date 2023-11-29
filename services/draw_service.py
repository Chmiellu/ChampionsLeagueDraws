from typing import List, Tuple
from random import shuffle
from model.team import Team

def generate_pairs(teams: List[Team]) -> List[Tuple[str, str]]:

    pairs = []
    first_place_teams = [team for team in teams if team.group_rank == 1]
    second_place_teams = [team for team in teams if team.group_rank == 2]

    # Shuffle with condition to prevent scenario teams from the same country end up on the last two positions of the list
    def custom_shuffle(teams_list):
        shuffled_list = teams_list.copy()
        shuffle(shuffled_list)
        while any(shuffled_list[i].country == shuffled_list[i + 1].country for i in range(len(shuffled_list) - 1)):
            shuffle(shuffled_list)
        return shuffled_list

    first_place_teams = custom_shuffle(first_place_teams)
    second_place_teams = custom_shuffle(second_place_teams)


    for team1 in first_place_teams:
        team2 = None
        i = 0
        while i < len(second_place_teams):
            if len(second_place_teams) == 2:

                for team1 in first_place_teams[-2:]:
                    for team2 in second_place_teams:
                        if team1.country == team2.country:
                            repeat_country = team1.country
                            last = 0
                            for team1 in first_place_teams[-2:]:
                                for team2 in second_place_teams:
                                    if team1.country == repeat_country and team1.country != team2.country:
                                        pairs.append((team1.name, team2.name))
                                        continue
                                    elif team1.country != team2.country and last>0:
                                        pairs.append((team1.name, team2.name))
                                        continue
                                    last += 1
                            return pairs

            candidate_team = second_place_teams[i]
            if candidate_team.country != team1.country and candidate_team.group_letter != team1.group_letter:
                team2 = candidate_team
                del second_place_teams[i]
                break
            else:
                i += 1

        if team2 is not None:
            pairs.append((team1.name, team2.name))

    return pairs