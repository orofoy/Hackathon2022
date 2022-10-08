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

