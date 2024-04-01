import pprint

message = "It was a bright and cold day in April."

count = {}

for charater in message:
    count.setdefault(charater, 0)
    count[charater] = count[charater] + 1
pprint.pprint(count)

