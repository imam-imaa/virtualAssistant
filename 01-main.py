import speech_recognition as sr
import webbrowser 
import pyttsx3
import musicLibrary
# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text) 
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]  
        webbrowser.open(link)  

    else:
        # let OpenAI handle the request
        pass         
    

   

if __name__ == "__main__":
    speak("Initializing imam ....")
    while True:
            # listen  for the wake word "imam"
            # obtain audio from the microphone
        
            r = sr.Recognizer()
          
            print("recognizing...")         
            
            try:
                 with sr. Microphone() as source:
                    print("Listening....")  
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                 word = r.recognize_google(audio)
                 if (word.lower() == "imam"):
                      speak("YA")
                      # listen for command
                      with sr. Microphone() as source:
                        print("imam Active....")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)    

           
            except Exception as e:
                print("Error; {0}".format(e))
        
    
    
    
    
    
