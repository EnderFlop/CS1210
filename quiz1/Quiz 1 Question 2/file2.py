def q3(s, lowLetter, highLetter):
    smallest = None
    highest_index = None
    for index in range(len(s)):
        letter = s[index]
        if letter > lowLetter and letter < highLetter:
            if smallest == None or letter <= smallest:
                smallest = letter
                highest_index = index
    return smallest, highest_index