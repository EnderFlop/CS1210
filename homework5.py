def hawkID():
    return("agbarloon")

def q1(n):
  if n == 1 or n == 0:
    return [1]
  list = [n**2]
  recurse = q1(n-1)
  list = recurse + list + recurse
  return list

#print(q1(5))

def q2(n, listOfStrings):
  if len(listOfStrings) == 0: #If nothing in list, return 0
    return 0
  if len(listOfStrings[0]) < n: #If condition met, add 1 and continue
    return 1 + q2(n, listOfStrings[1:])
  return 0 + q2(n, listOfStrings[1:]) #If condition failed, add 0 and continue

#print(q2(4, ['hi', 'bye', 'goodbye', 'hello']))
#print(q2(10, ['hi', 'bye', 'goodbye', 'hello']))
#print(q2(2, ['hi', 'bye', 'goodbye', 'hello']))
#print(q2(5, ['hello', 'bye']))

def q3(item1, item2):
  type1 = type(item1)
  type2 = type(item2)
  if type1 == list and type2 == list and len(item1) == len(item2): #If they are lists
    result = True
    for i in range(len(item1)):
      if q3(item1[i], item2[i]) == False:
        result = False
    return result
  if (type1 == type2 or (type1 == int and type2 == float) or (type1 == float and type2 == int)) and type1 != list: #If they are the same type and not lists
    return True
  else:
    return False
  
#print(q3(True, False))
#print(q3(1, 'a'))
#print(q3([],[]))
#print(q3([],[3]))
#print(q3(['c'],[3]) )
#print(q3([5.0],[3]))
#print(q3([1,2,['a','b']],[3,4, [1,2,3]]))
#print(q3([1,2,[False, 'b']],[3, 4, [True, 'hello']]))
#print(q3([[[[],[2],[],['hi', [0]]]]], [[[[],[-2],[],['bye', [1]]]]]))
#print(q3([[[[],[2],[],['hi', [0]]]]], [[[[],[-2],[],['bye', 0]]]]))