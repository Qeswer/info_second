def first(chisla):
    maxA = chisla[0]; maxID = 0
    n = len(chisla)
    print(chisla)
    for i in range(1, n):
        if maxA < chisla[i]:
            maxA = chisla[i]
            maxID = i
    print("максимальный элемент: ", maxA)
    print("ID элемента: ", maxID)
    chisla[maxID] = 0
    print('\nответ',chisla)
first(list(map(int,input("введите числа ").split())))
def second(chisla):
    print(chisla)
    n = len(chisla)
    rad=[]
    maxR=0; maxID=0; 
    for i in range(0,n,2):
        X=chisla[i]
        y=chisla[i+1]
        r =round((X**2+y**2)**0.5, 2)
        rad.append(r)
    print(rad)
    k = len(rad)
    for i in range(0,k):
        if maxR <= rad[i]:
            maxR = rad[i]
            maxID = i
    print('максимальный радиус =', (maxR))
second(list(map(int, input("введите координаты ").split())))
def third(x):
    n = 1
    matrixList = [[0 for i in range(x)] for i in range(x)]
    print(matrixList)
    for i in range(x):
        for j in range(x):
            matrixList[i][j] = n
            n += 1
    for i in range(x):
        if i%2!=0:
            matrixList[i].reverse()
            print(matrixList[i])
        else:
            print(matrixList[i])
third(int(input('введите размер матрицы ')))
    
