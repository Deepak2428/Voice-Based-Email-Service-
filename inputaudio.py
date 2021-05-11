def takeaudio(text):
    import speech_recognition 
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        
        if(text=="normal"):
            input=r.record(source, duration=4)
        elif(text=="subject"):
            input=r.record(source, duration=7)
        else:
            input=r.record(source, duration=20)
        
        input=r.recognize_google(input)
    return (input)