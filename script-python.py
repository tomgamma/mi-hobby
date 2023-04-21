texto = open ('mihobby.md','r')
respuesta = texto.read()
diccionario = {}
lista = []

for AAA in range (1,6):
    lista.append(respuesta.splitlines()[AAA])

lista[0]= lista[0].replace("1.","")
lista[1]= lista[1].replace("2.","")
lista[2]= lista[2].replace("3.","")
lista[3]= lista[3].replace("4.","")
lista[4]= lista[4].replace("5.","")

for AAAA in range(5):
    diccionario[lista[AAAA].split(":")[0]] = lista[AAAA].split(":")[1] 

print(diccionario)