import random


def getNumbers(n):
    getTheNumbers = open("numbers.txt", "w+")
    list__1 = [random.randint(-10, 10) for i in range(3 * n)]
    for i in range(len(list__1)):
        getTheNumbers.write(str(list__1[i]) + str("; "))
        if i == len(list__1) - 1:
            getTheNumbers.write(str("\n"))
    firstNumbers = []
    thirdNumbers = []
    for i in range(n):
        firstNumbers.append(list__1[i])
    for j in range(n):
        thirdNumbers.append(list__1[len(list__1) - n + j])
        list__1[j] = thirdNumbers[j]
        list__1[len(list__1) - n + j] = firstNumbers[j]
    print(list__1)
    for i in range(len(list__1)):
        getTheNumbers.write(str(list__1[i]) + str("; "))


getNumbers(int(input("введите N ")))
