from NPparse import parse
from NPparse import info

userQuote = input("Enter your quote: ")

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

for i in range(1, numOfOccurances + 1):
    print(dict[i])

if not foundQuote:
    print("Could not find quote.")

f.close()