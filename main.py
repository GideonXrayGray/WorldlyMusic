import sys
from googletrans import Translator
import random

statement ="London Ontario is the better London."
translate = Translator()
langlist = ("af","sq","ar","be","bg","ca","zh-CN","zh-TW","hr","cs","da","nl","en","eo","et","tl","fi","fr","gl","de","el","iw","hi","hu","is","id","ga","it","ja","ko","la","lv","lt","mk","ms","mt","no","fa","pl","pt","ro","ru","sr","sk","sl","es","sw","sv","th","tr","uk","vi","cy","yi")
rlang = []
print("Original Statment: " + statement)

while len(rlang) < 3:
    choice = random.choice(langlist)
    rlang.append(choice)

for key in rlang:
    tstatment = translate.translate(dest=key, text=statement)
    statement = tstatment.text

print(translate.translate(statement).text)
print(rlang)
