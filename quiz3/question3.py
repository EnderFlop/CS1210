def q3(item):
    if type(item) == list:
        score = 1
        for i in item:
            score += q3(i)
        return score
    elif type(item) == int:
        return item
    elif type(item) == str:
        return len(item)
    else:
        return 0

#print(q3([3]))
#print(q3([3, "five", False, [10]]))
#print(q3([3, [6, [10]]]))