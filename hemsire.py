import personel


class hemsire(personel.Personel):
    def __init__(self, personel_no, ad, soyad, dep, maas, calisma_saati, sertifika, hastane) -> None:
        super().__init__(personel_no, ad, soyad, dep, maas)
        self.__calisma_saati: int = calisma_saati
        self.__sertifika: bool = sertifika
        self.__hastane: str = hastane

    def __str__(self) -> None:
        print("Calistigi saat: {}, Sertifikasi: {}, Hastane: {}".format(self.__calisma_saati, self.__sertifika, self.__hastane))

    def get_info(self) -> tuple:
        return self.__calisma_saati, self.__sertifika, self.__hastane

    def get_pers(self) -> tuple:
        return super().get_info()

    def set_info(self) -> None:
        pass

    def maas_arttir(self) -> int:
        no, ad, soyad, dep, maas = super().get_info()
        return round(maas * 1.2)