class Pekac:

    def __init__(self, polmer1, polmer2):
        self.polmer1 = polmer1
        self.polmer2 = polmer2

    def __str__(self):
        return "Pretvori iz pekača s polmerom {} v pekač s polmerom {}".format(self.polmer1, self.polmer2)

    def razmerje_ploscin_pekaca(self):
        import math
        ploscina1 = math.pi*float(self.polmer1)**2
        ploscina2 = math.pi*float(self.polmer2)**2
        return ploscina2/ploscina1


class Sestavina:

    def __init__(self, kolicina, sestavina, mera):
        self.kolicina = kolicina
        self.sestavina = sestavina
        self.mera = mera
        self.pretvorjeno = None

    def __str__(self):
        return "{} {} {}".format(self.sestavina, self.kolicina, self.mera)

    def pretvori(self, pekac):
        razmerje = pekac.razmerje_ploscin_pekaca()
        nova_kolicina = razmerje * int(self.kolicina)
        return nova_kolicina


class Recept:
    def __init__(self, sestavine, pekac):
        self.sestavine = sestavine
        self.pekac = pekac

    def dodaj_sestavino(self, sestavina):
        self.sestavine.append(sestavina)

    def Izracunaj(self):
        for sestavina in self.sestavine:
            sestavina.pretvorjeno = round(sestavina.pretvori(self.pekac), 1)

    def izpisi_nov_recept(self):
        prikaz = ''
        for sestavina in self.sestavine:
            prikaz += ('<p> ' + str(sestavina) + ': ' +
                       str(round(sestavina.pretvori(self.pekac), 1)) + sestavina.mera + ' </p>')
        return prikaz
