# girilen sayının 0-100 arasında olup olmadığını karşılatırın.

sayi= int(input('sayi giriniz: '))

if ((sayi <= 100) and (sayi >= 0) ):
     print ("girdiğiniz sayi 0-100 arasindadir .")
     
elif (sayi > 100):
     print ("girdiğiniz sayi 100 den büyüktür. ")
     
else:
     print ("girdiğiniz sayi 0 dan küçüktür. ")
     