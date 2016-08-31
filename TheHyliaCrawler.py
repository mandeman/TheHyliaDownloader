from bs4 import BeautifulSoup
import urllib.request
import requests
from config import IP_ADDRESS


def get_link(url, loc):
    sc = requests.get(url).text
    soup = BeautifulSoup(sc, 'html.parser')
    i = 0

    for link in soup.findAll('a'):
        if r'http://anime.thehylia.com/soundtracks/' in link.get('href'):
            downloader(link.get('href'), loc)
            i += 1
            # print(links.get('href'))
    if i == 0:
        print("Sorry. No results.")
    else:
        print("Finished downloading!")


def downloader(songpage, loc):
    sc = requests.get(songpage).text
    soup = BeautifulSoup(sc, 'html.parser')
    for link in soup.findAll('a'):
        if r'http://anime.thehylia.com/soundtracks/' in link.get('href'):
            print("Downloading " + link.string)
            wapas(link.get('href'), loc, link.string)


def wapas(downloadpage, loc, songname):
    sc = requests.get(downloadpage).text
    soup = BeautifulSoup(sc, 'html.parser')
    for link in soup.findAll('a'):
        if (IP_ADDRESS in link.get('href')):
            urllib.request.urlretrieve(link.get('href'), loc + '\\' + songname + '.mp3')
            print(songname + " done.")


query = input(r"What anime's soundtrack are you looking for?")
loc = input("Enter download location : ")
get_link(r"http://anime.thehylia.com/search?search=" + query, loc)
