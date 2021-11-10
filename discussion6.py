def hawkID():
    return("agbarloon")

def replaceVowels(input_string, replacement):
  if input_string == "":
    return ""
  if input_string[0] in "aeiou":
    return replacement + replaceVowels(input_string[1:], replacement)
  else:
    return input_string[0] + replaceVowels(input_string[1:], replacement)
  
#print(replaceVowels("hello", "z"))
#print(replaceVowels("hi", "aa"))
#print(replaceVowels("goodbye", ""))

def printContents(content):
  for item in content:
    if type(item) == list:
      printContents(item)
    else:
      print(item)

#printContents([1,2,"a"])
#printContents([1, [], 'a', [[[[3,4]]]], [[5],99]])