#parola ve wmail bilgisi isteyip doğruluğunu kontrol edin.
# email: email@hmeyragy.com  parola: 252525

username= 'hmeyragy'
password= 254125

isim= str(input ('email adinizi giriniz : '))

şifre= int(input ('email şifrenizi giriniz: '))


if (username == isim and password == şifre):
     print (True)
     
elif (username != isim or password != şifre ):
     print (False)
     
     
