__author__ = 'aferreiradominguez'
#Diccionario
dicc={"Heat":"Miami","Cavaliers":"Cleveland","Lakers":"LA"}
print (dicc["Lakers"])
print (dicc.get("Lakers"))
print (dicc.items())
print (dicc.keys())
print (dicc.values())
print (dicc.pop("Lakers"))


#Lista
lis=[22,True,"lolo",[1,2,3]]
lis.append(5)
print(lis)
print(lis.count(True))
lis.extend(lis[1:3])
print(lis)
lis.insert(1,"tatatatata")
print(lis)
print(lis.index(True,0,5))
print(lis.index(True,5))
lis.remove(True)
print(lis)
lis.reverse()
print(lis)

#cadea
cadea="cadea de proba"
print(cadea.count("de"))
print(cadea.find("ba"))
cadea2=cadea.join("**")
print (cadea2)
print (cadea2.partition("de"))
print (cadea2.split("de"))
print (cadea2.replace("ca","lolololo"))
