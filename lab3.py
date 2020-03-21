import re 
def first(text): #создаем функцию для первого задания
    print("дан текст: ", text) 
    reg = re.compile('[^а-яА-Я ][^a-zA-Z ]')
    text1 = reg.sub('', text)
    #text.replace('.')
    print(text1)
    Broke=text1.split() #разбиваем текст на список слов
    k=len(Broke) #длина списка
    list_three=[] # создаем список
    for i in range(k):
        if len(Broke[i])==3: 
            list_three.append(Broke[i]) # добавляем в новый список все слова с 3-мя буквами
    print("слова содержащие 3 буквы: "," ".join(list_three)) #выводим на экран
first(input(str("введите текст: "))) #обращаемся к первому заданию

def second(text_a): #функция для второго задания
    print("дан текст: ", text_a)
    reg = re.compile('[^a-zA-Z ][^а-яА-Я ]')
    text_a = reg.sub('', text_a)
    words = text_a.split()#разбиваем предложение на список слов
    new = [] #создаем новый список
    for i in range(len(words)): #цикл до длины списка
        word=words[i][::-1] #переворачиваем слово
        new.append(word) #перевернутое слово добавляем в новый список
    new.append(str('.')) #добавляем удаленный символ
    print("ответ:",'\n', ' '.join(new)) # вывод на экран
second(str(input("введите зашифрованный текст: "))) #обращаемся ко второй функции
input()


https://sun9-52.userapi.com/c857420/v857420639/194e26/alcimkjlyjU.jpg
