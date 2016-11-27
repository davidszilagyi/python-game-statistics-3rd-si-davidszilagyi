# Report functions

import math
import export

def open_file(file_name):
    file_ = open(file_name, "r+")

    database = []

    for lines in file_:
        database.append(lines.strip().split("\t"))

    file_.close()

    return database

def abc_sorting(a_list, a_index):
    datas = []
    datas_lowercase = []
    sorted_list = []

    for names in a_list:
        if not names[a_index] in datas:
            datas.append(names[a_index])
            datas_lowercase.append(names[a_index].lower())

    while datas:
        smallest = min(datas_lowercase)
        smallest_index = datas_lowercase.index(smallest)
        small = datas[smallest_index]
        sorted_list.append(small)
        datas.pop(datas.index(small))
        datas_lowercase.pop(datas_lowercase.index(smallest))

    return sorted_list

def get_most_played(file_name):
    a_text = "What is the title of the most played game?:"

    database = open_file(file_name)

    top_copies = float(database[0][1])
    latest = database[0][0]

    for games in database:
        if float(games[1]) > top_copies:
            top_copies = float(games[1])
            latest = games[0]
        elif float(games[1]) == top_copies:
            pass
    
    export.export_answers(a_text, latest)

    return latest

def sum_sold(file_name):
    a_text = "How many copies have been sold total?:"

    database = open_file(file_name)

    sum_total = 0

    for games in database:
        sum_total += float(games[1])

    export.export_answers(a_text, sum_total)

    return sum_total

def get_selling_avg(file_name):
    a_text = "What is the average selling?:"

    database = open_file(file_name)

    avg_total = 0

    for games in database:
        avg_total += float(games[1])
    
    avg_total = avg_total / len(database)

    export.export_answers(a_text, avg_total)

    return avg_total

def count_longest_title(file_name):
    a_text = "How many characters long is the longest title?:"

    database = open_file(file_name)

    names = []

    for games in database:
        names.append(games[0])

    longest = 0

    for titles in names:
        count = 0
        for char in titles:
            count += 1
        if count > longest:
            longest = count

    export.export_answers(a_text, longest)

    return longest

def get_date_avg(file_name):
    a_text = "What is the average of the release dates?:"

    database = open_file(file_name)

    sum_year = 0

    for games in database:
        sum_year += int(games[2])
    
    avg_year = math.ceil(sum_year / len(database))

    export.export_answers(a_text, avg_year)

    return avg_year

def get_game(file_name, title):
    a_text = "What properties has a game?:"

    database = open_file(file_name)

    properties = []

    for games in database:
        if games[0] == title:
            for i in range(len(games)):
                try:
                    properties.append(float(games[i]))
                except ValueError:
                    properties.append(games[i])
    
    export.export_answers(a_text, properties)

    return properties

def count_grouped_by_genre(file_name):
    a_text = "How many games are there grouped by genre?:"

    database = open_file(file_name)

    dictionary = {}

    genres = abc_sorting(database, 3)

    for types in genres:
        count = 0
        for games in database:
            if games[3] == types:
                count += 1
        dictionary[types] = count

    export.export_answers(a_text, dictionary)
    
    return dictionary

def get_date_ordered(file_name):
    a_text = "What is the date ordered list of the games?:"

    database = open_file(file_name)

    year_d = {}

    for games in database:
        if not int(games[2]) in year_d:
            titles = []
            
            for datas in database:
                if int(datas[2]) == int(games[2]):
                    titles.append(datas[0])
            
            lowercase = []
            sorted_titles = []

            for names in titles:
                if not names in lowercase:
                    lowercase.append(names.lower())

            while lowercase:
                smallest = min(lowercase)
                smallest_index = lowercase.index(smallest)
                small = titles[smallest_index]
                sorted_titles.append(small)
                titles.pop(titles.index(small))
                lowercase.pop(lowercase.index(smallest))

            year_d[int(games[2])] = sorted_titles

    temp = list(dict.values(year_d))
    
    ordered = []

    for i in range(len(temp)-1, -1, -1):
        if len(temp[i]) > 1:
            for x in range(0, len(temp[i])):
                ordered.append(temp[i][x])
        else:
            ordered.append(temp[i][0])

    export.export_answers(a_text, ordered)

    return ordered