#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: separate lines and add starts 

lines = text.split("\n")
for i in range(len(lines)): # loop rhough all indexes in the lines list
    lines[i] = "* " + lines[i] # add star to each string in "lines" list

text = "\n".join(lines)
pyperclip.copy("Lists of animals, Lists of aquarium life, ists of biologists by author abbreviation, Lists of cultivars")
print(text)