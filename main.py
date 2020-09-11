import pyttsx3
import datetime
import wikipedia
import speech_recognition as anishavoice
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour in range(4,12):
        speak("Good Morning Boss")
    elif hour in range(12,17):
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")
    speak('Please tell me  how may i help you')

def sendemail(to,content):
    server = smtplib.SMTP("smntp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("kishanmohanty2105@gmail.com","Kish@n21")
    server.sendmail("kishanmohanty2105@gmail.com",to,content)
    server.close()


def takeCommand():
    r = anishavoice.Recognizer()
    with anishavoice.Microphone() as myvoice:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 3830.7393000785655
        audio = r.listen(myvoice)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open edyoda" in query:
            webbrowser.open("classroom.edyoda.com")

        elif "open hack" in query:
            webbrowser.open("hackerearth.com")

        elif "whatsapp" in query:
            webbrowser.open("web.whatsapp.com")

        elif "hello" in query:
            speak("hello rashmi rani nayak")
            speak("hello rama monkey")
            speak("hello biswajit ")

        elif "play music" in query:
            music_dir = "D:\\music"
            songs= os.listdir(music_dir)
            i=random.randint(0,10)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "time" in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss, the time is {Time}")

        elif "name" in query:
            speak("My name is Anisha")

        elif "code" in query:
            path ="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin"
            os.startfile(path)

        elif "album" in query:
            path="C:\\Users\\ADMIN\\Pictures\\WALLPAPER"
            os.startfile(path)

        elif "email to kishan " in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "kishanmohanty95@gmail.com"
                sendEmail(to,content)
                speak("boss task completed!! Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry boss . i am not able to send this email at this moment")

        elif "close" in query:
            speak("Bye boss")
            speak("Take care")
            quit()



