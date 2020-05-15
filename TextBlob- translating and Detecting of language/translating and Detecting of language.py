# - *- coding: utf- 8 - *-
from textblob import TextBlob
word1=TextBlob("thank you for using this")
lang=word1.detect_language()
z=word1.translate(from_lang='en', to ='hi')
print(lang)
print(z)

# first install textblob library for using this
# pip install textblob
# encoding format should be exact and placed at beginning of file