
import pyttsx3
#To run Jarvis
import multiprocessing

def MySpeakFunction(text):
    command=pyttsx3.init('sapi5')
    voices=command.getProperty('voices')
    command.setProperty('voice',voices[1].id)
    command.setProperty('rate',174)
    command.say(text)
    command.runAndWait()
    
    
    
def startJarvis():
    print("process 1 is running")
    from main import start
    start()

#To run hotword
def listenHotword():
    print("process 2 is running")
    from features import hotword
    hotword()
    
    
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        p2.start()
        #join mtlb terminate karna jab cross button dabaye
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")