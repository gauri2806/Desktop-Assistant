# from urllib.parse import _ResultMixinBase
import pandas
import ntpath
import pyttsx3
from pywhatkit.mail import send_mail
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
  engine.say(audio)
  print(audio)
  engine.runAndWait()

#voice to text
def takecommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold=1
    audio = r.listen(source,timeout=1,phrase_time_limit=5)

  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"User said: {query}")

  except Exception as e:
    speak("Say that again please...")
    return "none"
  return query

# to wish
def wish():
  hour= int(datetime.datetime.now().hour)
  if hour>=0 and hour<=12:
    speak("Good Morning mam")
  elif hour>12 and hour<18:
    speak("Good Afternoon mam")
  else:
    speak("Good Evening mam")
  speak("I am Alexa. Please tell me how can I help you.")

#to send email
# def sendEmail(to, content):
#   server=smtplib.SMTP('smtp.gmail.com', 587)
#   server.ehlo()
#   server.starttls()
#   server.login('gaurikatti2806@gmail.com', 'password')
#   server.sendmail('gaurikatti2806@gmail.com',to,content)


if __name__ == "__main__":
  wish()
  while True:
  # if 1:
    query=takecommand().lower()
    if "open notepad" in query:
      npath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\\notepad.lnk"
      os.startfile(os.path.normpath(npath))

    elif "open cmd" in query:
      os.system("start cmd")

    elif "open camera" in query:
      cap=cv2.VideoCapture(0)
      while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k= cv2.waitKey(50)
        if k==27:
          break;
      cap.release()
      cv2.destroyAllWindows()

    elif "ip address" in query:
      ip=get('https://api.ipify.org').text
      speak(f"Your ip address is {ip}")

    elif "wikipedia" in query:
      speak("Searching wikipedia...")
      query=query.replace("wikipedia","")
      results=wikipedia.summary(query, sentences=2)
      speak("According to wikipedia, ")
      speak(results)

    elif "open youtube" in query:
      webbrowser.open("www.youtube.com")

    elif "open facebook" in query:
      webbrowser.open("www.facebook.com")

    elif "open linkedin" in query:
      webbrowser.open("www.linkedin.com")

    elif "open instagram" in query:
      webbrowser.open("www.instagram.com")

    elif "open whatsapp" in query:
      webbrowser.open("https://web.whatsapp.com/")

    elif "open discord" in query:
      webbrowser.open("https://discord.com/channels/@me")

    elif "open stack overlow" in query:
      webbrowser.open("www.stackoverflow.com")

    elif "open codechef" in query:
      webbrowser.open("https://www.codechef.com/users/gaur_i28")

    elif "open code forces" in query:
      webbrowser.open("https://codeforces.com/profile/gauri_28")

    elif "open leet code" in query:
      webbrowser.open("https://leetcode.com/gaur_i28/")

    elif "open geeks for geeks" in query:
      webbrowser.open("https://auth.geeksforgeeks.org/user/gaurikatti2806")

    elif "open github" in query:
      webbrowser.open("https://github.com/gauri2806")

    elif "open google" in query:
      speak("Mam, What should I search on google?")
      cm=takecommand().lower()
      webbrowser.open(f"{cm}")

    elif "send message" in query:
      kit.sendwhatmsg("+918080324256","this is gauri katti",1,8)

    elif "play songs on youtube" in query:
      kit.playonyt("Shiv Tandav")

    # elif "email to goury" or "email to gowri" or "email to gowry" or "email to gouri" in query:
    #   try:
    #     speak("What should I say?")
    #     content=takecommand().lower()
    #     to="gauikatti2806@gmail.com"
    #     sendEmail(to,content)
    #     speak("Email has been sent to goury")
      
    #   except Exception as e:
    #     print(e)
    #     speak("Sorry mam, I am not able to send this mail to gauri")

    elif "no thanks" or "shut up" in query:
      speak("Thanks for using me mam, have a good day.")
      sys.exit()

    speak("Mam, do you have any other work?")

     