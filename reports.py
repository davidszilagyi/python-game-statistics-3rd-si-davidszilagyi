# Report functions

import re
import export

def open_file(file_name):
    file_ = open(file_name, "r+")

    database = []

    for lines in file_:
        database.append(re.split("\t|\n", lines))

    file_.close

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

def count_games(file_name):
    a_text = ("How many games are in the file?:")

    export.export_answers(a_text, len(open_file(file_name)))

    return len(open_file(file_name))

def decide(file_name, year):
    a_text = ("Is there a game from a given year?:")

    database = open_file(file_name)

    for games in database:
        if games[2] == str(year):
            export.export_answers(a_text, "True")
            return True
    
    export.export_answers(a_text, "False")

def get_latest(file_name):
    a_text = "Which was the latest game?:"

    database = open_file(file_name)

    year_ = database[0][2]

    for games in database:
        if games[2] > year_:
            year_ = games[2]
            latest = games[0]
        elif games[2] == year_:
            pass
    
    export.export_answers(a_text, latest)

    return latest

def count_by_genre(file_name, genre):
    a_text = "How many games do we have by genre?:"

    database = open_file(file_name)

    count = 0

    for games in database:
        if games[3] == genre:
            count += 1
    
    export.export_answers(a_text, count)

    return count

def get_line_number_by_title(file_name, title):
    a_text = "What is the line number of the given game (by title)?:"

    database = open_file(file_name)

    for games in database:
        try:
            if games[0] == title:
                export.export_answers(a_text, database.index(games) + 1)
                return database.index(games) + 1
        except ValueError:
            export.export_answers(a_text, ("There is no game like " + title))
            return ("There is no game like " + title)

def sort_abc(file_name):
    a_text = "What is the alphabetical ordered list of the titles?:"

    sorting = abc_sorting(open_file(file_name), 0)

    export.export_answers(a_text, sorting)

    return sorting

def get_genres(file_name):
    a_text = "What are the genres?"

    sorting = abc_sorting(open_file(file_name), 3)

    export.export_answers(a_text, sorting)

    return sorting

def when_was_top_sold_fps(file_name):
    a_text = "What is the release date of the top sold 'First-person shooter' game?:"

    database = open_file(file_name)

    top_sold = 0

    for games in database:
        if games[3] == "First-person shooter":
            if float(games[1]) > float(top_sold):
                top_sold = float(games[1])
                year_ = int(games[2])
    
    export.export_answers(a_text, year_)

    return year_