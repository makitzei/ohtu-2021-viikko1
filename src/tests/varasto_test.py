import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virhevarasto = Varasto(-1, -1)
        self.ylivarasto = Varasto(5, 8)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_virheellisen_varaston_tilavuus_nolla(self):
        self.assertAlmostEqual(self.virhevarasto.tilavuus, 0)

    def test_virheellisen_varaston_saldo_nolla(self):
        self.assertAlmostEqual(self.virhevarasto.saldo, 0)
    
    def test_uuden_varaston_saldo_ei_ylita_tilavuutta(self):
        self.assertAlmostEqual(self.ylivarasto.saldo, 5)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)
    
    def test_negatiivinen_lisays_ei_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_liika_lisays_valuu_yli(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_negatiivista_maaraa_ei_voi_ottaa(self):
        self.varasto.lisaa_varastoon(5)
        maara = self.varasto.ota_varastosta(-3)
        
        self.assertAlmostEqual(maara, 0)
    
    def test_voidaan_ottaa_korkeintaan_saldon_verran(self):
        self.varasto.lisaa_varastoon(5)
        maara = self.varasto.ota_varastosta(8)
        
        self.assertAlmostEqual(maara, 5)
    
    def test_tulostus_oikein(self):
        self.assertEqual(
            str(self.varasto), 
            "saldo = 0, vielä tilaa 10")
