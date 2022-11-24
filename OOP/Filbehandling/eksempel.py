import csv
from pathlib import Path

filen = Path(__file__).parent / "eksempel.csv"

with open(filen) as fil:
    filinnhold = csv.reader(fil, delimiter=";")
        
    overskrifter = next(fil)
    print(overskrifter)

    #for rad in fil:
     #   print(rad)