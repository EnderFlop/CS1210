import sys
sys.setrecursionlimit(1000)

def selectionSort(L):
    i = 0
    # invariant: L[0:i] sorted and in final position
    while i < len(L):
        minIndex = findMinIndex(L, i)
        L[i], L[minIndex] = L[minIndex], L[i]
        # now L[0:i+1] sorted an in final position.
        i = i + 1
        # L[0:i] sorted/in final position,and "loop invariant" (loop entry point assumption) holds again

        ## uncomment this if you want to see progress (don't do for large L though!)
        #print("sorted and in final pos:", L[0:i], "unsorted:", L[i:])

# return index of min item in L[startIndex:]
# assumes startIndex < len(L)
#
def findMinIndex(L, startIndex):
    minIndex = startIndex
    currIndex = minIndex + 1
    while currIndex < len(L):
        if L[currIndex] < L[minIndex]:
            minIndex = currIndex
        currIndex = currIndex + 1
    return minIndex

def insertionSort(L):
    i = 1
    
    # invariant: L[0:i] is sorted
    while i < len(L):
        itemToMove = L[i]
        # find where itemToMove should go, shifting larger items right one slot along the way
        j = i-1
        while ((j>=0) and (itemToMove<L[j])):
            L[j+1] = L[j]
            j = j-1

        # found the spot - put itemToMove there
        L[j+1] = itemToMove

        # now L[0:i+1] is sorted (though items not necessarily in final position)
        i = i + 1
        # L[0:i] sorted and "loop invariant" (loop entry point assumption) holds again

        ## uncomment this if you want to see progress (don't do for large L though!)
        #print("sorted:", L[0:i], "unsorted:", L[i:])
        
    return

# Recursive version of merge sort.  
# (It's much easier for most people to correctly implement mergesort recursively.)
# Note: this version modifies L itself, like the other sorts.
#
def mergeSort(L):
    if (len(L) < 2):
        return 
    else:
        # 1. divide list into (almost) equal halves
        middleIndex = len(L)//2
        left = L[:middleIndex]
        right = L[middleIndex:]
        
        #2. recursively sort left and right parts
        mergeSort(left)
        mergeSort(right)
        
        #3. merge sorted left/right parts
        mergedL = merge(left, right)
        
        # mergedL is now sorted but we need to do one more thing (related to Note above)
        # this copies the contents of margedL into L
        L[:] = mergedL[:]
        return
    
# Merge function used by both the recursive and non-recursive merge sorts.
def merge(L1, L2):
    mergedL = []
    iL1 = 0
    iL2 = 0

    while iL1 != len(L1) and iL2 != len(L2):
        if L1[iL1] <= L2[iL2]:
            mergedL.append(L1[iL1])
            iL1 = iL1 + 1
        else:
            mergedL.append(L2[iL2])
            iL2 = iL2 + 1

    # At this point, we've used up all the items from one of the lists.
    # Use list "extend" method to add all the remaining items to mergedL
    mergedL.extend(L1[iL1:])
    mergedL.extend(L2[iL2:])

    return mergedL

def builtinSort(L):
    L.sort()

def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
  
    for j in range(l , h):
        if   arr[j] <= x:
  
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)
  
# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quickSort(arr):
  
    # Create an auxiliary stack
    l=0
    h=len(arr) - 1
    size = h - l + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
  
        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False
  
        # loop from left to right same as the bubble
        # sort
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True
  
        # if nothing moved, then array is sorted.
        if (swapped==False):
            break
  
        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False
  
        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1
  
        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
  
        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start+1

##########

import random
# return a new list with the same elements as input L but randomly rearranged
def mixup(L):
    newL = L[:]
    length = len(L)
    for i in range(length):
        newIndex = random.randint(i,length-1)
        newL[newIndex], newL[i] = newL[i], newL[newIndex]
    return(newL)

##########

import time

def timeSort(sortfn, L):
    t1 = time.time()
    sortfn(L)
    t2 = time.time()
    return (t2 - t1)

# try, e.g.,
# l = mixup(list(range(4000)))
# timeAllSorts(l)
def timeAllSorts(L):

    Lcopy = L[:]
    sTime = timeSort(selectionSort, Lcopy)
    Lcopy = L[:]
    iTime = timeSort(insertionSort, Lcopy)
    Lcopy = L[:]
    mTime = timeSort(mergeSort, Lcopy)
    Lcopy = L[:]
    biTime = timeSort(builtinSort, Lcopy)
    Lcopy = L[:]
    quickTime = timeSort(quickSort, Lcopy)
    Lcopy = L[:]
    ctTime = timeSort(cocktailSort, Lcopy)
    
    print(f"{len(L)}\nSelection Sort {sTime}\nInsertion Sort {iTime}\nMerge Sort {mTime}\nBuilt-In Sort {biTime}\nQuick Sort {quickTime}\nCocktail Sort {ctTime}")


# The code below is commented out (with ''' before and after) so that the code above will run even
# when you are using a Python that does not have pylab.  If you are using a Python
# with pylab, remove the '''s.
# As demonstrated in Lectures 30 and 31, you can call "compareSorts" to produce a chart graphing
# running times of selection and insertion sort on randomly ordered lists of various sizes.
# For HW 7, use several functions like this (with additional sorting methods) to compare all the
#sorting methods on various kinds of data
#

import pylab
def compareCheapSorts(minN = 10000, maxN=200000, step=20000):
    listSizes = list(range(minN, maxN, step))
    selectionSortTimes = []
    insertionSortTimes = []
    mergeSortTimes = []
    builtInTimes = []
    quickSortTimes = []
    cocktailSortTimes = []
    
    for listSize in listSizes:
        #Random Data
        #listToSortOrig = mixup(list(range(listSize)))
        #Sorted Data
        #listToSortOrig = list(range(listSize))
        #Reverse Sorted Data
        listToSortOrig = list(range(listSize))
        listToSortOrig.reverse()
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #selectionSort(listToSort)
        endTime = time.time()
        selectionSortTimes.append(endTime-startTime)
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #insertionSort(listToSort)
        endTime = time.time()
        insertionSortTimes.append(endTime-startTime)
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        mergeSort(listToSort)
        endTime = time.time()
        mergeSortTimes.append(endTime-startTime)
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        builtinSort(listToSort)
        endTime = time.time()
        builtInTimes.append(endTime-startTime)
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #quickSort(listToSort)
        endTime = time.time()
        quickSortTimes.append(endTime-startTime)
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #cocktailSort(listToSort)
        endTime = time.time()
        cocktailSortTimes.append(endTime-startTime)
        
    pylab.figure(1)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Cheap Sorting Algorithms on Reverse Sorted Data (Quicksort Removed)")
    #pylab.plot(listSizes, selectionSortTimes, 'bo-', label="Selection Sort")
    #pylab.plot(listSizes, insertionSortTimes, 'ro-', label="Insertion Sort")
    pylab.plot(listSizes, mergeSortTimes, 'go-', label="Merge Sort")
    pylab.plot(listSizes, builtInTimes, 'mo-', label="Built-In Sort")
    #pylab.plot(listSizes, quickSortTimes, 'ko-', label="Quicksort")
    #pylab.plot(listSizes, cocktailSortTimes, 'co-', label="Cocktail Sort")
    pylab.legend(loc="upper left")

#compareCheapSorts()

def compareExpensiveSorts(minN = 1000, maxN=10000, step=1000):
    listSizes = list(range(minN, maxN, step))
    selectionSortTimes = []
    insertionSortTimes = []
    mergeSortTimes = []
    builtInTimes = []
    quickSortTimes = []
    cocktailSortTimes = []
    
    for listSize in listSizes:
        #Random Data
        #listToSortOrig = mixup(list(range(listSize)))
        #Sorted Data
        #listToSortOrig = list(range(listSize))
        #Reverse Sorted Data
        listToSortOrig = list(range(listSize))
        listToSortOrig.reverse()
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        selectionSort(listToSort)
        endTime = time.time()
        selectionSortTimes.append(endTime-startTime)
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        insertionSort(listToSort)
        endTime = time.time()
        insertionSortTimes.append(endTime-startTime)
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #mergeSort(listToSort)
        endTime = time.time()
        mergeSortTimes.append(endTime-startTime)
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #builtinSort(listToSort)
        endTime = time.time()
        builtInTimes.append(endTime-startTime)
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        #quickSort(listToSort)
        endTime = time.time()
        quickSortTimes.append(endTime-startTime)
        
        listToSort = listToSortOrig[:]
        startTime = time.time()
        cocktailSort(listToSort)
        endTime = time.time()
        cocktailSortTimes.append(endTime-startTime)
        
    pylab.figure(1)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Expensive Sorting Algorithms on Reverse Sorted Data")
    pylab.plot(listSizes, selectionSortTimes, 'bo-', label="Selection Sort")
    pylab.plot(listSizes, insertionSortTimes, 'ro-', label="Insertion Sort")
    #pylab.plot(listSizes, mergeSortTimes, 'go-', label="Merge Sort")
    #pylab.plot(listSizes, builtInTimes, 'mo-', label="Built-In Sort")
    #pylab.plot(listSizes, quickSortTimes, 'ko-', label="Quicksort")
    pylab.plot(listSizes, cocktailSortTimes, 'co-', label="Cocktail Sort")
    pylab.legend(loc="upper left")

#compareExpensiveSorts(minN=1000, maxN=10000, step=1000)
