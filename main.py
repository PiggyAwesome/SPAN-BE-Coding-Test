import string, operator, sys, os

number_correct = None
league = {}
final = []

log = False # Set to True for detailed logging

def read_file(filename: str):
    "Open file and read the contents into a list."
    with open(filename, "r") as game_stats:
        game_stats = game_stats.read().splitlines()                     
    return game_stats



def fix_spaces(game):
    """Enables support for whitespace in team names.
    Example: Change ['team', 'name', '1'] into ['team name', '1']"""

    detailed = []

    game_back = game                                            # Create backup of line for later use

    game = game.replace(",", "").split(" ")                     # Replace the comma with whitespace to prevent messing up split(). 
         
    assert game != game_back, "Format error"

    if len(game) > 4:                                           # Check if Team name contains spaces
        gamePt1 = game_back.split(", ")[0]                      # Put Team 1 Score into a var
        gamePt2 = game_back.split(", ")[1]                      # Put Team 2 Score into a var

        gamePt1_name = " ".join(gamePt1.split(" ")[0:-1])       # Filter Team 1 name into a var 
        gamePt1_point = gamePt1.split(" ")[-1]                  # Filter Team 1 points into a var 

        gamePt2_name = " ".join(gamePt2.split(" ")[0:-1])       # Filter Team 2 name into a var 
        gamePt2_point = gamePt2.split(" ")[-1]                  # Filter Team 2 points into a var 


        assert gamePt1 != None, "Error happened while correcting whitespaces"
        assert gamePt2 != None, "Error happened while correcting whitespaces"
        assert gamePt1_name != None, "Error happened while correcting whitespaces"
        assert gamePt2_name != None, "Error happened while correcting whitespaces"
        assert gamePt1_point != None, "Error happened while correcting whitespaces"
        assert gamePt2_point != None, "Error happened while correcting whitespaces"

        "Merge the new values into a list"
        detailed.append(gamePt1_name)
        detailed.append(gamePt1_point)
        detailed.append(gamePt2_name)
        detailed.append(gamePt2_point)

        return detailed

    else:
        return game


def points_calc(game):
    "Calculate the points that each team have"
    team1_points = 0
    team2_points = 0
    if game[1] == game[-1]:
        team1_points += 1
        team2_points += 1
        if log == True:
            print(f"TIE: {game[0]} {game[1]} : {game[2]} {game[3]}")

    elif game[1] > game[-1]:
        team1_points += 3
        team1_points += 0
        if log == True:
            print(f"WIN: {game[0]} {game[1]} : {game[2]} {game[3]}")
    elif game[-1] > game[1]:
        team2_points += 3  
        team1_points += 0
        if log == True:
            print(f"WIN: {game[2]} {game[3]} : {game[0]} {game[1]}")

    return [game[0], team1_points, game[2], team2_points]

def update_leagues(detailed):
    "Update dictionary containing each team's stats"
    if detailed[0] in league:                                           # If team already exists in dictionary
        league[detailed[0]] = league[detailed[0]] + int(detailed[1])    # Add the value to the current value
    else:
        league[detailed[0]] = int(detailed[1])                          # Else create item

    if detailed[2] in league:                                           # If team already exists in dictionary
        league[detailed[2]] = league[detailed[2]] + int(detailed[3])    # Add the value to the current value
    else:
        league[detailed[2]] = int(detailed[3])                          # Else create item

    assert league != detailed, "Error while updating leagues"
    return league


def format_league(league):
    "Sort the dictionary by value using operator. Then, reverse to sort from most points to least"

    assert type(league) == dict, "Error, leauge should be dict"
    league = dict(sorted(league.items(), key=operator.itemgetter(1), reverse=True))
    number_correct = None

    prevItem = list(league)[0]                                                          # Set a value to prevItem

    number = 1                         
    number_accurate = 0
    
    for item in league:   
        number_accurate += 1
        s = "s"
        if league[item] == 1:                                                           # Correct plurals
            s = "" 
        if s == "" :                  
            assert league[item] == 1, "Error, plurals is incorrect"


        if league[item] == league[prevItem]:                                            # Make sure that the number stays the same if game ends as a tie.
            number_correct = False
            pass
        else:   
            number += 1                                                                 # Forward to next number
            if number_correct == False:
                number = number_accurate         
            number_correct = True
        formated = f"{number}. {item}, {league[item]} pt{s}"

        assert formated != league, "impossible error detected."

        final.append(formated)                                                        


        prevItem = item

    return sorted(final)                                                              # Sort the ties alphabetically
        


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        assert os.path.exists(filename), "Game log file not found"
        game_stats = read_file(filename)                        # Open file and read the contents into a list.
    except IndexError:
        print(f"Incorrect Arguments. Format: python {__file__} <game-logs-filename>")
        exit()
    for game in game_stats:                                     # For each different game
        detailed = fix_spaces(game)                             # If user uses spaces in team names
        detailed = points_calc(detailed)                        # Calculate points from game score
        league = update_leagues(detailed)                       # Update dictionary containing each team's stats
    final = format_league(league)
    with open(filename.split(".")[0] + "_output." + filename.split(".")[1], "w") as output_file:
        output_file.write("\n".join(final))
    print("\n".join(final))
