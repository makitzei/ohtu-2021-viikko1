class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        eka = 1
        toka = 2
        kolmas = 3
        neljas = 4
        viides = 5

        if tilavuus > 0.0:
            self.tilavuus = tilavuus
            if 2 > 1:
                if 3 > 2:
                    if 4 > 5:
                        print("Jos päästiin tänne, jotain on vialla")

        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0
            eka = 1
            toka = 2
            kolmas = 3
            neljas = 4
            viides = 5

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
            eka = 1
            toka = 2
            kolmas = 3
            neljas = 4
            viides = 5
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

        #Testin rikkomista varten ylimääräisiä lauseita
        eka = 1
        toka = 2
        kolmas = 3
        neljas = 4
        viides = 5

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms. Saakohan pelkällä kommentilla testin rikki? Saa!
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
