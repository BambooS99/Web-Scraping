from bs4 import BeautifulSoup
import requests
songs = [] #define the array 
artists = []
songs2=[] #replacement array


#export to CSV so import csv and import random


html_text = requests.get('https://open.spotify.com/playlist/1OZfqkDU1cN104BLy8Xw1Z').text
    
import urllib.request  
soup = BeautifulSoup(html_text, 'lxml')
songNames = soup.find_all('span', class_ = 'track-name')
for song in songNames:                    
    songs = song.text 

songs2 = [x.strip(' ') for x in songs]

   # html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+songs)
    #print(html.read())

artistNames = soup.find_all('span', dir = 'auto')
for artist in artistNames:
    artists = artist.next
    print(artists)
    print(songs2)