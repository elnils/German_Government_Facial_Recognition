#Importiere Libraries
import cv2
import os
import numpy as np
#pip install pillow --update
from PIL import Image #Python Image Library
import pickle
# pip install opencv-contrib-python

#Definiere den Ort der Dateo final_training.py
BASIS_DIR = os.path.dirname(os.path.abspath(__file__))
#Finde den Ort wo meine Bilder liegen, die "trainiert werden sollen"
bilder_dir = os.path.join(BASIS_DIR, "bilder")


gesichts_klassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
augen_klassifier = cv2.CascadeClassifier('haarcascade_eye.xml')
# print(dir (cv2.face))

#Definiere den "Gesichtserkenner" 
recognizer = cv2.face.LBPHFaceRecognizer_create()


current_id = 0 #Erstelle leeres Dictionoary mit Label-Ids 
label_ids ={}
y_labels =[]
x_train = []

#Lade die Bilder
for root, dirs, files in os.walk(bilder_dir):
	for file in files:
#Lade alle PNG oder jpg
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root,file)
# Drucke mir den Ort von dem geladenen Bild (zur Kontrolle beim Laden)
			print (path)
# Definieren, dass das Label dem Ordnernamen entspricht von den jeweiligen Bildern - Also alle Angela Merkel Bilder sind nummeriert, aber sie liegen alle im Ordner "Angela Merkel". Außerdem: Schreib alles klein und ersetze Leerzeichen durch Bindestrichte
			label = os.path.basename(root).replace(" ", "-").lower()
			print (label, path)
			if not label in label_ids: #Falls Label noch nicht vorhanden, erstelle eins für die jeweilige ID
				label_ids[label]= current_id
				current_id +=1
			id_ = label_ids[label]
			print(label_ids)
			# y_labels.append(label)
			# x_train.append(path)
			pil_image = Image.open(path).convert("L") #Konvertiere Bild in Grau/Monochrom nach PIL (Python Image Library)
			groesse = (750, 750) #anlyse alle bilder in gleichem format *nach* der Gesichtserkennung, so dass alle Gesichter etwa gleich groß sind..
			#Konvertriere Bilder zu Matritzen --> numpy.array
			final_image = pil_image.resize(groesse, Image.ANTIALIAS)
			image_array = np.array(final_image, "uint8")
			print(image_array)

# Definiere "Region of Interests" 
			gesichter= gesichts_klassifier.detectMultiScale(image_array, 1.3,5)
			for (x, y,w,h) in gesichter:
				roi = image_array[y:y+h, x:x+w]
				x_train.append(roi)
				y_labels.append(id_)
			
			augen= augen_klassifier.detectMultiScale (image_array, 1.3,5)
			for (ex, ey,ew,eh) in augen:
				roi2 = image_array[ey:ey+eh, ex:ex+ew]
				x_train.append(roi2)
				y_labels.append(id_)
			
# print(y_labels)
# print(x_train)

#Speichere die Labels ab für meinen Hauptdatensatz! :)
with open ("labels.pickle", "wb") as f: #wb = writing bytes
	pickle.dump(label_ids, f)

#Final: Traniere die Daten und konvertiere alle ins gleiche Formate (numpy-arrays)!
recognizer.train(x_train, np.array(y_labels))
#Speichere die Ergebnisse
recognizer.save("trainer.yml")