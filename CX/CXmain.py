from CXParse import parse

inputQuote = input("Enter a phrase to find in Star Wars Ep 3: ")
while len(inputQuote) <= 1:
    print("Error: Input must be a word and more than one character")
    inputQuote = input("Enter a phrase to find in Star Wars Ep 3: ")
total_array = parse(inputQuote)
if len(total_array) == 0:
    print("Sorry, quote not found.")
else:
    for x in total_array:
        print(x)
