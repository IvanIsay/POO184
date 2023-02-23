
from Personaje import *

#1. Solicitar Datos
print("")
print("#######  Datos Heroe #####")
especieH= input("Escribe la especie del Heroe:  ") 
nombreH= input("Escribe el nombre del Heroe:  ") 
alturaH= float(input("Escribe la altura del Heroe:  ")) 
recargaH= int(input("Cuantas Balas recargas al Heroe:  "))

print("")
print("#######  Datos Villano ####")
especieV= input("Escribe la especie del Villano:  ") 
nombreV= input("Escribe el nombre del Villano:  ") 
alturaV= float( input("Escribe la altura del Villano:  ") )
recargaV= int(input("Cuantas Balas recargas al Villano:  ")) 


#2. Crear objeto de clase Personaje

heroe= Personaje(especieH,nombreH,alturaH)
villano= Personaje(especieV,nombreV,alturaV)

#3. Usar atributos y metodso

print("")
print("#######  Objeto Heroe ####")
print("El personaje se llama: "+ heroe.nombre)
print("pertenece a la especie: "+ heroe.especie)
print("y tiene una altura de : "+ str(heroe.altura))
heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargaH)


print("")
print("#######  Objeto Villano ####")

print("El personaje se llama: "+ villano.nombre)
print("pertenece a la especie: "+ villano.especie)
print("y tiene una altura de : "+ str(villano.altura))
villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargaV)







