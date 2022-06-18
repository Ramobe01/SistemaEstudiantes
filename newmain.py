from msilib.schema import CheckBox, ComboBox
import tkinter as tk
from tkinter import ttk
import ventana

window = tk.Tk()
window.title('Sistema de Gestión Educativo')
window.geometry('700x460')
window.resizable(True,True)

#Etiquetas - Labels
##Datos Personales
datos = ventana.Label()  
datos.hacer_etiqueta(window,'Datos Personales',0,0,2,0,(5,10))
datos.hacer_etiqueta(window,'Nombre',1,0,1,0,0)
datos.hacer_etiqueta(window,'Apellido',2,0,1,0,0)
datos.hacer_etiqueta(window,'DNI',3,0,1,0,0)
datos.hacer_etiqueta(window,'Domicilio',4,0,1,0,0)
datos.hacer_etiqueta(window,'Género',5,0,1,0,0)
###Grado
datos.hacer_etiqueta(window,'Año',6,0,1,0,0)


###Materias
datos.hacer_etiqueta(window,'Materias',8,0,2,0,0)

#Entradas - Entrys
e_nombre = ventana.Entry()
e_nombre.hacer_entrada(window,1,1)

e_apellido = ventana.Entry()
e_apellido.hacer_entrada(window,2,1)

e_dni = ventana.Entry()
e_dni.hacer_entrada(window,3,1)

e_domicilio = ventana.Entry()
e_domicilio.hacer_entrada(window,4,1)


#Checkbox
c_materia_literatura = ventana.CheckButton('Literatura')
c_materia_literatura.hacer_check_button(window,'Literatura',9,0,'W',(10,0))

c_materia_matematica = ventana.CheckButton('Matemática')    
c_materia_matematica.hacer_check_button(window,'Matematica',9,1,'E',0)

c_materia_ingles = ventana.CheckButton('Inglés')
c_materia_ingles.hacer_check_button(window,'Inglés',10,0,'W',(10,0))

c_materia_educ_fis = ventana.CheckButton('Educ.Física')
c_materia_educ_fis.hacer_check_button(window,'Educ. Física',10,1,'E',0)

c_materia_ciencias = ventana.CheckButton('Ciencias')
c_materia_ciencias.hacer_check_button(window,'Ciencias',11,0,'W',(10,0))

c_materia_religion = ventana.CheckButton('Religión')    
c_materia_religion.hacer_check_button(window,'Religión',11,1,'E',(0,18))

c_materia_artes = ventana.CheckButton('Artes')
c_materia_artes.hacer_check_button(window,'Artes',12,0,'W',(10,0))

c_materia_historia = ventana.CheckButton('Hisoria')    
c_materia_historia.hacer_check_button(window,'Historia',12,1,'E',(0,20))

c_materia_geo = ventana.CheckButton('Geografía')
c_materia_geo.hacer_check_button(window,'Geografía',13,0,'W',(10,0))

c_materia_quimica = ventana.CheckButton('Química')    
c_materia_quimica.hacer_check_button(window,'Química',13,1,'E',(0,17))

materias_disponibles = (c_materia_literatura,c_materia_matematica,c_materia_ingles,c_materia_educ_fis,c_materia_ciencias,c_materia_religion,c_materia_artes,c_materia_historia,c_materia_geo,c_materia_quimica)

#Lista Desplegable - ComboBox
com_genero = ventana.ComboBox()
com_genero.hacer_lista_desplegable(window,'readonly',('Femenino','Masculino','Otro'),5,1,0)

com_anio = ventana.ComboBox()
com_anio.hacer_lista_desplegable(window,'readonly',('1er','2do','3ro', '4to', '5to'),6,1,0)

#Botones
boton = tk.Button(text='Click',command=lambda: ventana.boton_aniadir(lbx_estudiante,e_nombre.obtener_entrada(),e_nombre,e_apellido,e_dni,e_domicilio,com_genero,com_anio,materias_disponibles))
boton.grid(row=20,column=0)

#Separador
separator = ttk.Separator(window,orient= tk.VERTICAL, style='TSeparator')
separator.grid(column=2, row=0, rowspan=30, sticky='NS',padx=(15,0))


#frame2
lbx_estudiante = tk.Listbox(window)
lbx_estudiante.grid(row=1,column=3, sticky='NSEW', rowspan=14, columnspan=4)
lbx_estudiante.bind('<<ListboxSelect>>')

window.columnconfigure(3,weigh=1)
window.rowconfigure(1, weight=2)
window.rowconfigure(2, weight=2)
window.rowconfigure(3, weight=2)
window.rowconfigure(4, weight=2)
window.rowconfigure(5, weight=2)
window.rowconfigure(6, weight=2)
window.rowconfigure(8, weight=2)
window.rowconfigure(9, weight=2)
window.rowconfigure(10, weight=2)
window.rowconfigure(11, weight=2)
window.rowconfigure(12, weight=2)
window.rowconfigure(13, weight=2)
window.rowconfigure(14, weight=2)
window.rowconfigure(15, weight=2)


window.mainloop()