import speech_recognition as sr

r = sr.Recognizer()

while True:
    
    try:
        with sr.Microphone() as source:
            print("Speak...")
            audio = r.listen(source)
            voice = r.recognize_google(audio, language="tr-TR")
            
            text = open("text.txt", "w")
            text.write(voice+"\n")

            print(voice)
        
    except:
        raise ValueError("Time Out!")
