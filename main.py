import sys
from googletrans import Translator
import random


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

def langaugeGen():
    lang_list = list(LANGUAGES.keys())
    return random.choice(lang_list)

def translaterMessage(statement,numoflang):
    translate = Translator()
    original = statement
    count = 0

    while count != numoflang:
        try:
            tstatment = translate.translate(dest=langaugeGen(), text=statement)
            print(f"{LANGUAGES[tstatment.src]:<10} ---> {LANGUAGES[tstatment.dest]:<20}  {translate.translate(tstatment.text).text:<60} {tstatment.text}")
            statement = tstatment.text
            count = count + 1
        except:
            print("")
       
    print(f"\r\nOriginal: {original:<20}")
    print(f"Translated: {translate.translate(statement).text}")
    start()

def start():
    translaterMessage(input("Input a statement or lyric: "),int(input("Enter the number of translation loops: ")))

start()
