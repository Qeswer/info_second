import re
def first(text):
    print("дан текст: ", text)
    reg = re.compile('[^a-zA-Z ]')
    text1 = reg.sub('', text)
    print(text1)
    Broke=text1.split()
    k=len(Broke)
    list_three=[]
    for i in range(k):
        if len(Broke[i])==3:
            list_three.append(Broke[i])
    print("слова содержащие 3 буквы: "," ".join(list_three))
first(input(str("введите текст: ")))

def second(text_a):
    print("дан текст: ", text_a)
    reg = re.compile('[^a-zA-Z ]')
    text_a = reg.sub('', text_a)
    words = text_a.split()
    new = []
    for i in range(len(words)):
        word=words[i][::-1]
        new.append(word)
    new.append(str('.'))
    print("ответ:",'\n', ' '.join(new))
second(str(input("введите зашифрованный текст: ")))
input()

https://sun9-52.userapi.com/c857420/v857420639/194e26/alcimkjlyjU.jpg
