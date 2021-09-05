def hawkID():
    return("agbarloon")

def q1(origString, repeatCount, lettersToRepeat):
  new_str = ""
  while origString:
    letter = origString[0]
    if letter.lower() in lettersToRepeat:
      new_str += letter * repeatCount
    else:
      new_str += letter
    origString = origString[1:]
  return new_str

def q2(num, string1, string2):
  num_differences = 0
  index = 0
  shortest_len = min(len(string1), len(string2))
  while index < shortest_len:
    if string1[index] != string2[index]:
      num_differences += 1
    index += 1
  return len(string1) == len(string2) and num == num_differences

def q3(inputString, minLetter, lettersToIgnore, specialLetter):
  smallest_letter = "~"
  highest_index = None
  special_letter_count = 0
  i = 0
  while i < len(inputString):
    letter = inputString[i].lower()
    if letter == specialLetter:
      special_letter_count += 1
    if letter < smallest_letter and letter not in lettersToIgnore and letter > minLetter:
      smallest_letter = inputString[i]
    if letter == smallest_letter and letter not in lettersToIgnore and letter > minLetter:
      highest_index = i
    i += 1
  if smallest_letter == "~":
    smallest_letter = None
  return smallest_letter, highest_index, special_letter_count % 2 != 0


#print(q3("bccacbd", "a", "eb", "z"))
#print(q3("bccacbd", "a", "aefg", "d"))
#print(q3("abc", "d", "", "a"))
#print(q3("aaabac", "d", "", "a"))