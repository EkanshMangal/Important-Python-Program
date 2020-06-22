# pip install pydub

import pydub
sound = pydub.AudioSegment.from_mp3("F:\mnf\en21.mp3")
sound.export("F:\mnf\en21.wav", format="wav")