#pip install pyttsx3
#pip install playsound
from datetime import datetime
from threading import Timer

x=datetime.today()
h=x.hour
m=x.minute+1
s=0

if x.minute>58:
  h=x.hour+1
  m=0
  s=0

print("Welcome to the PYBOT2.0 demo")
print("Il est "+str(x.hour)+"h", str(x.minute)+"m", str(x.second)+"s, la démo commencera à "+str(h)+"h", str(m)+"m", str(s)+"s")

#messages
m15h="Il est 15h. L'atelier multimédia est terminé."
m15h55="Il est 15h55. La séance se terminera dans 5 minutes."
m16h="Il est 16h. La séance de 15h est terminée. Merci de bien vouloir fermer votre session."
m16h55="Il est 16h55. La séance se terminera dans 5 minutes."
m17h="Il est 17h. La séance de 16h est terminée. Merci de bien vouloir fermer votre session."
m17h30="La Médiathèque fermera ses portes dans 30 minutes."
m17h45="La Médiathèque fermera ses portes dans 15 minutes."
m17h55="La Médiathèque fermera ses portes dans 5 minutes."
m17h59="La Médiathèque fermera dans 1 minute. Merci de bien vouloir fermer votre session."

#voice rate setting
rate=150

#15h
y15h=x.replace(day=x.day+1, hour=h, minute=m, second=s, microsecond=0)
delta_t15h=y15h-x
secs15h=delta_t15h.seconds+1
def speak_15h():
  print("15h00 : "+m15h)
  import pyttsx3
  engine=pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m15h)
  engine.runAndWait()
  engine.stop()
t15h=Timer(secs15h,speak_15h)
t15h.start()

#15h55
y15h55=x.replace(day=x.day+1, hour=h, minute=m, second=s+10, microsecond=0)
delta_t15h55=y15h55-x
secs15h55=delta_t15h55.seconds+1
def speak_15h55():
  print("15h55 : "+m15h55)
  import pyttsx3
  engine=pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m15h55)
  engine.runAndWait()
  engine.stop()
t15h55=Timer(secs15h55,speak_15h55)
t15h55.start()

#16h
y16h=x.replace(day=x.day+1, hour=h, minute=m, second=s+20, microsecond=0)
delta_t16h=y16h-x
secs16h=delta_t16h.seconds+1
def speak_16h():
  print("16h00 : "+m16h)
  import pyttsx3
  engine=pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m16h)
  engine.runAndWait()
  engine.stop()
t16h=Timer(secs16h,speak_16h)
t16h.start()

#16h55
y16h55=x.replace(day=x.day+1, hour=h, minute=m, second=s+30, microsecond=0)
delta_t16h55=y16h55-x
secs16h55=delta_t16h55.seconds+1
def speak_16h55():
  print("16h55 : "+m16h55)
  import pyttsx3
  engine=pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m16h55)
  engine.runAndWait()
  engine.stop()
t16h55=Timer(secs16h55,speak_16h55)
t16h55.start()

#17h
y17h=x.replace(day=x.day+1, hour=h, minute=m, second=s+40, microsecond=0)
delta_t17h=y17h-x
secs17h=delta_t17h.seconds+1
def speak_17h():
  print("17h00 : "+m17h)
  import pyttsx3
  engine=pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m17h)
  engine.runAndWait()
  engine.stop()
t17h=Timer(secs17h,speak_17h)
t17h.start()

#17h30
y17h30=x.replace(day=x.day+1, hour=h, minute=m, second=s+50, microsecond=0)
delta_t17h30=y17h30-x
secs17h30=delta_t17h30.seconds+1
def speak_17h30():
  print("17h30 : "+m17h30)
  import pyttsx3
  engine=pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m17h30)
  engine.runAndWait()
  engine.stop()
t17h30=Timer(secs17h30,speak_17h30)
t17h30.start()

#17h45
y17h45=x.replace(day=x.day+1, hour=h, minute=m+1, second=s, microsecond=s)
delta_t17h45=y17h45-x
secs17h45=delta_t17h45.seconds+1
def speak_17h45():
  print("17h45 : "+m17h45)
  import pyttsx3
  engine=pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m17h45)
  engine.runAndWait()
  engine.stop()
t17h45=Timer(secs17h45,speak_17h45)
t17h45.start()

#17h55
y17h55=x.replace(day=x.day+1, hour=h, minute=m+1, second=s+10, microsecond=s)
delta_t17h55=y17h55-x
secs17h55=delta_t17h55.seconds+1
def speak_17h55():
  print("17h55 : "+m17h55)
  import pyttsx3
  engine=pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m17h55)
  engine.runAndWait()
  engine.stop()
t17h55=Timer(secs17h55,speak_17h55)
t17h55.start()

#17h59
y17h59=x.replace(day=x.day+1, hour=h, minute=m+1, second=s+20, microsecond=s)
delta_t17h59=y17h59-x
secs17h59=delta_t17h59.seconds+1
def speak_17h59():
  print("17h59 : "+m17h59)
  import pyttsx3
  engine=pyttsx3.init()
  engine.setProperty("rate",rate)
  engine.say(m17h59)
  engine.runAndWait()
  engine.stop()
t17h59=Timer(secs17h59,speak_17h59)
t17h59.start()