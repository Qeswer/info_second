import  random
f = open("qeswer(1).txt","w+")
f1 = open("qeswer(2).txt","w+")
numbers = [ random.randint(-10,10) for i in range(int(input("введите N ")))]
k = int(input("введите кратное число k: "))
print(numbers)
for i in numbers:
    f.write(str(i) + str(";"))
new = []
for i in numbers:
    if i%k == 0:
        new.append(i)
for i in new:
    numbers.remove(i)
for i in numbers:
    f1.write(str(i) + str(";"))
f1.write(str("\nудалены элементы: "))
for i in new:
    f1.write(str(i) + str(";"))
f.close()
f1.close()
