import sys

saldo = 0
kontoer = [{"kontoNummer": "1234",
            "passord": "laks",
            "saldo": 1000},
            {"kontoNummer": "4321",
            "passord": "ost",
            "saldo": 7621},
            {"kontoNummer": "5555",
            "passord": "moskus",
            "saldo": 2000000}
        ]

def loggInnMeny():
    print("**********************")
    print("*      PYBANKEN      *")
    print("**********************")
    print("")
    print("1) Velg konto         ")
    print("2) Avslutt            ")
    valg = input("Gjør ditt valg: ")

    if (valg == "1"):
        print("")
        loggInn()
    elif (valg == "2"):
        print("")
        sys.exit("Takk for at du brukte PYBanken")
    else:
        print("")
        print("Gjør et gyldig valg")
        print("")
        loggInnMeny()

def loggInn():
    global kontoer

    print("**********************")
    print("*      PYBANKEN      *")
    print("**********************")
    print("")
    kontoValg = input("Skriv ditt kontonummer: ")

    for konto in kontoer: 
        if (kontoValg == konto["kontoNummer"]):
            passord = input("Skriv ditt passord: ")
            if (passord == konto["passord"]):
                kontoMeny(kontoValg)
            else:
                print("")
                print("Ugyldig kontonummer eller passord")
                print("")
                loggInnMeny()

def kontoMeny(kontonummer):

    print("")
    print("1) Se din Saldo")
    print("2) Sett inn penger")
    print("3) Ta ut penger")
    print("4) Logg ut")
    print("5) Avslutt")
    print("")
    
    valg = input("Gjør ditt valg: ")

    for konto in kontoer:
        if kontonummer == konto["kontoNummer"]:
            if valg == "1":
                print("Din saldo: ", konto["saldo"])
                kontoMeny(kontonummer)
            if valg == "2":
                innskudd = int(input("Innskudsbeløp: "))
                #Bør sjekke at ikke innskudd er negativt, men orker ikke akkurat nå
                konto["saldo"] = konto["saldo"] + innskudd
                print("Ny saldo: ", konto["saldo"])
                kontoMeny(kontonummer)
            if valg == "3":
                uttak = int(input("Uttaksbeløp: "))
                #Bør sjekke at det er nok penger på konto, men orker ikke akkurat nå
                konto["saldo"] = konto["saldo"] - uttak
                print("Ny saldo: ", konto["saldo"])
                kontoMeny(kontonummer)
            if valg == "4":
                loggInnMeny()
            if valg == "5":
                print("")
                sys.exit("Takk for at du brukte PYBanken")
            else:
                print("")
                print("Ugyldig valg")
                print("")
                kontoMeny(kontonummer)          

loggInnMeny()


