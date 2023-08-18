class KelimeHarfAlgila:
    def __init__(self):
        self.metin = ""

    def metin_gir(self):
        self.metin = input("Bir metin girin: ")

    def harf_say(self):
        harf_sayisi = len([harf for harf in self.metin if harf.isalpha()])
        return harf_sayisi

    def kelime_say(self):
        kelimeler = self.metin.split()
        kelime_sayisi = len(kelimeler)
        return kelime_sayisi

    def calistir(self):
        self.metin_gir()
        harf_sayisi = self.harf_say()
        kelime_sayisi = self.kelime_say()

        print("Girilen metinde:")
        print(f"Toplam harf sayısı: {harf_sayisi}")
        print(f"Toplam kelime sayısı: {kelime_sayisi}")


if __name__ == "__main__":
    uygulama = KelimeHarfAlgila()
    uygulama.calistir()
