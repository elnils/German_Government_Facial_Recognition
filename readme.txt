*************************************************************************************
*************************************************************************************
*************************************************************************************
*************************************************************************************
"Facial recognition with Python: A program to recognize the German Federal Cabinet"
-German text below-


1) Own question/objective

Increasingly, our everyday life is becoming more technological and digitalized, be it through the smartphone and related apps, "smart homes" and, above all, the public space. Recently, the topic of mass surveillance and face recognition has been limited to China and the social scoring system. However, there are constantly new attempts to set up automatic face recognition in public spaces in Germany (see Südkreuz Berlin). I wanted to understand more about how machine learning and face recognition works and thus tried building this little algorithm.

2) Justification of the approach

With the help of the library OpenCV I was able to train a face recognition for the current federal cabinet in less than 100 lines of code. 
In total I used three codes to automatically recognize the members of the current federal government.

	a) Firstly, I used the iCrawler (https://pypi.org/project/icrawler/) to crawl the first 100 images for each member of the federal government and put them into the appropriate folder.
	The file is called: "federal government_crawler.py"
	Then the 100 loaded pictures per person were cleaned by hand, because face recognition can only "learn properly" if the picture always shows one and the same person. I made sure that each person has at least 30 different images (after cleaning there is a variation of the number of images from 30 for Gerd Müller to 98 for Angela Merkel, which would be a lot of improvement, but it would take a lot of time to download all images individually until all persons have e.g. 100. For the purpose of the work I ask to tolerate this variation)

	b) Secondly, I wrote my own code and tried different variations of face and object recognition especially with the help of the OpenCV documentation (https://opencv-python-tutroals.readthedocs.io/en/latest/#), various YouTube tutorials and stackoverflow. OpenCV also offers the possibility to create your own classifier with e.g. Blob Detection, which I haven't tried yet due to lack of time, but would like to try it for satellite images. 
	The file is called: "bundesregierung.py"

	c) Thirdly, I wrote a learning algorithm for the face recognition code using the same sources from b) and tried face recognition several times using different images and number of "learning images".
	The file is called: "training.py" or the trained data is called "trainer.yml" or "labels.pickle".


3) Empirical demo

After several iterations my "Federal Government Face Recognition" has a relatively good recognition rate for some members of the federal government (Coincidentally especially for the CDU members: Angela Merkel, Annegret Kamp-Karrenbauer, Helge Braun, Anja Karliczek). Nevertheless, this is mainly due to 1) the good image quality in pixels 2) the high number of available individual photos 3) Probably due to certain "easily recognisable unique selling points". 
The file "d" shows how Angela Merkel is recognized and the corresponding probability is displayed.

From this project I have learned several things. Technically I wrote my first own Python program and it was very exciting to run through different iterations, to understand error messages or to learn how to formulate questions for stackoverflow. As a social scientist, I was interested in how the different iterations of face recognition work, how classifiers work and how OpenCV's classifiers were developed. All in all, it is amazing how little work these systems can do today and at the same time how easily they can be "outsmarted". A face recognition system needs countless images of a person to be able to classify them. But as soon as, for example, the inputs are not clean (i.e. the images for learning), people wear sunglasses or even close one eye, my program does not recognize the people anymore. Yes, my program is a very small project with little data, but these patterns can be transferred to large surveillance systems as the project "Adversial Fashion" (https://adversarialfashion.com/) shows. Finally, these are projects in which I would like to bring in perspective what I have learned from this project.

An example of the recognition of the Federal Cabinet works if you hold a photo (e.g. Angela Merkel) in front of the camera. This is shown in the attached file "Proof_Merkel.jpg". Nevertheless, it also shows that some people are recognized better than others. 
*************************************************************************************
*************************************************************************************
How the program works:

Start: python bundesregierung.py
Stop: Press the Q key (Quit)

Translated with www.DeepL.com/Translator (free version)

*************************************************************************************
*************************************************************************************
*************************************************************************************
"Gesichtserkennung mit Python: Ein Programm zur Erkennung des Bundeskabinetts"

1) Eigene Frage-/Zielstellung

Zunehmend technologisiert und digitalisiert sich unser Alltag, sei es durch das Smartphone und zugehörige Apps, "Smart Homes" und vor allem auch der öffentliche Raum. In jüngster Zeit hatte das Thema der Massenüberwachung und Gesichtserkennung sich vor allem auf China und das Social Scoring System beschränkt. Jedoch gibt es stetig neue Versuche eine automatische Gesichtserkennung im öffentlichen Raum in Deutschland einzurichten (siehe Südkreuz Berlin). Im Zusammenhang mit einem Unikurs wollte ich gerne selber genauer verstehen wie maschienelles Lernen und Gesichtserkennung funktioniert. 

2) Begründung des Vorgehens

Mit Hilfe der Library OpenCV ist es mir möglich gewesen in unter 100 Zeilen Code eine Gesichtserkennung für das aktuelle Bundeskabinett anzutrainieren. 
Insgesamt habe ich drei Codes genutzt um automatisiert die Mitglieder der aktuellen Bundesregierung zu erkennen.

	a) Erstens, habe ich mit dem iCrawler (https://pypi.org/project/icrawler/) die 100 ersten Bilder für jedes Mitglied der Bundesregierung gecrawled und in zugehörigen Ordner abgelegt.
	Die Datei heißt: "bundesregierung_crawler.py"
	Dann wurden die 100 geladenen Bilder pro Person händisch gesäubert, denn die Gesichtserkennung kann nur "richtig lernen", wenn auf dem Bild stets nur ein und die selbe Person abgebildet ist. Dabei habe ich drauf geachtet, dass jede Person mindestens 30 unterschiedliche Bilder hat (Nach dem Cleaning gibt es eine Variation der Bilderanzahl von 30 bei Gerd Müller bis 98 bei Angela Merkel, was insgesamt Verbesserungswürdig wäre, aber sehr viel Zeitaufwand wäre um alle Bilder einzeln herunterzuladen bis alle Personen zB 100 haben. Für den Zweck der Arbeit bitte ich diese Variation zu tolerieren)

	b) Zweitens, habe vor allem mit der OpenCV Dokumentation (https://opencv-python-tutroals.readthedocs.io/en/latest/#), verschiedenen YouTube-Tutorials und Stackoverflow, einen eigenen Code geschrieben und unterschiedliche Varianten der Gesichts- und Objekterkennung ausprobiert. OpenCV bietet auch durch zB Blob Detection die eigene Möglichkeit Classifier zu erstellen, was ich aus Zeitgründen noch nicht ausprobiert habe, aber perspektivisch gerne für Satelittenbilder ausprobieren möchte. 
	Die Datei heißt: "bundesregierung.py"

	c) Drittens, habe ich für den Code zur Gesichtserkennung einen Lernalgorithmus mit den gleichen Quellen aus b) geschrieben und die Gesichtserkennung mehrmals durch unterschiedliche Bilder, und Anzahl an "Lernbildern" ausprobiert.
	Die Datei heißt: "training.py" bzw. die trainierten Daten "trainer.yml" bzw. "labels.pickle"


3) Empirische Demo

Nach mehreren Iterationen hat meine "Bundesregierungs-Gesichtserkennung" eine relativ gute Erkennungsquote für einige Mitglieder der Bundesregierung (Zufälligerweise insbesondere für die CDU-Mitglieder: Angela Merkel, Annegret Kamp-Karrenbauer, Helge Braun, Anja Karliczek). Dennoch liegt dies vor allem an 1) der guten Bildqualität in Pixeln 2) Der hohen Anzahl an verfügbaren Einzelfotos 3) Wahrscheinlich an bestimmten "gut-erkennbaren Alleinstellungsmerkmalen". 
Die Datei "d" zeigt wie in etwa Angela Merkel erkannt wird und die zugehörige Wahrscheinlichkeit angezeigt wird.

Aus diesem Projekt habe ich verschiedene Dinge gelernt. Technisch betrachtet habe ich mein erstes eigene Python-Programm geschrieben wobei es sehr spannend war durch unterschiedliche Iterationen zu laufen, Fehlermeldungen zu versthene oder zu lernen wie genau man Fragen bei zB Stackoverflow formulieren sollte. Sozialwissenschaftliche habe ich mich damit beschäftigt wie die unterschiedlichsten Iteratonen der Gesichtserkennung funktionieren, wie Classifier funktionieren und wie genau OpenCV's Classifier entwickelt wurden. Insgesamt ist es erstauntlich mit wie "wenig Arbeit" diese Systeme heutzutage funktioneiren können und gleichzeitig auch wie einfach sie "überlistet" werden können. Eine Gesichtserkennung braucht unzählige Bilder einer Person um sie zu ordenn zu können. Jedoch sobald, zB die Inputs nicht sauber sind (also die Bilder zum lernen), Personen Sonnenbrillen tragen oder auch nur ein Auge schließen, so dann erkennt mein Programm die Personen nicht mehr. Ja, mein Programm ist ein sehr kleines Projekt mit wenigen Daten, dennoch lassen sich diese Muster auf die großen Überwachunssystem übertragen wie das Projekt "Adversial Fashion" (https://adversarialfashion.com/) zeigt. Schließlich sind dies Projekte in die ich mein gelerntes und erlerntes aus diesem Projekt perspektivisch einbringen möchte.

Ein Beispiel der Erkennung des Bundeskabinetts funktioniert, wenn man Foto (zB Angela Merkel) vor die Kamera hält. Dies zeigt die beiliegende Datei "Proof_Merkel.jpg". Dennoch zeigt sich dadurch auch, dass manche Personen besser erkannt werden als Andere. 
*************************************************************************************
Zur Funktionsweise des Programms:

Start: python bundesregierung.py
Stop: Drücke die Q-Taste (Quit)
*************************************************************************************
*************************************************************************************
*************************************************************************************
