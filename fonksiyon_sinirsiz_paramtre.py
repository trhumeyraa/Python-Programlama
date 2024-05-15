#yazdığoımız fonksiyondaki sınırsız parametreyi listeye eklesin


def paramtre(*params):
  liste=[]
  for param in params:
               liste.append(param)
               
  return liste

a=paramtre(10,21065,55,355,65,5,66,652,566,5665,5566,) 
print(a)