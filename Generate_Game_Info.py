#Author: jdye@scu.edu
#Date: 2020-05-06
#Collaborators: https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters


import requests
from bs4 import BeautifulSoup
import csv

def get_prices():
    prices_list1 = list()
    price = soup.find_all('div', class_='col search_price_discount_combined responsive_secondrow')
    for x in price:
        prices_list1.append(x.text.split())
    prices_list2 = list()
    for x in prices_list1:
        new = " ".join(x)
        new = new.split('$')
        if new[-1] == '':
            new[-1] = '-1'
        if new[-1] == 'Free to Play' or new[-1] == 'Free' or new[-1] == 'Free To Play':
            new[-1] = '0'
        prices_list2.append(new[-1])
    return prices_list2

def get_urls():
    games_url = list()
    links = soup.find_all('a', href=True)
    count = 1
    for a in links:
        if 120 < count < 146:
            games_url.append(a['href'])
        count+=1
    return games_url

def get_genres():
    genres = soup.find_all('a', class_='app_tag')
    genres_list = list()
    for x in genres:
        genres_list.append(x.text.split())
    genres_list_complete = list()
    for x in genres_list:
        new = " ".join(x)
        genres_list_complete.append(new)
    return genres_list_complete

def get_descriptions():
    descriptions = soup.find_all('div', id='game_area_description')
    for x in descriptions:
        description = x.text.split()
        description = description[3:]
        description = ' '.join(description)
    return description

def get_release_date():
    release_date = soup.find_all('div', class_='date')
    for x in release_date:
        date = x.text
    return date

def get_titles():
    title = soup.find('div', class_='apphub_AppName')
    title = title.text
    return title

def get_trailers():
    try:
        video = soup.select_one('[data-webm-source]')['data-webm-source']
    except TypeError:
        video = 'Sorry No Trailer'
    return video


#lists to be imported to csv
total_prices = list()
total_urls = list()
total_genres = list()
total_descriptions = list()
total_release_dates = list()
total_titles = list()
total_trailers = list()


#Get Prices and URLS
for x in range(1,9):
    r = requests.get('https://store.steampowered.com/search/?category1=998&page={}'.format(x))
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #Prices
    prices = get_prices()
    lists_total_prices = list()
    lists_total_prices.append(prices)
    for sublist in lists_total_prices:
        for val in sublist:
            total_prices.append(val)

    #URLs
    urls = get_urls()
    lists_total_urls = list()
    lists_total_urls.append(urls)
    for sublist in lists_total_urls:
        for val in sublist:
            total_urls.append(val)

#Get Other Info
for x in total_urls:
    r = requests.get(x)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #Genres
    genres = get_genres()
    total_genres.append(genres)

    #Descriptions
    description = get_descriptions()
    total_descriptions.append(description)

    #Release_Date
    release_date = get_release_date()
    total_release_dates.append(release_date)

    #Titles
    title = get_titles()
    total_titles.append(title)

    #Trailer URL
    trailer = get_trailers()
    total_trailers.append(trailer)
    
with open('games.csv', mode='w', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'genre', 'price', 'date_released','description', 'url', 'movie_url']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for x in range(len(total_urls)):
        row = {'title': total_titles[x], 'genre': total_genres[x], 'price': total_prices[x], 'date_released': total_release_dates[x], 'description': total_descriptions[x], 'url': total_urls[x], 'movie_url': total_trailers[x]}
        writer.writerow(row)


