import math

def hawkID():
    return("agbarloon")

def get_max(list):
  max = -math.inf
  for number in list:
    if number > max:
      max = number
  return max

def get_min(list):
  min = math.inf
  for number in list:
    if number < min:
      min = number
  return min

def get_common(list):
  max_dict = {}
  for num in list:
    if num in max_dict.keys():
      max_dict[num] += 1
    else:
      max_dict[num] = 1
  sorted_dict = dict(sorted(max_dict.items()))
  largest_key = None
  largest_value = 0
  for k,v in sorted_dict.items():
    if v > largest_value:
      largest_value = v
      largest_key = k
  return largest_key
    


def q1(infoDict, listOfLists):
  final_list = []
  for list in listOfLists:
    red_count = 0
    blue_count = 0
    green_count = 0
    for number in list:
      result = infoDict.get(number, None)
      if result == "red":
        red_count += 1
      if result == "blue":
        blue_count += 1
      if result == "green":
        green_count += 1
    if red_count > blue_count and red_count > green_count:
      final_list.append(get_max(list))
    if blue_count > red_count and blue_count > green_count:
      final_list.append(get_min(list))
    else:
      final_list.append(get_common(list))
  return final_list

#print(q1( {1:"purple", 2:"red", 3:"blue", 25:"red"}, [[4], [2,3,3], [1,2,3], [17]] ))

def q2(filename, minWordLengthToConsider = 1):
  text = open(filename, "r")
  text_list = [i for i in text]
  print(text_list)

print(q2("SMScollection.txt"))