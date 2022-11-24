class Person:
    """
    Klasse for å lage et person-objekt.

    Parametere:
    fornavn (str): Personens fornavn
    etternavn (str): Personens etternavn
    fodselsaar (int): Personens fodselsår. Fire siffer.
    """
    def __init__ (self, fornavn:str, etternavn:str, fodselsaar:int):
        """
        Konstruktør
        """
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fodselsaar = fodselsaar

trond = Person("Trond", "Skauge", 1984)

