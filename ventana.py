import tkinter as tk
from tkinter import ttk
from xmlrpc.client import Boolean

class Label:
    def __init__(self):
        pass

    def hacer_etiqueta(self,ventana,text,row,column,columnspan,padx,pady):
        etiqueta = tk.Label(ventana,text=text)
        etiqueta.grid(row=row,column=column,columnspan=columnspan,padx=padx,pady=pady)

class Entry:
    def __init__(self):
        self.dato = tk.StringVar()

    def hacer_entrada(self,ventana,row,column):
        entrada = tk.Entry(ventana,textvariable=self.dato)
        entrada.grid(row=row,column=column)

    def obtener_entrada(self):
        valor = self.dato.get()
        return valor


class CheckButton():
    def __init__(self,nombre):
        self.dato = tk.BooleanVar()
        self.nombre = nombre 
        

    def hacer_check_button(self,ventana,text,row,column,sticky,padx):
        checkbutton = tk.Checkbutton(ventana,text=text,variable=self.dato)
        checkbutton.grid(row=row,column=column,sticky=sticky,padx=padx)

    def obtener_valor(self):
        valor = self.dato.get()
        return valor

class ComboBox(Entry):
    def hacer_lista_desplegable(self,ventana,state,values,row,column,pady):
        lista = ttk.Combobox(ventana,state=state,values=values,textvariable=self.dato)
        lista.grid(row=row,column=column,pady=pady)

class Button:
    def __init__(self):
        pass

    def hacer_boton(self,ventana,text,row,column,columspan,padx,pady,width,command):
        boton = tk.Button(ventana,text=text,command=command)
        boton.grid(row=row,column=column,columnspan=columspan,padx=padx,pady=pady,width=width)



class Estudiante:

    def __init__(self,nombre,apellido,dni,domicilio,genero,anio,materias):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.domicilio = domicilio
        self.genero = genero
        self.materias = materias
    

#FUNCIONES
def boton_aniadir(ventana,estudiante,*entradas):
    nombre = entradas[0].obtener_entrada()
    apellido = entradas[1].obtener_entrada()
    dni = entradas[2].obtener_entrada()
    domicilio = entradas[3].obtener_entrada()
    genero = entradas[4].obtener_entrada()
    anio = entradas[5].obtener_entrada()
    materias = checkear_materia(entradas[6])
    estudiante = Estudiante(nombre,apellido,dni,domicilio,genero,anio,materias)
    l_formulario = Label()
    l_formulario.hacer_etiqueta(ventana,'{} {} {}'.format(estudiante.nombre,estudiante.apellido,estudiante.dni),2,10,5,0,0)
    print(estudiante.materias)

def checkear_materia(materias):
    materias_cursadas = []
    for materia in materias:
        if (materia.obtener_valor() == True):
            materias_cursadas.append(materia.nombre)
    return tuple(materias_cursadas)

