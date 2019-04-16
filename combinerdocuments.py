# coding: utf-8

import csv
import pandas as pd

#Document utilisé pour combiné les différentes périodes sur lesquelles ont été prélevées les données

df1259 = pd.read_csv("compilationFinale-1910-1959.csv")

df6069 = pd.read_csv("compilationFinale-1960-1969.csv")

df7079 = pd.read_csv("compilationFinale-1970-1979.csv")

df8084 = pd.read_csv("compilationFinale-1980-1984.csv")

df8589 = pd.read_csv("compilationFinale-1985-1989.csv")

df9099 = pd.read_csv("compilationFinale-1990-1999.csv")

df0005 = pd.read_csv("compilationFinale-2000-2005.csv")

df0608 = pd.read_csv("compilationFinale-2006-2008.csv")

df0911 = pd.read_csv("compilationFinale-2009-2011.csv")

frames = [df1259, df6069, df7079, df8084, df8589, df9099, df0005, df0608, df0911]

result = pd.concat(frames)

with open("tousEditions.csv", "w") as my_empty_csv:
  pass

result.to_csv("tousEditions.csv", index=False)

print(result.head(20))
