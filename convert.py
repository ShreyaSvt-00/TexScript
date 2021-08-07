# import speech_recognition as sr
# import moviepy.editor as mp
# import sys

# clip = mp.VideoFileClip(r"aaadd.mp4")
# clip.audio.write_audiofile(r"converted.wav")
# r = sr.Recognizer()
# audio = sr.AudioFile("converted.wav")
# with audio as source:
#   audio_file = r.record(source)
# result = r.recognize_google(audio_file)


# # exporting the result
# with open('recognized.txt',mode ='w') as file:
#    file.write("Recognized Speech:")
#    file.write("\n")
#    file.write(result)
#    f = open('example.txt', 'r')
#    file_contents = f.read()
#    print (file_contents)
#    f.close()
# sys.stdout.flush()



import speech_recognition as sr
import moviepy.editor as me
import sys

VIDEO_FILE = sys.argv[1]
OUTPUT_AUDIO_FILE = "converted.wav"
OUTPUT_TEXT_FILE = "data/recognized.txt"
try:
    video_clip = me.VideoFileClip(r"{}".format(VIDEO_FILE))
    video_clip.audio.write_audiofile(r"{}".format(OUTPUT_AUDIO_FILE))
    recognizer =  sr.Recognizer()
    audio_clip = sr.AudioFile("{}".format(OUTPUT_AUDIO_FILE))
    with audio_clip as source:
        audio_file = recognizer.record(source)
    print("Please wait ...")
    result = recognizer.recognize_google(audio_file)
    with open(OUTPUT_TEXT_FILE, 'w') as file:
        file.write(result)
        print("Speech to text conversion successfull.")
except Exception as e:
    print("Attempt failed -- ", e)
