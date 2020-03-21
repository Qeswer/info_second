import  random #импортируем библиотеку 
f = open("qeswer.txt","wt")  #открываем файл, символ "W" означает редактирование, если файл не существует, то он будет 
numbers = [ random.randint(-10,10) for i in range(int(input("введите N ")))]#создаем список из случайных чисел
print(numbers)
for i in range(len(numbers)):
    f.write(str(numbers[i]) + str("; ")) #записываем числа в файл
k = 0
minus = [] #создаем список
for i in numbers: #пробегаемся по списку чисел
    for j in numbers: #пробегаемся по списку
        if i!=0 and j!=0 and i==-j: #задаем условие, находим противоположное
            k+=1
            minus.append(i); minus.append(j) #добавляем в новый список числа
            numbers.remove(i); numbers.remove(j) #удаляем со старого списка противоположные числа
            break #завершаем
for i in range(0,len(minus),2): #пробегаемся по четным элементам в новом списке
    print("числа:",minus[i],":",minus[i+1]) #вывод на экран
    f.write(str("\n"))
    f.write(str("числа: "))
    f.write(str(minus[i]))
    f.write(str(":"))
    f.write(str(minus[i+1])) #записываем в файл
print("кол-во пар противопол-х чисел:", k) 
f.write(str("\n"))
f.write(str("кол-во пар противопол-х чисел:"))
f.write(str(k))
k = int(input())
f.close() 
