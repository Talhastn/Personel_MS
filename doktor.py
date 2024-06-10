import personel


class doktor(personel.Personel):
    def __init__(self, personel_no, ad, soyad, dep, maas, uzmanlik, deneyim, hastane) -> None:
        super().__init__(personel_no, ad, soyad, dep, maas)
        self.__uzmanlik: str = uzmanlik
        self.__deneyim_yili: int = deneyim
        self.__hastane: str = hastane

    def __str__(self) -> None:
        print("Uzmanligi: {}, Deneyim yili: {}, Hastane: {}".format(self.__uzmanlik, self.__deneyim_yili, self.__hastane))

    def get_info(self) -> tuple:
        return self.__uzmanlik, self.__deneyim_yili, self.__hastane

    def get_pers(self) -> tuple:
        return super().get_info()

    def set_info(self) -> None:
        pass

    def maas_arttir(self) -> int:
        no, ad, soyad, dep, maas = super().get_info()
        return round(maas * 1.2)
