import  random
f = open("qeswer(1).txt","w+") #Открываем файл, если не существует, создаем
f1 = open("qeswer(2).txt","w+")
numbers = [ random.randint(-10,10) for i in range(int(input("введите N ")))]#рандомный список
k = int(input("введите кратное число k: ")) #вводим любое число
print(numbers)
for i in numbers:
    f.write(str(i) + str(";")) #записываем в файл числа
new = [] #создаем список
for i in numbers: #пробегаемся по списку чисел
    if i%k == 0: #условие кратности
        new.append(i) #добавляем в новый список кратные числа
for i in new: #пробегаемся по новому списку чисел
    numbers.remove(i) #удаляем кратные числа со старого списка
for i in numbers: #пробегаемся по списку, где удалены числа 
    f1.write(str(i) + str(";")) #записываем в новый файл оставшиеся числа
f1.write(str("\nудалены элементы: "))
for i in new:
    f1.write(str(i) + str(";"))
f.close() #закрытие файла
f1.close()
