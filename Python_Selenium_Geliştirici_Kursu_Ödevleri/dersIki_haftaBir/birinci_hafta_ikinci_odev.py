ogrenciler = []
programKapat = False


def ogrEkle():
    ogrSayisi = int(input("Kaç tane öğrenci eklemek istiyorsunuz : "))
    for i in range(ogrSayisi):
        ogr = input("Öğrenci girişi yapınız : ")
        ogrenciler.append(ogr)


def ogrSil():
    ogrSilinecekSayisi = int(input("Kaç kişi sileceksiniz : "))
    ogrSilinecekListesi = []
    x = 0
    while ogrSilinecekSayisi:
        x += 1
        ogrSilinecek = input(
            "Silinicek değerleri isim soyisim şeklinde giriniz : ")
        ogrSilinecekListesi.append(ogrSilinecek)

        for i in ogrenciler:
            if i in ogrSilinecekListesi:
                ogrenciler.remove(i)
            else:
                continue
        if ogrSilinecekSayisi == x:
            break

    print(ogrSilinecekListesi)

    print("Yeni listedeki öğrenci saysı: " + str(len(ogrenciler)))
    for i in ogrenciler:
        print("Yeni listedeki öğrenciler : " + str(i))


def ogrGoster():
    ogrNumara = 0
    for i in ogrenciler:
        ogrNumara += 1
        print(str(ogrNumara) + " : " + str(i))


def ogrNumaraOgren():
    numarasiOgrenilecek = input("Kimin dizi indexini öğrenmek istiyorsunuz : ")
    x = 0
    for i in ogrenciler:
        if i == numarasiOgrenilecek:
            print("Kişi bulundu aradığınız kişi '" +
                  str(i) + "' İndex numarası : " + str(x))
        x += 1


def kapat():
    print("Program sonlandırılıyor son kişi listesi : ")
    for i in ogrenciler:
        print(i)
    programKapat = True
    return programKapat


def menu():
    menuSec = int(input("Yapmak istediğiniz işlemi seçiniz : \n 1 = > Öğreci ekle \n 2 = > Öğrenci sil \n 3 = > Eklenmiş olan öğrencileri göster \n 4 = > Kayıtlı öğrenci numarası öğren \n 5 = > Programı kapat ve listenin son halini getir \n Menüde verilen değerlerden herhangi birini kullanabilmek için başındaki menü numarasını tuşlayaınız .... "))
    if menuSec == 1:
        ogrEkle()
    elif menuSec == 2:
        ogrSil()
    elif menuSec == 3:
        ogrGoster()
    elif menuSec == 4:
        ogrNumaraOgren()
    elif menuSec == 5:
        return kapat()
    else:
        print("-------------  Hatalı giriş tekrar deneyin --------------------")


while True:
    if menu():
        break
