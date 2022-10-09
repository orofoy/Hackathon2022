from NPparse import findQuote
from glob import glob
import os

# Returns a list of all the text files in the folder
def listOfFiles():
    list = os.listdir()
    textList = []
    for file in list:
        if ".srt" in file:
            textList.append(file)

    return textList

userQuote = input("Enter your quote: ")

if len(userQuote) >= 1:
    textFiles = listOfFiles()
    foundQuote = False
    for i in range(len(textFiles)):
            foundQuote = findQuote(userQuote, textFiles[i])

    # TODO: if found in first movie but not second it sets it back to false
    if not foundQuote:
        print("Could not find quote.")
else:
    print("You must type in a quote!")


