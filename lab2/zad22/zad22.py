with open("nameslist.txt") as names:
    test = {}
    line = names.read()
    for name in line.split('\n'):
        if name in test:
            test[name] += 1
        else:
            test[name] = 1
            print (len(test))