import sys
from googletrans import Translator
import random

# statement =" I am a man of my word"

langlist = ("af","sq","ar","be","bg","ca","zh-CN","zh-TW","hr","cs","da","nl","en","eo","et","tl","fi","fr","gl","de","el","iw","hi","hu","is","id","ga","it","ja","ko","la","lv","lt","mk","ms","mt","no","fa","pl","pt","ro","ru","sr","sk","sl","es","sw","sv","th","tr","uk","vi","cy","yi")
# print("Original Statment: " + statement)


def langaugeGen(number):
    rlang = []
    while len(rlang) < number:
        choice = random.choice(langlist)
        rlang.append(choice)
    return rlang

def translaterMessage(statement="Hello World",numoflang=3):
    translate = Translator()
    print("Original: " + statement)
    for key in langaugeGen(numoflang):
        tstatment = translate.translate(dest=key, text=statement)
        print(tstatment.src + "-->" + tstatment.dest)
        statement = tstatment.text
    print("Results: " + translate.translate(statement).text)


translaterMessage(input("Input a statement: "),int(input("Enter the number of translations: ")))
