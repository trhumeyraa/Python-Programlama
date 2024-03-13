# 3e ve 4e bölünme

sayi=int(input('bir sayi girin: '))

if (sayi % 3== 0 ) and (sayi % 4 == 0):
               print ('sayi 3e ve 4e tam bölünür')
               
elif (sayi % 3 == 0) and (sayi % 4 != 0):
               print ('sayi 3e tam bölünür ')
               
elif (sayi % 3 != 0) and (sayi % 4 == 0):
               print ('sayi 4e tam bölünür ')
               
elif (sayi % 3 != 0) and (sayi % 4 != 0):
               print ('sayi 3e ve 4e tam bölünmez')