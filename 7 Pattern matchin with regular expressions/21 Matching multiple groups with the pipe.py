import re

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))


# Create your own class

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowels = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowels)