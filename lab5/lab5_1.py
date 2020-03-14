a = open("qeswer.txt")
a1 = open("qeswer2.txt","wt")
word = str(input("введите слово: "))
for line in a:
    words = line.split()
    for i in words:
        if str(word)==str(i):
            a1.write(line)
a.close()
a1.close()