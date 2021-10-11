def f1w(inputString, inputDict, specialValue):
    s = 0
    s2 = 0
    a = 0.0
    i = 0
    while i < len(inputString):
        char = inputString[i]
        s = s + inputDict[char]
        if inputDict[char] == specialValue:
            s2 = s2 + 1
        i += 1
    a = s / len(inputString)
    return (a, s2)