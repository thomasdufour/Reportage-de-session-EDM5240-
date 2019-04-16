# coding: utf-8

import csv
import pandas as pd

dfTous = pd.read_csv("LeDevoir.csv")

df3 = dfTous["NbEditions"]

#print(df3)

with open("articleDevoir.csv", "w") as my_empty_csv:
  pass

fichier = "articleDevoir.csv"

s = []

dfDate = dfTous["DATE"]

#Code permettant de diviser les lignes par le nombre d'éditions du Devoir

dfTous = dfTous.iloc[:,2:].div(dfTous.NbEditions, axis=0)

dfTous = dfTous * 100

#Ajouter la colonne des dates

dfTous = dfTous.join(dfDate)

cols = dfTous.columns.tolist()

#Changer une colonne de place

cols = cols[-1:] + cols[:-1]

dfTous = dfTous[cols]

del dfTous['NbEditions']

#Arrondir les résultats

dfTous = dfTous.round(decimals=2)

print(dfTous.head(20))

dfTous.to_csv("articleDevoir.csv", index=True)
