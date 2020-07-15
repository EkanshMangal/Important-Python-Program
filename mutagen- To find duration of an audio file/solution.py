# from mutagen.mp3 import MP3
# # function to convert the seconds into readable format
# def convert(seconds):
#     hours = seconds // 3600
#     seconds %= 3600
#     mins = seconds // 60
#     seconds %= 60
#     return hours, mins, seconds
# # Create an MP3 object
# # Specify the directory address to the mp3 file as a parameter
# audio = MP3("F:\Important Python Program\mutagen- To find duration of an audio file\itsamatch.mp3")
# # Contains all the metadata about the mp3 file
# audio_info = audio.info    
# length_in_secs = int(audio_info.length)
# hours, mins, seconds = convert(length_in_secs)
# print(length_in_secs)
# print("Hours:", hours)
# print("Minutes:", mins)
# print("Seconds:", seconds)

# import soundfile as sf
# f = sf.SoundFile('F:\Important Python Program\mutagen- To find duration of an audio file\Chakachak.mp3')
# print('samples = {}'.format(len(f)))
# print('sample rate = {}'.format(f.samplerate))
# print('seconds = {}'.format(len(f) / f.samplerate))

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