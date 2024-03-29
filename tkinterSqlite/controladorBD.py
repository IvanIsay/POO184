from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    # Preparamos la coneccion para usarala cuando sea necesario
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:/Users/lOkY/Documents/GitHub/POO184/tkinterSqlite/DBUsuarios.db")
            print("Conectado BD")
            return conexion
        
        except sqlite3.OperationalError:
             print(" No se pudo conectar")
          
    # Metodo para Insertar        
    def guardarUsuario(self,nom,cor,con):
        
        # 1. llamar a la conexion
        conx= self.conexionBD()
        
        # 2. Revisar parametros vacios
        if( nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Aguas!!", "Revisa tu formulario")
            conx.close()
        else:
            #3. Prepara datos y el querySQL
            cursor= conx.cursor()
            conH= self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInsert="insert into TBRegistrados(nombre,correo,contra) values(?,?,?)"
            
            #4. Proceder a Insertar y cerramos la Conx
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito"," Se guardo el Usuario")
        
            
    def encriptarCon(self,con):
        conPlana= con
        conPlana= conPlana.encode() #convertimos con a bytes
        sal= bcrypt.gensalt()
        
        conHa= bcrypt.hashpw(conPlana,sal)
        #print(conHa)
        return conHa
    
    def consultaUsuario(self,id):
        #1. preparar la conexion
        conx= self.conexionBD()
        
        #2.verificar que el ID no este vacio
        if( id == ""):
            messagebox.showwarning("Cuidado","Id vacio escribe uno valido")
            conx.close()
        else: 
            # 3.proceder a buscar
            try:
                #4. Prepara lo necesario para el select
                cursor= conx.cursor()
                sqlSelect="select * from TBRegistrados where id="+id 
                
                #5. Ejecucion y guardado de la consulta
                cursor.execute(sqlSelect)
                RSusuario= cursor.fetchall()
                conx.close()
                
                return RSusuario
                
            except sqlite3.OperationalError:
                print("Error Consulta")