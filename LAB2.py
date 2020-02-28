import random
def shellSort(alist):
    shag = len(alist)//2
    while shag > 0:
      for startposition in range(shag):
        gapInsertionSort(alist,startposition,shag)
      print("шаг",shag,"\nсписок",alist)
      shag = shag // 2
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        element = alist[i]
        position = i
        while position>=gap and alist[position-gap]>element:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=element
alist = random.sample(range(10),9)
print("задание первое\nдан массив:",alist)
shellSort(alist)
print("ответ:",alist)
def new(chisla):
    dlina = len(chisla)//2
    while dlina > 0:
        for startp in range(dlina):
            newShell(chisla,startp,dlina)
            dlina=dlina//2
def newShell(chisla, start,gap):
    for i in range(start + gap,len(chisla),gap):
        k = chisla[i]
        position = i
        while position>=gap and chisla[position-gap]>k:
            chisla[position] = chisla[position-gap]
            position =position - gap
        chisla[position]=k
def second(x):
    matrixList = [[0 for i in range(x)] for i in range(x)]
    print('задание второе:\n___________________________\nдана матрица:')
    for i in range(x):
        matrixList[i] = random.sample(range(10),x)
    for i in range(x):
        print(matrixList[i])
    print('_________________________\nответ:')
    for i in range(x):
        new(matrixList[i])
        print(matrixList[i])
second(int(input("введите размер матрицы ")))
https://sun9-69.userapi.com/c857420/v857420153/1941c2/dvoYHw7d98c.jpg
