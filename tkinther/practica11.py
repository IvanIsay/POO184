from tkinter import Tk,Button,Frame,messagebox

#5. declaramos funcion para mensaje
def mostrarMensajes():
    messagebox.showinfo("Aviso:","Presionaste el boton azul")
    messagebox.showerror("Error:","Todo fallo con exito")
    print(messagebox.askokcancel("Pregunta","¿Ella o el  jugo con tu corazon?"))
 

#6. FUncion para agregar botones
def agregarBoton():
    botonVerde.config(text="+",bg="green",fg="white")
    botonNuevo= Button(seccion3,text="Nuevo")
    botonNuevo.pack()




 
    



#1.Instanciamos el objeto ventana
ventana= Tk()
ventana.title("Ejemplo de 3 Frames ")
ventana.geometry("600x400")

#2. agregamos los Frames
seccion1= Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both')

seccion2= Frame(ventana,bg="gray")
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana,bg="pink")
seccion3.pack(expand=True,fill='both')

#3. Agregamos botones
botonAzul= Button(seccion1,text="Boton Azul",fg="blue",command=mostrarMensajes)
botonAzul.place(x=60,y=60)

botonNegro= Button(seccion2,text="Boton Negro",fg="white", bg="black")
botonNegro.grid(row=0 , column=0)

botonAmarillo =Button(seccion2,text="Boton Amarillo", bg="#ffff4d")
botonAmarillo.grid(row=1 , column=1)

botonVerde=Button(seccion3,text="Boton Verde", bg="#99e699", command=agregarBoton)
botonVerde.configure(height=2,width=10)
botonVerde.pack()


#4. Poscionamiento de elemntos 


#llamamos al Main
ventana.mainloop()
