from NPQuoteDict import findQuote
from glob import glob
import os

# Returns a list of all the text files in the folder
def listOfFiles():
    list = os.listdir()
    textList = []
    for file in list:
        if ".txt" in file:
            textList.append(file)

    return textList

for i in range(len(listOfFiles())):
    print("hi")

userQuote = input("Enter your quote: ")

if len(userQuote) >= 1:
    findQuote(userQuote)
else:
    print("You must type in a quote!")