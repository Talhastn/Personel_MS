import random


class Hasta():
    def __init__(self, has_no, ad, soy, dog, hastalik, tedavi) -> None:
        self.__hasta_no: int = has_no
        self.__ad: str = ad
        self.__soyad: str = soy
        self.__dogum_tarihi: str = dog
        self.__hastalik: str = hastalik
        self.__tedavi: str = tedavi

    def __str__(self) -> None:
        print("Hasta No: {}, Ad-Soyad: {}, Dogum Tarihi: {}, Hastaligi: {}, Tedavi: {}".format(
            self.__hasta_no, self.__ad + " " + self.__soyad, self.__dogum_tarihi, self.__hastalik, self.__tedavi))

    def get_info(self) -> tuple:
        return self.__hasta_no, self.__ad, self.__soyad, self.__dogum_tarihi, self.__hastalik, self.__tedavi

    def set_info(self):
        pass

    def tedavi_suresi_hesapla(self) -> int:
        return random.randint(0, 7)
