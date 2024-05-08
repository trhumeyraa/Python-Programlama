names = ['Ali','Yağmur','Hakan', 'Deniz']


names+=['Cenk']
print (names)


str('Sena')
names.insert(0, 'Sena')
print (names)


names.pop(-2)
print (names)
 
 
names2 = ['Ali','Yağmur','Hakan', 'Deniz'] 
names2= names2.index('Deniz')
print (names2)


names3 = ['Ali','Yağmur','Hakan', 'Deniz']
isFound= 'Ali' in names
print (isFound)


names4= ['Ali','Yağmur','Hakan', 'Deniz']
names4.reverse()
print (names4)


names5 = ['Ali','Yağmur','Hakan', 'Deniz']
names5.sort()
print (names5)



print ('*************************************')



str= "Chevrolet , Dacia"
str= str.split(',')
print (str)