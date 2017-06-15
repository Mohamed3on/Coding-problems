def plusone(digits):
    num = ""
    for d in digits:
        num += str(d)
    incremented = str(int(num) + 1)
    incrementedAsList = []
    for i in incremented:
        incrementedAsList.append(int(i))
    return incrementedAsList


print(plusone([2, 3, 1, 5, 2, 1, 4, 9]))
