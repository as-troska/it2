import csv
import json
from pathlib import Path

class Fil:
    def __init__(self, filnavn, format = "dict", skilletegn = ";", tegnsett = "utf-8-sig"):
        self.filinnhold = []
        self.overskrifter = None
        self.filnavn = Path(__file__).parent / filnavn
        self.filtype = filnavn.split(".")[1]
        self.tegnsett = tegnsett
        self.skilletegn = skilletegn
        self.format = format

        match self.filtype:
            case "csv":
                match format:
                    case "dict":
                        with open(self.filnavn, encoding=self.tegnsett) as fil:
                            filinnholdet = csv.DictReader(fil, delimiter=self.skilletegn)
                            for rad in filinnholdet:
                                self.filinnhold.append(rad)
                    case "list":
                        with open(self.filnavn, encoding=self.tegnsett) as fil:
                            filinnholdet = csv.reader(fil, delimiter=self.skilletegn)
                            self.overskrifter = next(filinnholdet)
                            for rad in filinnholdet:
                                radinnhold = []
                                for verdi in rad:
                                    radinnhold.append(verdi)
                                self.filinnhold.append(radinnhold)
            case "json":
                with open(self.filnavn, encoding=self.tegnsett) as fil:
                    self.filinnhold.append(json.load(fil))
            case "txt":
                return     
            
    def skrivUt(self):
        match self.filtype:
            case "csv":
                match self.format:
                    case "dict":
                        for rad in self.filinnhold:
                            print(rad)
                    case "list":
                        print(self.overskrifter)            
                        print(self.filinnhold)
            case "json":
                formatert = json.dumps(self.filinnhold, indent = 2, ensure_ascii=False)
                print(formatert)            
        
    def skrivOver(self, innhold, sjekk = "n"):
        if (sjekk == "n"):
            while True:
                svar = input("Dette overskriver filen. Er du sikker? ")
                if svar.lower() == "y" or svar.lower() == "j" or svar.lower() == "ja" or svar.lower() == "yes":
                    with open(self.filnavn, "w") as fil: 
                        fil.write(innhold)
                    break
                else:
                    break

    def skrivTil(self, nyRad):
        if self.filtype == "csv":
            print(len(nyRad))
            print(len(self.filinnhold[0]))
            if type(nyRad) is not list or len(nyRad) != len(self.filinnhold[0]):
                print("Du kan bare legge til nye linjer i form av lister med like mange verdier som i den opprinnelige csv-fila")
            else:
                with open(self.filnavn, "a", newline='') as fil:
                    writer = csv.writer(fil, delimiter=self.skilletegn, quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(nyRad)
            self.oppfrisk()
        elif self.filtype == "text":
            return
        elif self.filtype == "json":
            if type(nyRad) is not dict:
                print("Du kan bare legge til dicts til jsoninnholdet")
            else:
                keys = list(self.filinnhold[0].keys())
                print(keys[0])
                if type(self.filinnhold[0][keys[0]]) is list:
                    self.filinnhold[0][keys[0]].append(nyRad)
                    ##Her må eg fjerne lista eg la til!
                    with open(self.filnavn, "w", encoding=self.tegnsett) as fil:
                        json.dump(self.filinnhold, fil, indent = 2, ensure_ascii=False)
                else:
                    self.filinnhold[0].append(nyRad)
                    with open(self.filnavn, "w", encoding=self.tegnsett) as fil:
                        json.dump(self.filinnhold, fil, indent = 2, ensure_ascii=False)
            self.oppfrisk()

        else:
            print("Ukjent filtype")
    
    def oppfrisk(self):
        self.filinnhold.clear()

        if self.filtype == "csv":        
            if self.format == "dict":
                with open(self.filnavn, encoding=self.tegnsett) as fil:
                    filinnholdet = csv.DictReader(fil, delimiter=self.skilletegn)

                    for rad in filinnholdet:
                        self.filinnhold.append(rad)                

            if self.format == "list":
                with open(self.filnavn, encoding=self.tegnsett) as fil:
                    filinnholdet = csv.reader(fil, delimiter=self.skilletegn)

                    self.overskrifter = next(filinnholdet)

                    for rad in filinnholdet:
                            radinnhold = []
                            for verdi in rad:
                                radinnhold.append(verdi)

                            self.filinnhold.append(radinnhold)
        elif self.filtype == "json":
            with open(self.filnavn, encoding=self.tegnsett) as fil:
                self.filinnhold = json.load(fil)

personer = Fil("folk.json")
personer.skrivUt()





        