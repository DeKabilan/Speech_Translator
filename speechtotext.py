import speech_recognition as sr


voice = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Now")
    audio = voice.listen(source)
    gets = voice.recognize_google(audio)
print(gets)