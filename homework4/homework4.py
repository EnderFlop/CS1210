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

def count_unique_words(list_of_lists):
  unique = {}
  for list in list_of_lists:
    for word in list:
      if word in unique:
        unique[word] += 1
      else:
        unique[word] = 1
  return unique

def sort_dict(dict, min_word_length, number_of_words):
  #take in a dictionary of word:frequency, give back ten most common words that are longer than min_word_length
  valid_dict = {}
  for k,v in dict.items():
    if len(k) >= min_word_length:
      valid_dict[k] = v

  #sort dict and find 10 highest words
  final_dict = {}
  most_common_words = sorted(valid_dict, key=valid_dict.get, reverse=True)
  if len(most_common_words) < number_of_words:
    number_of_words = len(most_common_words)
  for i in range(number_of_words):
    final_dict[most_common_words[i]] = valid_dict[most_common_words[i]]
  return final_dict

def q2(filename, minWordLengthToConsider = 1):
  #cleaning up dataset and making unique lists
  text = open(filename, encoding="utf-8").read()
  messages = text.splitlines()
  ham_list = []
  spam_list = []
  for message in messages:
    message = message.strip(".!?;:@#$%^&*()- ")
    message = message.lower()
    l = message.split()
    if l[0] == "ham":
      ham_list.append(l[1:])
    if l[0] == "spam":
      spam_list.append(l[1:])

  #number of ham/spam messages
  ham_list_length = len(ham_list)
  spam_list_length = len(spam_list)
  #number of words in ham/spam
  ham_word_length = 0
  spam_word_length = 0
  for msg in ham_list:
    ham_word_length += len(msg)
  for msg in spam_list:
    spam_word_length += len(msg)
  #unique words in ham/spam
  ham_unique = count_unique_words(ham_list)
  spam_unique = count_unique_words(spam_list)
  ham_unique_length = len(ham_unique)
  spam_unique_length = len(spam_unique)
  #Find ten most common and their percentages
  ham_ten_most_common = sort_dict(ham_unique, minWordLengthToConsider, 10)
  spam_ten_most_common = sort_dict(spam_unique, minWordLengthToConsider, 10)
  ham_final = {}
  spam_final = {}
  for k,v in ham_ten_most_common.items():
    ham_final[k] = (v, v / ham_word_length) 
  for k,v in spam_ten_most_common.items():
    spam_final[k] = (v, v / spam_word_length)
  #average lengths of ham messages and spam messages (total words / number of sentences)
  ham_average = ham_word_length / ham_list_length
  spam_average = spam_word_length / spam_list_length

  #print data
  print("\n******************\n")
  print(f"There were {ham_list_length} ham messages.")
  print(f"There were a total of {ham_word_length} words in ham messages.")
  print(f"There were a total of {ham_unique_length} unique words in ham messages.")
  print(f"The ten most common words (of the length requested), the number they occurred, and their frequencies in ham messages are:")
  for k, v in ham_final.items():
    print(f"{k}: {v[0]} times, {round(v[1]*100, 2)}% frequency.")
  print("\n******************\n")
  #spam data!
  print(f"There were {spam_list_length} spam messages.")
  print(f"There were a total of {spam_word_length} words in spam messages.")
  print(f"There were a total of {spam_unique_length} unique words in spam messages.")
  print(f"The ten most common words (of the length requested), the number they occurred, and their frequencies in spam messages are:")
  for k, v in spam_final.items():
    print(f"{k}: {v[0]} times, {round(v[1]*100, 2)}% frequency.")
  print("\n******************\n")

#q2("SMScollection.txt", 10)