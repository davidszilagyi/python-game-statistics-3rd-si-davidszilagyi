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
#print("Number of games: " + str(reports.count_games(file_name)))
#print("Year: " + str(year) + " - " + str(reports.decide(file_name, year)))
#print("Latest game: " + reports.get_latest(file_name))
#print("Genre: " + str(genre) + " - Count: " + str(reports.count_by_genre(file_name, genre)))
#print("The '" + str(title) +"' is there: " + str(reports.get_line_number_by_title(file_name, title)))
#print(reports.sort_abc(file_name))
#print(reports.get_genres(file_name))
#print(reports.when_was_top_sold_fps(file_name))