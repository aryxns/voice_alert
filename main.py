import speech_recognition as sr  
import pyttsx3
r = sr.Recognizer()
engine = pyttsx3.init()
 # obtain audio from the microphone  

with sr.Microphone() as source:  
	print("Please wait. Calibrating microphone...")  
	r.adjust_for_ambient_noise(source, duration=5)  
	print("Say something!")  
	audio = r.listen(source)  
check = str(r.recognize_google(audio))

 # recognize speech using Sphinx  
try:  
	print("aryxn's bot thinks you said '" + check + "'")  
except sr.UnknownValueError:  
	print("aryxn's bot could not understand your voice")  
except sr.RequestError as e:  
	print("Error!; {0}".format(e))

for check_word in check:
	if check_word == "A":
		print("Get Back To The Meeting")
		engine.say("Get Back To The Meeting")
		engine.runAndWait()
		break
	else:
		print("no problems")
	engine.runAndWait()
