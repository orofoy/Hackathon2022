from CXParse import parse

inputMovieName = input("Enter the numbered Star Wars movie you want to find a quote from(1-6): ")

inputQuote = input("Enter a phrase to find in Star Wars Ep " + inputMovieName + ": ")
while len(inputQuote) <= 1:
    print("Error: Input must be a word and more than one character")
    inputQuote = input("Enter a phrase to find in Star Wars Ep " + inputMovieName + ": ")
total_array = parse(inputQuote, inputMovieName)
if len(total_array) == 0:
    print("Sorry, quote not found in Ep " + inputMovieName)
else:
    print("Quotes from Star Wars Ep " + inputMovieName + ": \n")
    for x in total_array:
        print(x)
