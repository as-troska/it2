import math as m

class Planet:
    """
    Klasse for å lage planet-objekter.

    Parametere:
    navn(str): Planetens navn
    solavstand (float): Avstand fra sola i millioner km.
    radius (float): Planetens radius i km
    antallRinger = 0 (int): Antall ringer rundt planeten
    antallMaaner = 0 (int): Antall måner planeten har.
    """
  
    def __init__(self, navn:str, solavstand:float, radius:float, antallRinger:int = 0, antallMaaner:int = 0):
        """
        Konstruktør
        """
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
        self.antallRinger = antallRinger
        self.antallMaaner = antallMaaner

    def volum(self):
        return (4/3) * m.pi * self.radius**3

    def overflate(self):
        return 4 * m.pi * self.radius**2

    def lystidfrasol(self):
        return (self.solavstand*1000000) / 300000

merkur = Planet("Merkur", 62.925, 4879/2)
venus = Planet("Venus", 108.242, 12104/2)
jorda = Planet("Jorda", 148.492, 12756/2, 0, 1)


print(merkur.navn)
print(venus.radius)
print(jorda.solavstand)

#help(Planet)

print(merkur.volum())
print(venus.volum())
print(jorda.volum())

print(merkur.overflate())
print(venus.overflate())
print(jorda.overflate())

print(merkur.lystidfrasol())
print(venus.lystidfrasol())
print(jorda.lystidfrasol())

