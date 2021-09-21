import math

def hawkID():
    return("agbarloon")

def how_many(string, char):
  # i miss .count()
  char_count = 0
  for character in string:
    if character.lower() == char:
      char_count += 1
  return char_count

def q1(inputString, minLetter):
  #Return 6 things
  #Smallest letter and the smallest index it occurs
  #third smallest letter and smallest index
  #most common letter and how many times
  first_smallest, second_smallest, third_smallest = None, None, None
  fs_index, ss_index, ts_index = None, None, None
  most_common_letter_count, most_common_letter = None, None
  for index in range(len(inputString)):
    letter = inputString[index]
    #If the letter meets requirements for checking
    if letter >= minLetter:
      #If there is no smallest or the letter is smaller than current smallest
      if first_smallest == None or letter < first_smallest:
        third_smallest, ts_index = second_smallest, ss_index
        second_smallest, ss_index = first_smallest, fs_index
        first_smallest, fs_index = letter, index
      #elif the letter is different from the first smallest and smaller than the second smallest
      elif letter != first_smallest and (second_smallest == None or letter < second_smallest):
        third_smallest, ts_index = second_smallest, ss_index
        second_smallest, ss_index = letter, index
      #elif the letter isn't either of the other two and is smaller than the third smallest
      elif letter != first_smallest and letter != second_smallest and (third_smallest == None or letter < third_smallest):
        third_smallest, ts_index = letter, index

    letter_count = how_many(inputString, letter)
    if most_common_letter_count == None or letter_count > most_common_letter_count:
      most_common_letter = letter
      most_common_letter_count = letter_count
    elif letter_count == most_common_letter_count:
      if letter > most_common_letter:
        most_common_letter = letter

  return first_smallest, fs_index, third_smallest, ts_index, most_common_letter, most_common_letter_count

#print(q1('aacyYcqyQQqyqc', 'b'))
#print(q1('aacyYcqyQQqyqc', 'r'))
#print(q1('adbc', 'a'))

def q2(L, goalX, goalY):
  #L is list of x,y pairs [[x,y], [x2,y2], [x3,y3]]
  #return closest distance X or Y from all coords, and "XMIN" if it's X, "YMIN" if it's Y
  closest_pair, closest_distance_type = None, None
  closest_diff = math.inf
  for pair in L:
    x = pair[0]
    y = pair[1]
    x_distance = abs(goalX - x)
    y_distance = abs(goalY - y)
    if x_distance < closest_diff:
      closest_diff = x_distance
      closest_pair = pair
      closest_distance_type = "XMIN"
    if y_distance < closest_diff:
      closest_diff = y_distance
      closest_pair = pair
      closest_distance_type = "YMIN"
  return closest_pair, closest_distance_type

#print(q2([[4, 4], [10, 10]], 1, 8))
#print(q2([[10, 25], [2, 2], [49, 200]], 50, 8))

def q3(L):
  summation = []
  positive_lists = 0
  maximum_value = None
  for lst in L:
    temp_sum = 0
    pos_vs_neg = 0
    for item in lst:
      temp_sum += item
      if item > 0:
        pos_vs_neg += 1
      elif item < 0:
        pos_vs_neg -= 1
      if maximum_value == None or item > maximum_value:
        maximum_value = item
    if pos_vs_neg >= 1:
        positive_lists += 1
    summation.append(temp_sum)
  return summation, positive_lists, maximum_value

#print(q3([[1, 2, 2], [3]]))
#print(q3([[0, 1, 0], [], [-1, 100]]))
#print(q3([]))
