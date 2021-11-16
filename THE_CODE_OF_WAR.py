import random
import sys
import time

class THE_CODE_OF_WAR :
    def __init__(self,isim,can=3,enerji=100) -> None:
        self.isim = isim
        self.can = can
        self.enerji = enerji
        self.darbe = 0

    def durum_rapor_ver(self):
        print("Darbe :",  self.darbe )
        print("Can :" , self.can)
        print("Enerji :",self.enerji)

    def saldır(self,rakip):
        print("Bir saldırı gerçekleştirdiniz...")
        print("Lütfen Bekleyiniz\n")
        for i in range(10):
            time.sleep(.3)
            print(".",end="",flush=True)
        
        sonuç = self.saldırı_sonucu_hesapla()

        if sonuç == 0 :
            print("kazanan veya kaybeden taraf yok .")
        if sonuç== 1:
            print("SONUÇ : \n Rakibinizi darbelediniz.")
            self.darbele(rakip)
        if sonuç == 2:
            print("sonuç : \n rakibinizden darbe aldınız." )
            rakip.darbele(siz)
        
    def saldırı_sonucu_hesapla(self):
        return random.randint(0, 2)

    def kaç(self):
        print("KAÇILIYOR .." )
        for i in range(10):
            time.sleep(.3)
            print("\n" , flush=True)

        print("rakibiniz sizi yakaladı\n")
        print("rakibinizle burun burunasınız.")
    
    def darbele(self,darbelenen) :
        darbelenen.darbe += 1
        darbelenen.enerji -= 10
        if darbelenen.darbe % 5 == 0 :
            darbelenen.can -= 1
        if darbelenen.can < 1 :
            darbelenen.enerji = 100
            print('Oyunu {} kazandı!'.format(self.isim))
            self.oyundan_çık()
    
    def oyundan_çık(self):
        print('Çıkılıyor...')
        sys.exit()

siz = THE_CODE_OF_WAR("ibrahim")
rakip = THE_CODE_OF_WAR('cin ali')

while True:
    print("s:     SALDIR , \nr :     KAÇ , \nq:     ÇIKIŞ , ")
    hamle = input('\n> ')

    if hamle == "s" :
        siz.saldır(rakip)

        print("rakibinizin durumu : \n", rakip.durum_rapor_ver() )
        print("sizin durumunuz : \n", siz.durum_rapor_ver() )

    if hamle == "r":
        siz.kaç()

    if hamle == "q":
        siz.oyundan_çık()