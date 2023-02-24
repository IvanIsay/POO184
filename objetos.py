
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

#Ejemplo del Set para 1 atributo
heroe.setNombre(" Pepe pecas ")

print("")
print("#######  Objeto Heroe ####")
print("El personaje se llama: "+ heroe.getNombre() )
print("pertenece a la especie: "+ heroe.getEspecie() )
print("y tiene una altura de : "+ str(heroe.getAltura() ))
heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargaH)

#Ejemplo de un metodo privado
#heroe.__pensar()


print("")
print("#######  Objeto Villano ####")

print("El personaje se llama: "+ villano.getNombre() )
print("pertenece a la especie: "+ villano.getEspecie() )
print("y tiene una altura de : "+ str(villano.getAltura() ))
villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargaV)







