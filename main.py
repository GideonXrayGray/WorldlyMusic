import sys
from googletrans import Translator
import random

langlist = ("af","sq","ar","be","bg","ca","hr","cs","da","nl","en","eo","et","tl","fi","fr","gl","de","el","iw","hi","hu","is","id","ga","it","ja","ko","la","lv","lt","mk","ms","mt","no","fa","pl","pt","ro","ru","sr","sk","sl","es","sw","sv","th","tr","uk","vi","cy","yi")
# print("Original Statment: " + statement)

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'ar': 'arabic',
    'be': 'belarusian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'zh-CN': 'chinese_simplified',
    'zh-TW': 'chinese_traditional',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'gl': 'galician',
    'de': 'german',
    'el': 'greek',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hu': 'hungarian',
    'is': 'icelandic',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'ko': 'korean',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'mk': 'macedonian',
    'ms': 'malay',
    'mt': 'maltese',
    'no': 'norwegian',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'ro': 'romanian',
    'ru': 'russian',
    'sr': 'serbian',
    'sk': 'slovak',
    'sl': 'slovenian',
    'es': 'spanish',
    'sw': 'swahili',
    'sv': 'swedish',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'yi': 'yiddish',
  }

def langaugeGen(number):
    rlang = []
    while len(rlang) < number:
        choice = random.choice(langlist)
        rlang.append(choice)
    return rlang

def translaterMessage(statement,numoflang):
    translate = Translator()
    original = statement

    #Loops though ever lang in langaugeGen, translates, and prints result
    for key in langaugeGen(numoflang):
        tstatment = translate.translate(dest=key, text=statement)
        print(f"{LANGUAGES[tstatment.src]:<10} ---> {LANGUAGES[tstatment.dest]:<20}  {translate.translate(tstatment.text).text}")
        statement = tstatment.text
    print(f"\r\nOriginal: {original:<20}")
    print(f" {translate.translate(statement).text}")
    start()

def start():
    translaterMessage(input("Input a statement or lyric: "),int(input("Enter the number of translation loops: ")))

start()