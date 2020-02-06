# info_second
'''
def first(x):
    chisla = list(map(int,input("введите числа ").split()))
    mass = chisla
    maxA = chisla[0]; sumA = 0; maxID = 0
    n = len(chisla)
    print(chisla)
    for i in range(1, n):
        if maxA >= chisla[i]:
            maxA = chisla[i]
            maxID = i
        sumA += chisla[i]
    print("Максимальный элемент: ", minA)
    print("ID элемента: ", minID)
    sumA = sumA/len(chisla)
    print("Среднее арифметическое все чисел:", sumA)
    chisla[minID] = round(sumA,0)
    chisla[minID] = int(chisla[minID])
    print('\nответ',chisla)
second(2)
'''
'''
def second(x):
    chisla = list(map(int,input("введите координаты ").split()))
    print(chisla)
    n = len(chisla)
    rad=[]
    MaxR=0; MaxID=0; 
    for i in range(0,n,2):
        X=chisla[i]
        y=chisla[i+1]
        r = float((X**2+y**2)**0.5)
        print(r)
        rad.append(r)
    print(rad)
    R=max(rad)
    print('максимальный радиус =',R)
second(2)
'''
def third(x):
    n = 1
    matrixList = [[0 for i in range(x)] for i in range(x)]
    for i in range(x):
        for j in range(x):
            matrixList[i][j] = n
            n += 1
    for i in range(x):
        if i%2!=0:
            matrixList[i].reverse()
            print(matrixList[i])
        print(matrixList[i+1])

third(int(input('введите размер матрицы ')))
    
