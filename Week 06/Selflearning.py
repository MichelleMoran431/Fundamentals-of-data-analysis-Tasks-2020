# Week 6 Self learning lecture
#Converting a CSV file so that the panda program can read it accurately
import pandas as pd
import csv



dfauto = pd.read_csv('auto-mpg.csv',sep="\s+")

print(dfauto)
