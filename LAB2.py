import random
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)
      print("After increments of size",sublistcount,"\nThe list is",alist)
      sublistcount = sublistcount // 2
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=currentvalue
alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
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
    print('___________________________\nдана матрица:')
    for i in range(x):
        for j in range(x):
            matrixList[i][j] = random.randint(1,10)
    for i in range(x):
        print(matrixList[i])
    print('_________________________\nответ:')
    for i in range(x):
        new(matrixList[i])
        '''
        summ = []
        def listsum(numList):
            theSum = 0
            for i in numList:
                theSum = theSum + i
            summ.append(theSum)
            print(summ)
        listsum(matrixList[i])
        '''
        print(matrixList[i])
second(int(input("введите размер матрицы ")))

