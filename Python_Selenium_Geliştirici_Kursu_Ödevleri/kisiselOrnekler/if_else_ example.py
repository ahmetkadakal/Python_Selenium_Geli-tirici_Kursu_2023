#bu örnekde if else yapılarını kullanarak bir sayı tahmin oyunu yapacağım
import random   #bu rastgele sayı üreten bir python kütüphanesidir 

bulunacakSayi = random.randint(0,100) # bu kod 0 ile 100 arasında rastgele bir sayı üretecektir değişken isimlerini türkçe vermemin sebebi kodların yeni başlayanlar için daha anlaşılabilir olmasını istemem
tahminSayisi = 10 # kaç tahmin hakkı olsun istenyorsa
puan = 100 # her yanlış tahminde düşüreceğimiz sayı

#yukarda atamış olduğum değişkenkerin hepsi int yani tam sayı türündedir
print("Oyunumuza Hoşgeldiniz !!!\nBu oyunda tam 10 canınız var her yanlış cevabınızda canınız ve puanınız düşecek\nAman dikkat canınız biterse oyunu kaybedersiniz iyi şanslar \n 0-100 arasında tutulan sayı")
while True: # biz durdurana kadar dönecek bir döngü  
    kullaniciGirdisi = int(input("Tahminde Bulununuz (LÜTFEN SADECE SAYISAL DEĞER GİRİNİZ) : "))#burada kullanıcıdan bir Strin değer aldım ve onu bir int değere dönüştürdüm
    if (tahminSayisi>0):   # bunun amacı canımızın 0 dan fala olduğunu kontrol etmek
        if(kullaniciGirdisi == bulunacakSayi):# eğer doğru cevabı verdiysek bu ifin içine girer program
            print("Cevabı buldunuz tebrikler puanınız : " + " " +str(puan)+ " Kalan canınız : "+str(tahminSayisi))
            break#eğer doğru cevap gelirse oyunu bitirir
        elif(kullaniciGirdisi <= bulunacakSayi):#girilen sayı bulunması gereken sayıdan küçükmü kontrolü yapar
            tahminSayisi -= 1 # can düşer
            puan -= 10 # puan düşer
            print("Cevap daha yüksek bir sayı tekrar deneyin puanınız : " + "" +str(puan)+ " Kalan canınız : "+str(tahminSayisi)) 
        elif(kullaniciGirdisi >= bulunacakSayi):#girilen sayı bulunması gereken sayıdan büyükmü kontrolü yapar
            tahminSayisi -= 1# can düşer
            puan -= 10# puan düşer
            print("Cevap daha alçak bir sayı tekrar deneyin puanınız : " + "" +str(puan)+ " Kalan canınız : "+str(tahminSayisi)) 
    else:
        print("Bakıyorumda oyunu malesef kayıbetmişsin bulman gereken sayı : " + " " + str(bulunacakSayi))
        print("Üzülme sadece yeniden dene")
        break
"""
Arkadaşlar sadece bir örnek olması açısından yazdım 
Kendi bilgisayarınızda çalıştırmak isterseniz sadece kodları kopyalayıp yapıştırmanız yeeterli
Umarım açıklayıcı olmuştur 
İYİ ÇALIŞMALAR

!!! SADECE SAYISAL VERİ GİRİNİZ YOKSA PROGRAM HATA FIRLATACAKTIR

"""