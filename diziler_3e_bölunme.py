sayilar= [1,3,5,7,9,12,19,21]


for sayi in sayilar:
   if (sayi%3==0):
     print (sayi)
     
     
toplam= 0
for sayi in sayilar:
     toplam += sayi
print ("toplam: ", toplam)


for sayi in sayilar:
     if (sayi%2 !=0 ):
         print (sayi**2)