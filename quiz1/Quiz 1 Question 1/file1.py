def q2(s, n):
    new_str = ""
    for index in range(len(s)):
        letter = s[index]
        if index % n != 0:
            new_str += letter
    print(new_str)
    return new_str

q2("aba", 3)