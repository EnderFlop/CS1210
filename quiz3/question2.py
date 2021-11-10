def binarySearch(L, x): 
     finished = False
     low = 0
     high = len(L) - 1
     while (finished == False):
         midIndex = (low + high) // 2
         if x == L[midIndex]:
             finished = True
         elif L[midIndex] < x:
            low = midIndex + 1
         else: 
            high = midIndex - 1
     return midIndex
print(binarySearch(range(100000), 0))