import  random
f = open("qeswer.txt","wt")
numbers = [ random.randint(-10,10) for i in range(int(input("введите N ")))]
print(numbers)
for i in range(len(numbers)):
    f.write(str(numbers[i]) + str("; "))
k = 0
minus = []
for i in numbers:
    for j in numbers:
        if i!=0 and j!=0 and i==-j:
            k+=1
            minus.append(i); minus.append(j) 
            numbers.remove(i); numbers.remove(j) 
            break
for i in range(0,len(minus),2):
    print("числа:",minus[i],":",minus[i+1])
    f.write(str("\n"))
    f.write(str("числа: "))
    f.write(str(minus[i]))
    f.write(str(":"))
    f.write(str(minus[i+1]))
print("кол-во пар противопол-х чисел:", k)
f.write(str("\n"))
f.write(str("кол-во пар противопол-х чисел:"))
f.write(str(k))
f.close()
