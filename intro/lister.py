#Det er lurt å kunne nokre måter å lage lister på:

#Manuelt
liste = ["Dette", "er", "ei", "liste"]
print(liste[0], liste[1], liste[2], liste[3])

#Liste med tal
talListe = list(range(1,10))
print(talListe)
talListe = list(range(1,11))
print(talListe)
talListe = list(range(0, 11, 2))
print(talListe)

#Treng du ei liste med alfabetet? https://datagy.io/python-list-alphabet/

#Liste frå liste
listen = liste
liste.pop()
print(listen)

listen = list(liste)
liste.append("liste")
print(liste)
print(listen)

#Desse listemetodene bør de kunne: pop, insert, remove, append, reverse og sort
feitMusikk = []
feitMusikk.append("Autechre")
feitMusikk.append("Venetian Snares")
feitMusikk.append("Jazkammer")
print(feitMusikk)
feitMusikk.insert(0, "Kode9 and the Spaceape")
feitMusikk.insert(1, "Massive Attack")
print(feitMusikk)
feitMusikk.insert(2, "Einsturzende Neubauten")
feitMusikk.pop()
print(feitMusikk)
feitMusikk.remove("Einsturzende Neubauten")
print(feitMusikk)
feitMusikk.append("Einsturzende Neubauten")
feitMusikk.append("Einsturzende Neubauten")
feitMusikk.remove("Einsturzende Neubauten")
print(feitMusikk)
feitMusikk.sort()
print(feitMusikk)
print(feitMusikk.index("Massive Attack"))
feitMusikk.reverse()
print(feitMusikk)

#Nokre måtar å sjå etter noko i ei liste
print(feitMusikk.index("Massive Attack"))
print("Ballinciaga" in feitMusikk)
print("Kode9 and the Spaceape" in feitMusikk)
feitMusikk.append("Kode9 and the Spaceape")
print(feitMusikk.count("Kode9 and the Spaceape"))
print(feitMusikk.count("DJ Khaled"))


