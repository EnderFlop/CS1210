def q3(listOfPairs, startIndex):
    currentItem = listOfPairs[startIndex][0]
    resultString = [currentItem]
    nextIndex = listOfPairs[startIndex][1]
    while ( nextIndex != len(listOfPairs )):
      #update resultString
      resultString.append(listOfPairs[nextIndex][0])
      #update nextIndex
      nextIndex = listOfPairs[nextIndex][1]
    return resultString

lop = [['h', 2], ['w', 0], ['o', 4], ['e', 5], ['l', 3]]
print(q3(lop, 4))
