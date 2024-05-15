#yazığımız fonksiyonda 2 sayı arasındaki tüm asalları bulsun



def asalSayiBulma(sayi1, sayi2):
      for asal in range(sayi1,sayi2+1):
         if asal > 1:
                        for i in range (2,asal):
                                       if asal % i == 0:
                                        break
                        else:
                                       print (asal)
sayi1=int(input('sayi 1: '))
sayi2=int(input('sayi 2: '))                                       
asalSayiBulma(sayi1,sayi2)