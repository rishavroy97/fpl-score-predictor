import numpy as np
import pandas as pd

df = pd.read_csv('../mid_result_files/sorted_names.csv')

columns = ['mins-pm', 'team', 'opponent', 'cs-pm','goals-pm', 'assists-pm', 'yellow-cards-pm', 'red-cards-pm', 'bonus-pm', 'current-form', 'total']
new_df = pd.DataFrame(columns=columns)
start_index = 0
current_player_starting_index = start_index

for i in range(start_index, len(df)):
    # create a new player record
    new_row = {}
    
    # get the current player record
    row = df.iloc[i]
    current_player = row['playerId']
    new_row['team'] = row['team']
    new_row['opponent'] = row['opponent']

    # find number of matches
    number_of_matches = (row['gameweek'] - 1) * 1.0

    # for finding the player's first gameweek
    starting_row = df.iloc[current_player_starting_index]
    
    if number_of_matches == 0 or i == 0 or starting_row['playerId'] != current_player:
        
        # calculate for a new player
        # set a new player index
        current_player_starting_index = i

        new_row['mins-pm'] = 0
        new_row['goals-pm'] = 0
        new_row['assists-pm'] = 0
        new_row['cs-pm'] = 0
        new_row['yellow-cards-pm'] = 0
        new_row['red-cards-pm'] = 0
        new_row['bonus-pm'] = 0
        new_row['current-form'] = 0
        new_row['total'] = row['total']

        # print new_row

    else:
        # calculate all details
        total_mins = 0
        total_goals = 0
        total_assists = 0
        total_cs=0
        total_yc = 0
        total_rc = 0
        total_bonus = 0
        for j in range(current_player_starting_index, i):
            total_mins += df.iloc[j]['minutes-played']
            total_goals += df.iloc[j]['goals-scored']
            total_assists += df.iloc[j]['assists']
            total_cs +=df.iloc[j]['clean-sheet']
            total_yc += df.iloc[j]['yellow-cards']
            total_rc += df.iloc[j]['red-cards']
            total_bonus += df.iloc[j]['bonus']

        new_row['mins-pm'] = total_mins / number_of_matches
        new_row['goals-pm'] = total_goals / number_of_matches
        new_row['cs-pm'] = total_cs / number_of_matches
        new_row['assists-pm'] = total_assists / number_of_matches
        new_row['yellow-cards-pm'] = total_yc / number_of_matches
        new_row['red-cards-pm'] = total_rc / number_of_matches
        new_row['bonus-pm'] = total_bonus / number_of_matches
        new_row['total'] = row['total']

        # calculate form
        form_total = 0
        # n_of_matches = 0
        current_gameweek = row['gameweek']
        for j in range(1, 4):
            if i-j >= 0 and df.iloc[i-j]['gameweek'] >= current_gameweek-3 and (i-j)>=current_player_starting_index:
                form_total += df.iloc[i-j]['total']
                # n_of_matches+=1

        if number_of_matches == 1 or number_of_matches == 2:
            new_row['current-form'] = form_total / (number_of_matches * 1.0)
        else:
            new_row['current-form'] = form_total / 3.0 

    new_df.loc[i] = new_row

    print new_row

print new_df
new_df.to_csv('../mid_result_files/mid_data.csv', index=False)