def q3(listOfStrings1, listOfStrings2):
    index_list = []
    max_length = 0
    if len(listOfStrings1) < len(listOfStrings2):
        max_length = len(listOfStrings1)
    else:
        max_length = len(listOfStrings2)
    for i in range(max_length):
        first_string = listOfStrings1[i]
        second_string = listOfStrings2[i]
        if len(first_string) == len(second_string):
            index_list.append(i)
    return index_list