def listsmash(listu):
    y = ''
    for x in range(len(listu)):
        if x == len(listu) - 1:
            y += 'and ' + str(listu[x])
        else:
            y += str(listu[x]) + ','
    return y


print(listsmash([1, 345, 34656, 456456, 456454564]))
