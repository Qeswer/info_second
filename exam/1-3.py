def getWordsByString(string):
    words = []; word = str(''); n = 0
    for i in string:
        if i != ' ' and i !=',' and i !='.' and i !='!' and i !='?' and i !=':' and i !='-' and i !='/':
            word += i
        if len(word) != 0 and i == ' ':
            words.append(word); word = ''
        elif i == string[len(string)-1] and n == len(string)-1 and len(word) != 0:
            words.append(word); word = ''
        n += 1
    return(words)

def getWordsBySymblos(words, startLen):
    startSymbols = []; needWords = []; testWords = []; wordsOut = []
    word = str('')
    for i in words: #получаем слова нужной длины
        if len(i) >= startLen:
            needWords.append(i)
    for j in needWords:
        for k in range(startLen):
           word += str(j[k])
        startSymbols.append(word)
        word = ''
    startSymbols = set(startSymbols)
    for l in startSymbols:
        for m in needWords:
            for n in range(startLen):
                word += str(m[n])
            if word == l:
                testWords.append(m)
            word = ''
        if len(testWords) > 1:
            for o in testWords:
                wordsOut.append(o)
        testWords = []
    return(wordsOut)

print(getWordsBySymblos(getWordsByString(str(" aajjjj,  , /   hello    hel  hell  hi-  i  aabbb aaccc aaggg  ccdt cccggee  home     jkgjhjhgg drtrry.        aaaassssss  ?  ")), 2))    

string = str("hello how are you what are you doing?")
list = getWordsByString(string)

def var2(list):
    releaseList = []; releaseString = str('')
    for i in range(len(list)):
        if i%2 == 0:
            releaseList.append(list[i])
    for j in releaseList:
        releaseString += str(j) + str(" ")
    return(releaseString)

def var3(list):
    releaseList = []; releaseString = str('')
    for i in range(1, len(list)-1):
        releaseList.append(list[i])
    for j in releaseList:
        releaseString += str(j) + str(" ")
    return(releaseString)
print(var2(list))
print(var3(list))

