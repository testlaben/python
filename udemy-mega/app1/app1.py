from __future__ import print_function
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean \"%s\"? Enter y/n: "% get_close_matches(w, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == "n":
            return "The word doesn't exist!"
        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist!"

w = input("Enter word: ")

output = translate(w)
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
