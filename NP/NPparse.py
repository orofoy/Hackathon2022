
class info:
    def __init__(self, timeStamp, quote):
        self.timeStamp = timeStamp;
        self.quote = quote;
    def __str__(self):
        return "Time Stamp: " + self.timeStamp + "\nQuote:\n" + self.quote + "\n"

    def __set__(self, instance, value):
        self.instance = value;

    def __get__(self, instance):
        return self.instance
def parse(f):

    r1 = info("", "")

    # Read timestamp
    line = f.readline()
    r1.timeStamp = line

    quote = ""
    while line != '\n':

        line = f.readline()
        quote = quote + " " + line

    r1.quote = quote

    return r1

def findQuote(userQuote, movieFile):

    f = open(movieFile, encoding='utf-8-sig')

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

    return foundQuote

    f.close()