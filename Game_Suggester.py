#Author: jdye@scu.edu
#Date: 2020-05-06
#Collaborators: https://stackoverflow.com/questions/30565759/get-unique-values-in-list-of-lists-in-python, https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/

import csv
import ast
import sys

#Get all available genres
def get_possible_genres():
    
    #Creates list of genres from .csv
    possible_genres_list = list()
    with open('games.csv', mode='r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in reader:
            if count == 0:
                count +=1
                continue
            possible_genres_list.append(row[1])
    
    #Converts lists within possible_genres_list from strings back into lists
    possible_genres_list2 = list()
    for x in possible_genres_list:
        res = x.strip('][').split(', ')
        possible_genres_list2.append(res)
    
    #Removes Duplicates from possible_genres_list2
    possible_genres_quotes = set(x for l in possible_genres_list2 for x in l)
    possible_genres_quotes = list(possible_genres_quotes)

    #Fixes quotation marks of strings within the possible_genres_quotes list
    possible_genres = list()
    for x in possible_genres_quotes:
        x = x.strip("'")
        x = x.strip('"')
        x = x.upper()
        possible_genres.append(x)
    #Alphabetizes List
    possible_genres.sort()
    
    return possible_genres

def game_genres():
    #Creates list of genres from .csv
    possible_genres_list = list()
    with open('games.csv', mode='r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        count = 0
        total_genres = list()
        for row in reader:
            if count == 0:
                count +=1
                continue
            possible_genres_list.append(row[1])
    #Converts lists within possible_genres_list from strings back into lists
    possible_genres_list2 = list()
    for x in possible_genres_list:
        res = x.strip('][').split(', ')
        possible_genres_list2.append(res)

    #Fixes quotation marks of strings within the possible_genres_quotes list
    for y in possible_genres_list2:
        game_genres = list()
        for x in y:
            x = x.strip("'")
            x = x.strip('"')
            x = x.upper()
            game_genres.append(x)
        total_genres.append(game_genres)
    return total_genres


#Display Possible Genres
possible_genres = get_possible_genres()

restart = True
count = 1
while restart:
    print("\nGenres to choose from! P.S. There's a lot!\n")
    for x in range(len(possible_genres)):
        if (x % 10 == 0) and (x != 0):
            print('({})'.format(possible_genres[x]), end='\n')
        else:
            print('({})'.format(possible_genres[x]), end=' ')

    print()
    print()

    #Receive Desired Genres
    user_genres = list()
    user_genre_choice = ''
    print("\nEnter Desired Genres One At A Time, Enter 'done' When You Have Selected All Desired Genres.") 
    print("Alternatively, Quit The Program Using 'q' Or 'CTRL + C'.")
    print('Please Enter First Choice:')
    while user_genre_choice != 'DONE' or len(user_genres) == 0:
        try:
            user_genre_choice = input().upper()
            if user_genre_choice == 'Q':
                raise Exception('Quit')
        except Exception:
            sys.exit()
        except KeyboardInterrupt:
            sys.exit()
    
        if user_genre_choice in possible_genres and (user_genre_choice not in user_genres):
            print("Genre Added To Preferences, Please Enter Next Choice Or Enter 'done' To Continue.")
            user_genres.append(user_genre_choice)
            continue
        elif user_genre_choice in user_genres:
            print("Genre Already Added To Preferences, Please Enter Next Choice Or Enter 'done' To Continue.")
        elif user_genre_choice != 'DONE':
            print("Not An Option, Please Try Again Or Enter 'done' To Continue.")
        elif user_genre_choice == 'DONE' and len(user_genres) == 0:
            print("Cannot Find Game Suggestions Based On No Preferences. Please Enter At Least One Genre To Continue")

    print('\nGenres Selected: {}\n'.format(user_genres))

    #Received Desired Maximum Price
    done = False
    print("Please Enter Maximum Price For Game ($USD).")
    print("Alternatively, Quit The Program Using 'q' Or 'CTRL + C'.")
    while done == False:
        try:
            user_price = input().upper()
            if user_price == 'Q':
                raise Exception('Quit')
            elif float(user_price) >= 0:
                user_price = float(user_price)
                done = True
            elif float(user_price) < 0:
                print("Invalid Price. Please Try Again.")
        except ValueError:
            print('Not A Valid Price. Please Try Again.')
            continue
        except Exception:
            sys.exit()
        except KeyboardInterrupt:
            sys.exit()
    if count == 1:
        game_genres = game_genres()

    #Find Good Games For User
    good_games = dict()
    with open('games.csv', mode='r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        total_genres = list()
        row_num = 0
        next(reader, None)
        for row in reader:
            result = all(elem in game_genres[row_num] for elem in user_genres)
            if result and (float(row[2]) <= user_price):
                for x in row:
                    game = {'genres': game_genres[row_num], 'price': row[2], 'date_released': row[3], 'description': row[4] , 'url': row[5], 'movie_url': row[6]}
                    good_games[row[0]] = game
            row_num += 1
    if len(good_games) == 0:
        print('\nNo Games Matching Inputted Criteria. Please Re-Enter Parameters')
        count += 1
        continue

    if len(good_games) >= 1:
        count += 1
        #Show Games To User And Receive Feedback
        user_response = ''
        for key in good_games:
            if user_response != 'Y':
                title = key
                genres = ', '.join(good_games[key]['genres'])
                price = good_games[key]['price']
                if price == '-1':
                    price = "Price Unavailable, This Edition of Game May No Longer Be Available For Purchase."
                date_released = good_games[key]['date_released']
                description = good_games[key]['description']
                url = good_games[key]['url']
                movie_url = good_games[key]['movie_url']
                print('_____________________________________________________________________________________\n')
                print('Title:\n{}\n'.format(title))
                print('Genres:\n{}\n'.format(genres))
                if price == 'Price Unavailable, This Edition of Game May No Longer Be Available For Purchase.':
                    print('Price:\n{}\n'.format(price))
                else:
                    print('Price:\n${}\n'.format(price))
                print('Date Released:\n{}\n'.format(date_released))
                print('Description:\n{}\n'.format(description))
                print('URL:\n{}\n'.format(url))
                print('Trailer:\n{}\n'.format(movie_url))
                user_response = ''
                while user_response not in ['Y','N']:
                    user_response = input('Do You Like This Game? Please Enter Y/N\n').upper()
                    continue
        if user_response == 'Y':
            print('\nEnjoy Your New Game!\n')
            user_restart = ''
            while user_restart not in ['Y','N']:
                user_restart = input("Would You Like To Find A New Game? Enter Y/N\n").upper()
                if user_restart == 'N':
                    restart = False
        else:
            print('\nUnfortunately, There Are No More Games That Match Your Preferences\n')
            user_restart = ''
            while user_restart not in ['Y','N']:
                user_restart = input("Would You Like To Find A New Game? Enter Y/N\n").upper()
                if user_restart == 'N':
                    restart = False


