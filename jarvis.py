import pyttsx3
import datetime
import speech_recognition as sr




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning Ankush sir...')

    elif hour>=12 and hour<18:
         speak('good afternoon ankush sir....')

    else:
                  speak('good Evining ankush sir....')

    speak('please tell me sir, how can i help you.. just order me what ever you want i will do for you')
    


# def takeComand():

    
#     # it takes microphoneinput from desktop and give a output    
#     r=sr.Recognizer() 
#     with sr.Microphone() as source:
#         print("Listing.........")
#         r.pause_threshold = 1

#         audio= r.listen(source)

#     try:
#         print("Recogning.....") 
#         query=r.recognize_google(audio,language='en-in')
#         print(f"user said:{query}/n ")   

#     except Exception as e:
#         print(e)

#         print("say it again sir.. i could not here it properly..")    
#         return 'None'
#     return query    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    takeCommand()
    
