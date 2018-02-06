import json                         #importing json module
from difflib import get_close_matches

data = json.load(open("data.json")) #loading the data in json file in data in the form of dictionary
def translate(word):
    word = word.lower()             #converting the input word into lower case
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]   #Using for words having abbreviations
    elif word.title() in data:
        return data[word.title()]   #using for common nouns
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) >0:        #checking if a similar word exists
        usr = input("Did you mean %s instead?" %get_close_matches(word, data.keys())[0]).lower()    #taking the first closest match
        if usr == 'y':
            word = get_close_matches(word, data.keys())[0]
            return data[word]
        else:
            return "Word doesnt exist"
    else:
        return "The input word is invalid"

word = input("Enter the word you want the meaning for: ")
output = translate(word)

#followring code is to format the output properly
if type(output) == list:        #checking if the output of program is from correct function or the invalid output
    for item in output:
        print (item)
else:
    print(output)