import csv
import doktor
import hasta
import hemsire
import personel
import pandas as pd


# Dataya her seferinde eklemeye yarar.
def reload_dataframe():
    global df
    df = pd.read_csv(path)


# Dataları kaydeder.
def save_dataFrame(per_no=0, ad=0, soyad=0, dep=0, maas=0, uzmanlik=0, deneyim_yili=0, hastane=0, calisma_saati=0, sertifika=0, hasta_no=0, dogum_tarihi=0, hastalik=0, tedavi=0):
    liste = [per_no, ad, soyad, dep, maas, uzmanlik, deneyim_yili, hastane, calisma_saati, sertifika, hasta_no, dogum_tarihi, hastalik, tedavi]
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(liste)


# Dataya ve classlara personel ekler.
def personel_ekle():
    per_no, ad, soyad, dep, maas = personel_instance.get_info()
    save_dataFrame(per_no, ad, soyad, dep, maas, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    reload_dataframe()


# Dataya ve classlara doktor ekler.
def doktor_ekle():
    per_no, ad, soyad, dep, maas = doktor_instance.get_pers()
    uzmanlik, deneyim, hastane = doktor_instance.get_info()
    save_dataFrame(per_no, ad, soyad, dep, maas, uzmanlik, deneyim, hastane, 0, 0, 0, 0, 0, 0)
    reload_dataframe()


# Dataya ve classlara hemsire ekler.
def hemsire_ekle():
    per_no, ad, soyad, dep, maas = hemsire_instance.get_pers()
    calisma, sert, hast = hemsire_instance.get_info()
    save_dataFrame(per_no, ad, soyad, dep, maas, 0, 0, hast, calisma, sert, 0, 0, 0, 0)
    reload_dataframe()


# Dataya ve classlara hasta ekler.
def hasta_ekle():
    has_no, ad, soyad, dog, hastalik, tedavi = hasta_instance.get_info()
    save_dataFrame(0, ad, soyad, 0, 0, 0, 0, 0, 0, 0, has_no, dog, hastalik, tedavi)
    reload_dataframe()


# Datayi okur
path = "information.csv"
df = pd.read_csv(path)


# Data verileri
personel_instance = personel.Personel(5040, "Mahmut", "Kura", "Temizlik Gorevlisi", 2300)
personel_ekle()
personel_instance = personel.Personel(5041, "Riza", "Kocakulak", "Tekniker", 2700)
personel_ekle()
hemsire_instance = hemsire.hemsire(1313, "Ayse", "Kulucka", "Hemsire", 3900, 12, True, "Bozyaka")
hemsire_ekle()
hemsire_instance = hemsire.hemsire(1313, "Melike", "Kocuman", "Hemsire", 2800, 4, True, "Dokuz Eylul")
hemsire_ekle()
hemsire_instance = hemsire.hemsire(1313, "Ayse", "Kulucka", "Hemsire", 3300, 7, True, "Yesilyurt")
hemsire_ekle()
doktor_instance = doktor.doktor(2230, "Murat", "Kosan", "Doktor", 7500, "Beyin Cerrahi", 26, "Yesilyurt")
doktor_ekle()
doktor_instance = doktor.doktor(2233, "Cemile", "Gursoy", "Doktor", 6000, "Kardiyoloji", 11, "Trafik")
doktor_ekle()
doktor_instance = doktor.doktor(2232, "Duran", "Tekerlek", "Doktor", 5500, "Kardiyoloji", 4, "Ege")
doktor_ekle()
hasta_instance = hasta.Hasta(1234, "Rukiye", "Basibos", "11/06/1973", "Febromiyerji", "Kardiyo")
hasta_ekle()
hasta_instance = hasta.Hasta(1234, "Abdulrezzak", "Kefenli", "25/12/1944", "Kalp", "Otenazi")
hasta_ekle()
hasta_instance = hasta.Hasta(1234, "Ogun", "Gucumaydin", "02/02/2002", "Kirik", "Alci")
hasta_ekle()


# Uzmanliklara göre doktor sayilarini yazdirir.
def uzmanlik_alani_sayilari() -> None:
    uzmanlik_sayisi = df["uzmanlik"].value_counts()
    for uzmanlik, sayi in uzmanlik_sayisi.items():
        if uzmanlik != "0":
            print(f"{sayi} adet {uzmanlik} doktorumuz bulunmakta.")


# 5 yildan fazla deneyime sahip doktorlari yazdirir.
def deneyeimli_doktor() -> None:
    doktorlar = df[df["departman"] == "Doktor"]
    cok_deneyimli = doktorlar[doktorlar["deneyim_yili"] > 5].shape[0]
    print("5 yildan cok hizmet etmis doktorlar: {}".format(cok_deneyimli))


# Isme gore alfabetik siralama yapar.
def siralama():
    df_sorted = df.sort_values(by='ad')
    print(df_sorted)


# 7000'den fazla para alan personelleri bulan fonksiyon
def fazla_para_alan():
    maaslar = df[df["maas"] >= 7000]
    cok_parali = maaslar['ad'].tolist()

    for i in cok_parali:
        print("7000'den fazla para alan personeller: {}".format(i))


# 1990 yilindan sonra dogmus olan kisilerin isimleri ve dogum yillarini yazdiran fonskiyon
def gencler():
    tarihler = df[df["dogum_tarihi"] != '0']
    for index, row in tarihler.iterrows():
        dogum_yili = row["dogum_tarihi"][-4:]
        hasta_adi = row["ad"]
        if int(dogum_yili) > 1990:
            print("Hasta adı: {}, Doğum yılı: {}".format(hasta_adi, dogum_yili))


# Dataframe'den yeni bir dataframe olusturan fonksiyon
def new_df():
    newdf = df[["ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastalik", "tedavi"]]
    print(newdf)


uzmanlik_alani_sayilari()
deneyeimli_doktor()
siralama()
fazla_para_alan()
gencler()
new_df()
