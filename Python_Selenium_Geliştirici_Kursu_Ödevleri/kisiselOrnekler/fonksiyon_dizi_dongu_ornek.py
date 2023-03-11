degerler = []#boş bir dizi tanımladım
def veriAl():#bu fonksiyon kullanıcıdan veri alarak tanımlamış olduğum degerler dizisine ekliyor
    girilenDeger = input("Lütfen diziye eklememi istediğiniz değeri giriniz : ")
    degerler.append(girilenDeger)
    return degerler

def veriGoster(degerler):# bu fonksiyon ise diziye eklemiş olduğum değerleri gezerek ekrana yazıyor
    for i in degerler:
        print(i)

while True:#bu aslında sonsuz bir döngüdür kullanıcı N değerini girene kadar dönmeye devam edecektir
    devamMi = input("Veri girmek için y programı durdurup girilen veriliri görmek için N degeri girin : ")
    if devamMi == "y": # girilen değer için bir karar yapısı eğer kullanıcı y girerse veri alacaktır
        gelenDegerler = veriAl()
    elif devamMi == "N": # kullanıcıdan gelen değer N ise değer almayı bırakıp değerleri gösteren fonksiyonu çalıştıracak
        veriGoster(gelenDegerler)
        break
    else:# hatalı bir bir giriş yapılırsa kod hata fırlatmak yerine yeniden değer isteyecektir
        print("Hatalı tuşlama yapıldı lütfen tekrar deger giriniz : ")
        gelenDegerler 
