#pip install pyttsx3
from datetime import datetime
from threading import Timer
x=datetime.today()

#15h
y15h=x.replace(day=x.day+1, hour=15, minute=0, second=0, microsecond=0)
delta_t15h=y15h-x
secs15h=delta_t15h.seconds+1
def speak_15h():
  print("Il est exactement 15h. L'atelier multimédia est malheureusement déjà terminé. Merci de votre participation.")
  import pyttsx3
  engine = pyttsx3.init()
  engine.say("Il est exactement 15h. L'atelier multimédia est malheureusement déjà terminé. Merci de votre participation.")
  engine.runAndWait()
  engine.stop()
t15h=Timer(secs15h,speak_15h)
t15h.start()

#15h55
y15h55=x.replace(day=x.day+1, hour=15, minute=55, second=0, microsecond=0)
delta_t15h55=y15h55-x
secs15h55=delta_t15h55.seconds+1
def speak_15h55():
  print("La séance se terminera dans 5 minutes.")
  import pyttsx3
  engine = pyttsx3.init()
  engine.say("La séance se terminera dans 5 minutes.")
  engine.runAndWait()
  engine.stop()
t15h55=Timer(secs15h55,speak_15h55)
t15h55.start()

#16h
y16h=x.replace(day=x.day+1, hour=16, minute=0, second=0, microsecond=0)
delta_t16h=y16h-x
secs16h=delta_t16h.seconds+1
def speak_16h():
  print("Il est exactement 16h. La séance de 15h est terminée. Merci de bien vouloir fermer votre session.")
  import pyttsx3
  engine = pyttsx3.init()
  engine.say("Il est exactement 16h. La séance de 15h est terminée. Merci de bien vouloir fermer votre session.")
  engine.runAndWait()
  engine.stop()
t16h=Timer(secs16h,speak_16h)
t16h.start()

#16h55
y16h55=x.replace(day=x.day+1, hour=16, minute=55, second=0, microsecond=0)
delta_t16h55=y16h55-x
secs16h55=delta_t16h55.seconds+1
def speak_16h55():
  print("La séance se terminera dans 5 minutes.")
  import pyttsx3
  engine = pyttsx3.init()
  engine.say("La Médiathèque fermera dans 5 minutes.")
  engine.runAndWait()
  engine.stop()
t16h55=Timer(secs16h55,speak_16h55)
t16h55.start()

#17h
y17h=x.replace(day=x.day+1, hour=17, minute=0, second=0, microsecond=0)
delta_t17h=y17h-x
secs17h=delta_t17h.seconds+1
def speak_17h():
  print("Il est exactement 17h. La séance de 16h est terminée. Merci de bien vouloir fermer votre session.")
  import pyttsx3
  engine = pyttsx3.init()
  engine.say("Il est exactement 17h. La séance de 16h est terminée. Merci de bien vouloir fermer votre session.")
  engine.runAndWait()
  engine.stop()
t17h=Timer(secs17h,speak_17h)
t17h.start()

#17h30
y17h30=x.replace(day=x.day+1, hour=17, minute=30, second=0, microsecond=0)
delta_t17h30=y17h30-x
secs17h30=delta_t17h30.seconds+1
def speak_17h30():
  print("La Médiathèque fermera ses portes dans 30 minutes.")
  import pyttsx3
  engine = pyttsx3.init()
  engine.say("La Médiathèque fermera ses portes dans 30 minutes.")
  engine.runAndWait()
  engine.stop()
t17h30=Timer(secs17h30,speak_17h30)
t17h30.start()

#17h45
y17h45=x.replace(day=x.day+1, hour=17, minute=45, second=0, microsecond=0)
delta_t17h45=y17h45-x
secs17h45=delta_t17h45.seconds+1
def speak_17h45():
  print("La Médiathèque fermera ses portes dans 15 minutes.")
  import pyttsx3
  engine = pyttsx3.init()
  engine.say("La Médiathèque fermera ses portes dans 5 minutes.")
  engine.runAndWait()
  engine.stop()
t17h45=Timer(secs17h45,speak_17h45)
t17h45.start()

#17h55
y17h55=x.replace(day=x.day+1, hour=17, minute=55, second=0, microsecond=0)
delta_t17h55=y17h55-x
secs17h55=delta_t17h55.seconds+1
def speak_17h55():
  print("La Médiathèque fermera dans 5 minutes.")
  import pyttsx3
  engine = pyttsx3.init()
  engine.say("La Médiathèque fermera dans 5 minutes.")
  engine.runAndWait()
  engine.stop()
t17h55=Timer(secs17h55,speak_17h55)
t17h55.start()

#17h59
y17h59=x.replace(day=x.day+1, hour=17, minute=59, second=0, microsecond=0)
delta_t17h59=y17h59-x
secs17h59=delta_t17h59.seconds+1
def speak_17h59():
  print("La Médiathèque fermera dans 1 minute. Merci de bien vouloir fermer votre session.")
  import pyttsx3
  engine = pyttsx3.init()
  engine.say("La Médiathèque fermera dans 1 minute. Merci de bien vouloir fermer votre session.")
  engine.runAndWait()
  engine.stop()
t17h59=Timer(secs17h59,speak_17h59)
t17h59.start()