#pip install pyttsx3
from win10toast import ToastNotifier
from datetime import datetime
from threading import Timer
toaster=ToastNotifier()
x=datetime.today()
#messages
pybotinit="L'assistant est initialisé"
m11h55="Il est 11h55 ! L'atelier jeux vidéos va se terminer dans 5 minutes."
m12h="Il est midi ! L'atelier jeux vidéos est terminé."
m14h="Il est 14h ! L'atelier multimédia va commencer."
m15h="Il est 15h ! L'atelier multimédia est terminé."
m15h55="Il est 15h55 ! La séance se terminera dans 5 minutes."
m16h="Il est 16h ! La séance de 15h est terminée. Merci de bien vouloir fermer votre session."
m16h55="Il est 16h55 ! La séance se terminera dans 5 minutes."
m17h="Il est 17h ! La séance de 16h est terminée. Merci de bien vouloir fermer votre session."
m17h30="La Médiathèque fermera ses portes dans 30 minutes !"
m17h45="La Médiathèque fermera ses portes dans 15 minutes !"
m17h55="La Médiathèque va fermer ses portes dans 5 minutes !"
m17h59="La Médiathèque sera fermée dans 1 minute ! Merci de bien vouloir fermer votre session."
#voice rate setting
rate=160

toaster.show_toast("Pybot Notification","L'assistant est initialisé",threaded=True,icon_path="icon.ico")
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",rate)
engine.say(pybotinit)
engine.runAndWait()
engine.stop()

#14h
y14h=x.replace(day=x.day+1, hour=14, minute=0, second=0, microsecond=0)
delta_t14h=y14h-x
secs14h=delta_t14h.seconds+1
def speak_14h():
  print(m14h)
  toaster.show_toast("Pybot Notification","Il est 14h",threaded=True,icon_path="icon.ico")
  import pyttsx3
  engine = pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m14h)
  engine.runAndWait()
  engine.stop()
t14h=Timer(secs14h,speak_14h)
t14h.start()

#15h
y15h=x.replace(day=x.day+1, hour=15, minute=0, second=0, microsecond=0)
delta_t15h=y15h-x
secs15h=delta_t15h.seconds+1
def speak_15h():
  print(m15h)
  toaster.show_toast("Pybot Notification","Il est 15h",threaded=True,icon_path="icon.ico")
  import pyttsx3
  engine = pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m15h)
  engine.runAndWait()
  engine.stop()
t15h=Timer(secs15h,speak_15h)
t15h.start()

#15h55
y15h55=x.replace(day=x.day+1, hour=15, minute=55, second=0, microsecond=0)
delta_t15h55=y15h55-x
secs15h55=delta_t15h55.seconds+1
def speak_15h55():
  print(m15h55)
  toaster.show_toast("Pybot Notification","Il est 15h55",threaded=True,icon_path="icon.ico")
  import pyttsx3
  engine = pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m15h55)
  engine.runAndWait()
  engine.stop()
t15h55=Timer(secs15h55,speak_15h55)
t15h55.start()

#16h
y16h=x.replace(day=x.day+1, hour=16, minute=0, second=0, microsecond=0)
delta_t16h=y16h-x
secs16h=delta_t16h.seconds+1
def speak_16h():
  print(m16h)
  toaster.show_toast("Pybot Notification","Il est 16h",threaded=True,icon_path="icon.ico")
  import pyttsx3
  engine = pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m16h)
  engine.runAndWait()
  engine.stop()
t16h=Timer(secs16h,speak_16h)
t16h.start()

#16h55
y16h55=x.replace(day=x.day+1, hour=16, minute=55, second=0, microsecond=0)
delta_t16h55=y16h55-x
secs16h55=delta_t16h55.seconds+1
def speak_16h55():
  print(m16h55)
  toaster.show_toast("Pybot Notification","Il est 16h55",threaded=True,icon_path="icon.ico")
  import pyttsx3
  engine = pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m116h55)
  engine.runAndWait()
  engine.stop()
t16h55=Timer(secs16h55,speak_16h55)
t16h55.start()

#17h
y17h=x.replace(day=x.day+1, hour=17, minute=0, second=0, microsecond=0)
delta_t17h=y17h-x
secs17h=delta_t17h.seconds+1
def speak_17h():
  print(m17h)
  toaster.show_toast("Pybot Notification","Il est 17h",threaded=True,icon_path="icon.ico")
  import pyttsx3
  engine = pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m17h)
  engine.runAndWait()
  engine.stop()
t17h=Timer(secs17h,speak_17h)
t17h.start()

#17h30
y17h30=x.replace(day=x.day+1, hour=17, minute=30, second=0, microsecond=0)
delta_t17h30=y17h30-x
secs17h30=delta_t17h30.seconds+1
def speak_17h30():
  print(m17h30)
  toaster.show_toast("Pybot Notification","Il est 17h30",threaded=True,icon_path="icon.ico")
  import pyttsx3
  engine = pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m17h30)
  engine.runAndWait()
  engine.stop()
t17h30=Timer(secs17h30,speak_17h30)
t17h30.start()

#17h45
y17h45=x.replace(day=x.day+1, hour=17, minute=45, second=0, microsecond=0)
delta_t17h45=y17h45-x
secs17h45=delta_t17h45.seconds+1
def speak_17h45():
  print(m17h45)
  toaster.show_toast("Pybot Notification","Il est 17h45",threaded=True,icon_path="icon.ico")
  import pyttsx3
  engine = pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m17h45)
  engine.runAndWait()
  engine.stop()
t17h45=Timer(secs17h45,speak_17h45)
t17h45.start()

#17h55
y17h55=x.replace(day=x.day+1, hour=17, minute=55, second=0, microsecond=0)
delta_t17h55=y17h55-x
secs17h55=delta_t17h55.seconds+1
def speak_17h55():
  print(m17h55)
  toaster.show_toast("Pybot Notification","Il est 17h55",threaded=True,icon_path="icon.ico")
  import pyttsx3
  engine = pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m17h55)
  engine.runAndWait()
  engine.stop()
t17h55=Timer(secs17h55,speak_17h55)
t17h55.start()

#17h59
y17h59=x.replace(day=x.day+1, hour=17, minute=59, second=0, microsecond=0)
delta_t17h59=y17h59-x
secs17h59=delta_t17h59.seconds+1
def speak_17h59():
  print(m17h59)
  toaster.show_toast("Pybot Notification","Il est 17h59",threaded=True,icon_path="icon.ico")
  import pyttsx3
  engine = pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m17h59)
  engine.runAndWait()
  engine.stop()
t17h59=Timer(secs17h59,speak_17h59)
t17h59.start()
