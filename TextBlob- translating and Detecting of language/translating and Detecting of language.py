# - *- coding: utf- 8 - *-
from textblob import TextBlob
word1=TextBlob("thank you everyone for coming")
lang=word1.detect_language()
z=word1.translate(from_lang='en', to ='hi')
print(lang)
print(z)
