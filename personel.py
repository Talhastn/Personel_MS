class Personel():
    def __init__(self, personel_no, ad, soyad, dep, maas) -> None:
        self.__personel_no: int = personel_no
        self.__ad: str = ad
        self.__soyad: str = soyad
        self.__departman: str = dep
        self.__maas: int = maas

    def __str__(self) -> None:
        print("Personel Ad-Soyad: {}".format(self.__ad + " " + self.__soyad) + "/nPersonel departmani: {}".format(self.__departman) + "/nPersonel maas: {}".format(self.__maas))

    def get_info(self) -> tuple:
        return self.__personel_no, self.__ad, self.__soyad, self.__departman, self.__maas

    def set_info(self):
        pass
