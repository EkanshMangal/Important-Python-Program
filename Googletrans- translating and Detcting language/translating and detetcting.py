# 1) Translate
from googletrans import Translator
trans = Translator()
# to detect language
txt="Hello How are you"
dial_lang=trans.detect(txt).lang
print(dial_lang)
t = trans.translate(
    txt, src= dial_lang, dest='hi'
)
print(f'Source: {t.src}')
print(f'Destination: {t.dest}')
print(f'{t.origin} -> {t.text}')
# print()
# # # 2) List supported languages
# # from googletrans import LANGUAGES

# # for lang in LANGUAGES:
# #     print(f'{lang} - {LANGUAGES[lang]}')
# # print()

# # # 3) List possible mistakes and translations 
# pm = t.extra_data['possible-mistakes']
# pt = t.extra_data['possible-translations']

# print(f'Possible Mistakes: {pm}')
# print(f'Possible Translations: {pt}')