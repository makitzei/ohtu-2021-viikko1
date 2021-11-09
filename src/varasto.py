def tarkista_ala(muuttuja):
    if muuttuja < 0.0:
        return 0.0
    return muuttuja

def tarkista_yla(muuttuja, raja):
    if muuttuja > raja:
        return raja
    return muuttuja

class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = tarkista_ala(tilavuus)
        self.saldo = tarkista_yla(tarkista_ala(alku_saldo), self.tilavuus)

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms. Tehdään tästä rivistä testin vuoksi taas vähän liian pitkä.
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
