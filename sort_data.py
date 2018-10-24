import pandas
df = pandas.read_csv('result_files/names.csv')
new_df = df.sort_values(by=['playerId', 'gameweek'], ascending=[True, True])
new_df.to_csv('result_files/sorted_names.csv', index=False)