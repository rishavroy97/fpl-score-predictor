import csv

with open('main_data/14-15.csv', 'r') as main_file:
    
    csv_reader = csv.DictReader(main_file)

    with open('result_files/names.csv', 'w') as fwd_file:
        fieldnames = ['playerId', 'gameweek', 'name', 'minutes-played', 'team', 'opponent', 'goals-scored', 'assists', 'yellow-cards', 'red-cards', 'bonus', 'total']
        csv_writer = csv.DictWriter(fwd_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        line_count = 0
        for line in csv_reader:
            if line['Pos'] == 'FWD':
                player = {}
                player['playerId'] = line['PID']
                player['name'] = line['Name']
                player['minutes-played'] = line['MP ']
                player['team'] = line['Team']
                player['opponent'] = line['Opponent']
                player['gameweek'] = line['GW']
                player['goals-scored'] = line['GS ']
                player['assists'] = line['A ']
                player['yellow-cards'] = line['YC ']
                player['red-cards'] = line['RC ']
                player['bonus'] = line['B ']
                player['total'] = line['TP ']
                
                csv_writer.writerow(player)
                line_count += 1

        print(line_count)