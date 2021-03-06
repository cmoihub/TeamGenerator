'''
    This program will be used to arrange members of the department
    into sub-units equally (for now) and randomly
    For example,
    Given A, B, C, D, E, F,G
    If you want to have 2 teams based on this you would get [A, B, C] & [D, E, F, G]
    in one scenario and [A, D, F] and [B, C, E, G]
    3 teams e.g. [A, B], [C, D], [E, F, G]
'''

import random

def generate_teams(no_of_teams, items, teams):
    '''
        this function arranges members into different teams
        items - array of items to arrange into teams
    '''
    for team in range(no_of_teams):
        if(is_empty(items)):
            return teams

        # collect last item         
        if(len(teams) != no_of_teams):
            teams.append([items.pop()])

        else:
            i = no_of_teams
            if i != 0:
                # add an item to each team
                for team in teams:
                    if(is_empty(items)):
                        return teams
                    team.append(items.pop())
                    i = i - 1
    # on next iteration another round of items/members will be added to the teams                     
    generate_teams(no_of_teams, items, teams)
    return teams

def generate_teams_random(no_of_teams, items, teams):
    '''
        this function arranges members into different teams
        items - array of items to arrange into teams in a randomized order
    '''
    validate_items(items)
    random.shuffle(items)
    shuffled_teams = generate_teams(no_of_teams, items, teams)
    return shuffled_teams

# Helper functions

def is_empty_using_len(items):
    return (len(items) == 0)

def is_empty(items):
    return (items == [])

def validate_items(items):
    remove_duplicates(items)
    remove_spaces(items)

def remove_duplicates(items):
    unique_items = set(items)
    items = list(unique_items)

def remove_spaces(items):
    for item in items:
        if item == ' ':
            items.remove(item)
