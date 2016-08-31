from bs4 import BeautifulSoup
import urllib.request
import requests


def linkget(url, loc):
    sc = requests.get(url).text
    soup = BeautifulSoup(sc, 'html.parser')
    i = 0

    for links in soup.findAll('a'):
        if r'http://anime.thehylia.com/soundtracks/' in links.get('href'):
            downloader(links.get('href'), loc)
            i += 1
            # print(links.get('href'))
    if i == 0:
        print("Sorry. No results.")
    else:
        print("Finished downloading!")


def downloader(songpage, loc):
    sc = requests.get(songpage).text
    soup = BeautifulSoup(sc, 'html.parser')
    for links in soup.findAll('a'):
        if r'http://anime.thehylia.com/soundtracks/' in links.get('href'):
            print("Downloading " + links.string)
            wapas(links.get('href'), loc, links.string)


def wapas(downloadpage, loc, songname):
    sc = requests.get(downloadpage).text
    soup = BeautifulSoup(sc, 'html.parser')
    for links in soup.findAll('a'):
        if (r'http://50.7.54.34/' in links.get('href')):
            urllib.request.urlretrieve(links.get('href'), loc + '\\' + songname + '.mp3')
            print(songname + " done.")


query = input(r"What anime's soundtrack are you looking for?")
loc = input("Enter download location : ")
linkget(r"http://anime.thehylia.com/search?search=" + query, loc)
