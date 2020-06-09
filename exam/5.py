def getString(string):
    print(string)
    print(len(string))
    word = []
    print(string[2])
    for i in string:
        if i == str(' '):
            break
        word.append(str(i))
    print(len(word))
    for j in range(len(word)):
        list(string)[j] = word[len(word)]
    print(word)
    print(string)
getString(str("Hello world"))