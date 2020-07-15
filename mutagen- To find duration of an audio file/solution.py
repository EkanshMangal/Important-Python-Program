# To use this, use pip install mutagen

from mutagen.mp3 import MP3
# function to convert the seconds into readable format
# Specify the directory address to the mp3 file as a parameter
audio = MP3("fileName.mp3")
# Contains all the metadata about the mp3 file
audio_info = audio.info    
seconds = int(audio_info.length)
hours = seconds // 3600
seconds %= 3600
mins = seconds // 60
seconds %= 60
print("Hours:", hours)
print("Minutes:", mins)
print("Seconds:", seconds)