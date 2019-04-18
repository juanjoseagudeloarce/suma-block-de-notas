import os
import random

vector_uno=[]
vector_dos=[]
vector_suma=[]
archivo = open("suma block notas","w")

for i in range(6):
    vector_uno.append(random.randint(0,20))
    vector_dos.append(random.randint(0,20))
for i in range(len(vector_uno)):
    vector_suma.append(vector_uno[i]+vector_dos[i])

for i in vector_uno:
    archivo.write(" "+str(i))
archivo.write("\n")
for i in vector_dos:
    archivo.write(" "+str(i))
archivo.write("\n__________________\n")
for i in vector_suma:
    archivo.write(" "+str(i))
print ("Archivo Generado...")
archivo.close()
