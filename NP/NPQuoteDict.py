from NPparse import parse
from NPparse import info

def findQuote(userQuote):

    f = open("SW3.txt", encoding='utf-8-sig')

    dict = {}
    r1 = info(None, None)
    foundQuote = False
    numOfOccurances = 0

    for line in f:
        r1 = parse(f)
        line = line.replace('\n', '')

        if userQuote.lower() in r1.quote.lower():
            numOfOccurances += 1
            dict[numOfOccurances] = r1

            foundQuote = True

    for i in range(numOfOccurances):
        print(dict[i])

    if not foundQuote:
        print("Could not find quote.")

    f.close()

