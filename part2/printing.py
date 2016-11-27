# Printing functions

import reports
import random

types = []
games = []

file_name = "game_stat.txt"
database = reports.open_file(file_name)

for game in database:
    games.append(game[0])
    if not game[3] in types:
        types.append(game[3])

year = random.randint(1990, 2016)
genre = types[random.randint(0,len(types)-1)]
title = games[random.randint(0,len(games)-1)]

#print(types)
#print(games)
#print("The title of the most played games: " + str(reports.get_most_played(file_name)))
#print("Total copies: " + str(reports.sum_sold(file_name)))
#print("Average selling: " + str(reports.get_selling_avg(file_name)))
#print("The longest title in characters: " + str(reports.count_longest_title(file_name)))
#print("The average release date is: " + str(reports.get_date_avg(file_name)))
#print("The properties of " + str(title) + ": " + str(reports.get_game(file_name, title)))
#print(reports.count_grouped_by_genre(file_name))
#print(reports.get_date_ordered(file_name))