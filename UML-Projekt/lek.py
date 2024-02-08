import random
from abc import ABC, abstractmethod

class Ware(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._artikelNr : str
        self._kosten: float
    
    @abstractmethod
    def setArtikelNr(self, artikelNr: str) -> None:
        pass

    @abstractmethod
    def getArtikelNr(self) -> str:
        pass

    @abstractmethod
    def berechneKosten(self, basiswert: float) -> float:
        pass

class Material(Ware):
    def __init__(self, name: str, qualität: str, verfallsdatum: str) -> None:
        super().__init__()
        self.__name = name
        self.__qualität = qualität
        self.__verfallsdatum = verfallsdatum

    def setArtikelNr(self, artikelNr: str) -> None:
        self._artikelNr = artikelNr

    def getArtikelNr(self) -> str:
        return self._artikelNr

    def berechneKosten(self, basiswert: float) -> float:
        if self.__qualität != "mies":
            return basiswert*2
        return basiswert

class Dienstleistung(Ware):
    def __init__(self, material_1: Material, material_2: Material, dauer: float) -> None:
        super().__init__()
        self.__materialverbrauch = [material_1,material_2]
        self.__verantwortlicher : int
        self.__dauer = dauer

    def istGewinn(self) -> bool:
        return random.randint(0,2) % 2 == 0

    def setArtikelNr(self, artikelNr: str) -> None:
        self._artikelNr = artikelNr

    def getArtikelNr(self) -> str:
        return self._artikelNr
    
    def berechneKosten(self, basiswert: float) -> float:
        self.__dauer = basiswert
        if self.istGewinn():
            return -1.0
        # berechnung der GESAMTkosten hier, nicht in einem 
        # einzelnen material, weil GESAMT
        gesamtkosten = 0
        for material in self.__materialverbrauch:
            gesamtkosten += material.berechneKosten(self.__dauer)
        return gesamtkosten

class Kunde():
    def __init__(self, ware : Ware, kundenwunschdauer: float):
        self.__eineWare = ware
        self.__gesamtkosten : int
        self.__kundenwunschdauer = kundenwunschdauer
        self.__gesamtkosten = self.__eineWare.berechneKosten(self.__kundenwunschdauer)
        self.ausgabe(self.__gesamtkosten)

    def ausgabe(self,kostenwert):
        if kostenwert == -1.0:
            return print("Die Dienstleistung kann ohne zusätzliche Kosten in Anpsruch genommen werden")
        return print(f"Die Dienstleistung wird Mindestens {kostenwert} kosten. Sie müssen mehr bezahlen als erwartet"  )

class Main():
    def __init__(self) -> None:
        kühlflüssigkeit = Material("Kühlflüssigkeit", "gut", "Ende 2026")
        schmierstoff = Material("schmiere", "mies", "2024")
        zahnräder = Material("Zahnräder", "gut", "2248")
        zahnräder_pflegen = Dienstleistung(schmierstoff, zahnräder, 1)
        kühlung_erneuern = Dienstleistung(kühlflüssigkeit, kühlflüssigkeit, 1)
        kunde1 = Kunde(kühlung_erneuern, 1)
        kunde2 = Kunde(zahnräder_pflegen, 1)

if __name__ == "__main__":
    start = Main()