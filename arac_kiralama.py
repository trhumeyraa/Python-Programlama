#araç kiralama


gunsayisi= int(input("kaç gün kiraladınız?: "))

kmsayisi= int(input("kaç km yol gittiniz?: "))

gün = gunsayisi*500

km= kmsayisi*1

ucret = (float)((gün+km)*18)/100
sonuc= (float)(ucret+gün+km)
print (f"ödemeniz gereken tutar: {sonuc}")