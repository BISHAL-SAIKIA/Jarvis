import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    text = str(text)
    command=pyttsx3.init('sapi5')
    voices=command.getProperty('voices')
    command.setProperty('voice',voices[1].id)
    command.setProperty('rate',174)
    eel.DisplayMessage(text)
    command.say(text)
    command.runAndWait()


def takecommand():
 
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 15, 10)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)

    except Exception as e:
        return ""
    
    return query.lower()

# text=takecommand()
# speak(text)

@eel.expose
def allCommands(message=1):
    if message==1:
        query=takecommand()
        print(query)
    else:
        query=message
        
    try:
        if "open" in query:
            from features import openCommand
            openCommand(query)
            
        elif "on youtube" in query:
            from features import PlayYoutube
            PlayYoutube(query)
        else:
            from features import chatBot
            chatBot(query)
    except:
        print("error")
    
    eel.ShowHood()
    