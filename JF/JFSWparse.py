from srtFormat import isCount
from srtFormat import isTime
import collections

def parse(quote):

    count = ''
    time = ''
    subtitle = ''
    movieNum = 0
    movieToFile = {'Star Wars: The Phantom Menace': 'SW1.txt', 'Star Wars: Attack of the Clones': 'SW2.txt', 'Star Wars: Revenge of the Sith': 'SW3.txt', 'Star Wars: A New Hope': 'SW4.txt', 'Star Wars: Empire Strikes Back': 'SW5.txt', 'Star Wars: Return of the Jedi': 'SW6.txt'}
    quoteOrder = []
    for movie in movieToFile:
        with open(movieToFile[movie], encoding='utf-8-sig') as f:
            for lines in f:
                if isCount(lines):
                    count = lines
                elif isTime(lines):
                    time = lines
                elif lines != '\n':
                    subtitle += lines
                else:
                    quoteOrder.append([movie, count, time, subtitle])
                    subtitle = ''

    f.close()
    for quotes in quoteOrder:
        if quote.lower() in quotes[3].lower():
            print(quotes[0])
            print(quotes[2])
            print(quotes[3])