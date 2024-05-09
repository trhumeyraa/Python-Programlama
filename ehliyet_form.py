#isim yaş eğitim, ehliyet için 18den büyük ya lise ya üniversite olmalı


print ("******EHLİYET ALABİLMENİZ İÇİN BİLGİLERİ DOLDURUNUZ****** \n")
username= str(input('adiniz: '))
age= int(input('yaşiniz: '))
school= str(input('eğitim durumunuz (ilkokul, ortaokul, lise, üni, hiç): '))
üni= 'üniversite'
lise= 'lise'
orta= 'ortaokul'
ilk= 'ilkokul'
hiç= 'hiç'

if ((age>=18) and (school== üni or school == lise)):
     print ("ehliyet alabilirisiniz.")
     
elif ((age < 18) and (school== üni or school == lise)):
     print ("ehliyet alamazsiniz yaşiniz tutmuyor ")
     
if ((age>=18 ) and ((school==ilk) or (school== orta) or (school== hiç))):
     print ("ehliyet alamazsınız eğitim durumunuz yetersiz")
