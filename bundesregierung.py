# -*- coding: utf-8 -*-
#*************************************************************************************
#*************************************************************************************
#*************************************************************************************
#Inhaltsverzeichnis
#*************************************************************************************
#_0) Allgemeines (Libraries die geladen und installiert werden koennten)
#_1) Libraries importieren
#_2) Gesichts- und Augenklassifizierer laden (Deep-Learned Modelle aus dem OpenCV Package) sowie Kamera starten
#_3) OpenCV starten und definieren 
#_4)Kamerafenster laden und beenden (Q-Taste)



#_0) Allgemeines
#installiere libraries
#pip install numpy --upgrade
#pip install pickle --upgrade
#OpenCV herunterladen und installieren: Wie Du OpenCV2 instalieren kannst: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html
#pip install matpolitlib --upgrade

#*************************************************************************************
#*************************************************************************************
#*************************************************************************************

#_1) Libraries importieren

import numpy as np
import cv2, time
import matplotlib.pyplot as plt
import pickle
import os

#*************************************************************************************
#*************************************************************************************
#*************************************************************************************

#_2) Gesichts- und Augenklassifizierer laden (Deep-Learned Modelle aus dem OpenCV Package) sowie Kamera starten
gesichts_klassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
augen_klassifier = cv2.CascadeClassifier('haarcascade_eye.xml')

# Anwendung von Trainingsdaten um Prognose zu treffen über Person im Frame. 1) Lade den (gleichen) "Recognizer" aus den Trainingsdaten 2)Lade die Datei mit den trainierten Daten
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {"person_name": 1}
with open ("labels.pickle", "rb") as f: #lade mir das gelabelte Dictionary mit den Pickles aus den Trainingsdaten
	og_labels = pickle.load(f)
	labels = {value:key for key,value in og_labels.items()} #Umkehrung der Werte im Dictionary, damit die Namen angezeigt werden und nicht die Nummer

video = cv2.VideoCapture(0) #Starte das Video (an manchen Rechnern wird die Kamera mit (1) erfasst, aber default ist 0)
a=0
while True:
	a = a+1
	check, frame = video.read()
	print (check)
	print (frame)

#*************************************************************************************
#*************************************************************************************
#*************************************************************************************

#_3) OpenCV starten und definieren 

#OpenCV arbeitet mit Graumelierungen zur Erkennung, daher transformieren wir den Input nach Grau
	grau=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#Nun sollen alle Gesichter gefunden werden
	gesichter= gesichts_klassifier.detectMultiScale(grau, 1.3,5)

#Nun wird ein For-Loop erstellt um Iterativ "über den Frame zu gehen"

	for (x,y,w,h) in gesichter:
#Zeichne ein Rechteck über erkannte Gesichter und Augen in der "BGR-Farbe" (Blau, Grün, Rot) 255,0,0 in Stärke 2.
#x= x-Achse, y=Y-Achse, w=Breite (width), h=Höhe

		cv2.rectangle (frame, (x,y), (x+w, y+h), (255,0,0),2)
#Definiere die "Region of Interest" der Analyse (Höhe und Breite)

		roi_grau = grau[y:y+h, x:x+w]
		roi_farbe= frame[y:y+h, x:x+w]
		augen = augen_klassifier.detectMultiScale (roi_grau)
		for (ex,ey,ew,eh) in augen:
			cv2.rectangle (roi_farbe, (ex,ey), (ex+ew, ey+eh), (0,255,0), 1)
		id_, conf = recognizer.predict(roi_grau)

#Wenn die Übereinstimmung des im Frame gezeigten Gesichts zwischen 70-100% liegt, dann zeige die ID/Namen aus dem Trainingsset

		if conf >=85 and conf <=100:
		# print (id_) #Es ist möglich  id's und labels anzeigen, verbraucht aber viel Ram!
		# print (labels[id_])
			schriftart = cv2.FONT_HERSHEY_PLAIN #OpenCV bietet verschiedene Schriftarten an
			name = labels[id_]
			color = ((255, 255, 255))
			stroke = 1

			cv2.putText(frame, name, (x,y), schriftart, 1, color, stroke, cv2.LINE_AA) #Boxen beschriften
			cv2.putText(frame, str (conf), (x,y-20), schriftart, 0.75, color, stroke, cv2.LINE_AA)

#*************************************************************************************
#*************************************************************************************
#*************************************************************************************

#_4) Kamerafenster laden und beenden

	cv2.imshow("Aufnahme", frame)
	if cv2.waitKey(20) & 0xFF == ord("q"): #Beende die Aufnahme wenn Q gedrückt wird
		break

video.release()
cv2.destroyAllWindows()
