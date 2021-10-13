def q4(stringToProcess, translationDict):
    final_string = ""
    for i in range(0, len(stringToProcess), 2):
        multiplier = int(stringToProcess[i])
        letter = stringToProcess[i+1]
        if letter in translationDict:
            final_string += multiplier * translationDict[letter]
        else:
            final_string += multiplier * "-"
    return final_string