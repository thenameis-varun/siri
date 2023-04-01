import speech_recognition as sr         #spoken language to text formate

import pyttsx3                          #for text to speech

import pywhatkit                        #for Sending emails and WhatsApp messages
                                        # Sending emails and WhatsApp messages
                                        # Converting text to hand-written format
                                        # Generating QR codes
                                        # Searching on Google and YouTube
                                        # Playing a YouTube video
                                        # Generating text-to-speech output
                                        # Extracting text from images
                                        # Checking the weather of a location

import datetime                         #for date,time,day

import pyjokes                          #humorous jokes for programmers

import wikipedia                        #third-party library, API for accessing Wikipedia articles

import pyaudio                          #work with audio in Python.

import os                               #Creating and deleting files and directories
                                        #renaming files and directories
                                        #Getting information about the system environment
                                        # Joining and splitting file paths
                                        # Setting file permissions and ownership

import webbrowser                       #built-in module no need to install
                                        


from geopy.geocoders import Nominatim


listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()                 # say() makes speech from text . runAndWait() plays that speech in output

wish = int(datetime.datetime.now().strftime("%H"))
if 3<wish<12:
    talk('good morning sir    how can i help you ')
elif 12<wish<16:
    talk('good afternoon sir    how may i help you ')  
else:
    talk('good evening sir    how shall i help you')


def take_command():
    try:
        with sr.Microphone() as source:
            
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("▶️   "+command)
            
            if "what is your name" in command or "what's your name" in command:  
                print ('\nsiri ‼️')
                talk('you can call me siri')
                run_siri()
            elif 'siri' in command:
                command = command.replace('siri', '')
                return command
            else:
                print(" ✌️ ")
                talk("please call me by my name")
                run_siri()
    except:
        pass
    


def run_siri():
    command = take_command()
    
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song) 
      
                                   

    elif ('time' in command) or ('date' in command) or ('day' in command) :
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        day =datetime.date.today().strftime('%A')
        print(day)
        date = datetime.date.today()
        print(date)
        talk('Current time is ' + time+ ' day is  '+ day+ ' and its')
        talk(date)


    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)



    elif 'what is' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing, 3)
        print(info)
        talk(info)
    

    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'location' in command:
        import geo
        location=geo.location()
        print(location)
        talk(location)
        

    elif 'whatsapp' in command:
        talk('enter the following detail')
        phone_number=input("enter the phone number\n")
        message=input("enter the message to be sent\n")
        hour=int(input("enter hour\n"))
        minute=int(input("enter minute\n"))
        pywhatkit.sendwhatmsg(phone_number, message,hour,minute) 
        talk('message sent')

    elif 'weather' in command:
        # talk(' enter your location ')
        # location = input("Enter your location: ")

        # # Construct the search query
        # query = f"{location} weather"

        # # Search for the weather using Google
        # pywhatkit.search(query)
        import reading_webpage
        weather_info=reading_webpage.read()
        print(weather_info)
        talk(weather_info)

    elif 'open code' in command:
        path=r'C:\Users\91789\AppData\Local\Programs\Microsoft VS Code\code.exe'
        talk('opening new code')
        os.startfile(path)
    
    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in command:
        webbrowser.open("stackoverflow.com")   
    

    else:
        talk('u can come again.')


while True:
    run_siri()

