# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv, os, glob, requests, textract
from stopwords import stop
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import pandas as pd
import re

laListe = []

dfPays = pd.read_csv("pays.csv")

dfCompilation = pd.read_csv("compilationFinale.csv")

source = "devoir-api.csv"
 
entetes = {
	"User-Agent":"Thomas Dufour - requête transmise pour projet de journalisme de données dans le cours EDM5240 à l'UQAM",
	"From":"thomasdufour4@gmail.com"
}

fr = 0
nonFr = 0
nb = 0
row = 1095

f1 = open(source)
dates = csv.reader(f1)
next(dates)

#Permet de sauter une partie du document devoir-api pour commencer plus loin

for i in range(649):

	next(dates)

for date in dates:

	jour = date[1] + "/" + date[2] + "/" + date[3]

	print(jour)

	m = 0

	print("&"*66)

	urlFichier = "http://collections.banq.qc.ca/{}".format(date[5])

	nomFichier = os.path.basename(urlFichier)

	print("On va chercher le fichier {}\nà l'URL {}".format(nomFichier,urlFichier))

	pdf = requests.get(urlFichier, stream=True, headers=entetes)

	with open("pdfs/{}".format(nomFichier), 'wb') as fuddle:
		for chunk in pdf.iter_content(100):
			fuddle.write(chunk)

	texte = textract.process("pdfs/{}".format(nomFichier))

	#texte = texte.decode('utf-8')

	#texte = re.split(" |' ", texte)

	#print(texte)

	mots = word_tokenize(texte.decode('utf-8'))

	#print(mots)
	
	debut = ""
	x = 0

	Motlist = []

	for mot in mots:

		mot = debut + mot

		if "\xad" in mot:
			debut = mot.replace("\xad","")
			x = 1
			nb += 1

		else:
			debut = ""
			x = 0

		mot = mot.lower()

		if "-" in mot:
			mot = mot.replace("-", "")

		if mot not in stop:
			if mot.isalpha():
				if len(mot) > 1:
					m += 1
					phrase = mot
					Motlist.append(phrase)

	#print(Motlist)

	for i,x in enumerate(dfPays["Pays"]):

			colonne = dfPays.iloc[i][0]

			dfCompilation.set_value(row, colonne, 0)

			country = Motlist.count(x)

			#print(colonne)
	
			if country > 0:

				dfCompilation.set_value(row, colonne, country)

				print(x)

				print("-" * 80)

	dfCompilation.set_value(row, 'DATE', jour)

	dfCompilation.to_csv("compilationFinale.csv", index=False)
				
	row += 1

	os.remove("pdfs/{}".format(nomFichier))
	
