import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)
    voice = r.recognize_google(audio)
    
    text = open("text.txt", "w")
    text.write(voice)

    print(voice)
