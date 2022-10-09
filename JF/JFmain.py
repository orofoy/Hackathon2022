from JFSWparse import parse



quote = input('Enter a Star Wars quote: \n')

validInput = False

while not validInput:
    if len(quote) > 1:
        parse(quote)
        validInput = True
    else:
        print('One-letter input not accepted.\n')
        quote = input('Please enter a word: \n')