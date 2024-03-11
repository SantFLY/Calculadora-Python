from tkinter import *

ventanta = Tk()
ventanta.title("Calculadora en python")

i=0

e_Texto = Entry(ventanta)
e_Texto.grid(row=0, column=0, columnspan=4, padx=5)


#funciones a realizar con la calculadora
def click_boton(valor):
    global i
    e_Texto.insert(i, valor)
    i +=1
    
def borrar():
    e_Texto.delete(0, END)
    i = 0

def hacer_operaciones():
    ecuacuacion = e_Texto.get()
    resultado = eval(ecuacuacion)
    e_Texto.delete(0, END)
    e_Texto.insert(0, resultado)
    i=0


#Numeros
boton1 = Button(ventanta, text='1', width=5, height=2, command= lambda: click_boton(1))
boton2 = Button(ventanta, text='2', width=5, height=2, command= lambda: click_boton(2))
boton3 = Button(ventanta, text='3', width=5, height=2, command= lambda: click_boton(3))
boton4 = Button(ventanta, text='4', width=5, height=2, command= lambda: click_boton(4))
boton5 = Button(ventanta, text='5', width=5, height=2, command= lambda: click_boton(5))
boton6 = Button(ventanta, text='6', width=5, height=2, command= lambda: click_boton(6))
boton7 = Button(ventanta, text='7', width=5, height=2, command= lambda: click_boton(7))
boton8 = Button(ventanta, text='8', width=5, height=2, command= lambda: click_boton(8))
boton9 = Button(ventanta, text='9', width=5, height=2, command= lambda: click_boton(9))
boton0 = Button(ventanta, text='0', width=13, height=2, command= lambda: click_boton(0))

#Operadores
boton_borrar = Button(ventanta, text='AC', width=5, height=2, command= lambda: borrar())
boton_parentesis1 = Button(ventanta, text='(', width=5, height=2, command= lambda: click_boton("("))
boton_parentesis2 = Button(ventanta, text=')', width=5, height=2, command= lambda: click_boton(")"))
boton_punto = Button(ventanta, text='.', width=5, height=2, command= lambda: click_boton("."))
boton_div = Button(ventanta, text='/', width=5, height=2, command= lambda: click_boton("/"))
boton_mult = Button(ventanta, text='*', width=5, height=2, command= lambda: click_boton("*"))
boton_suma = Button(ventanta, text='+', width=5, height=2, command= lambda: click_boton("+"))
boton_resta = Button(ventanta, text='-', width=5, height=2, command= lambda: click_boton("-"))
boton_igual = Button(ventanta, text='=', width=5, height=2, command= lambda: hacer_operaciones())


#lineas 1
boton_borrar.grid(row= 1,column=0, padx=5, pady=5)
boton_parentesis1.grid(row= 1,column=1, padx=5, pady=5)
boton_parentesis2.grid(row= 1,column=2, padx=5, pady=5)
boton_div.grid(row= 1,column=3, padx=5, pady=5)

#linea 2
boton7.grid(row= 2,column=0, padx=5, pady=5)
boton8.grid(row= 2,column=1, padx=5, pady=5)
boton9.grid(row= 2,column=2, padx=5, pady=5)
boton_mult.grid(row= 2,column=3, padx=5, pady=5)

#linea 3
boton4.grid(row= 3,column=0, padx=5, pady=5)
boton5.grid(row= 3,column=1, padx=5, pady=5)
boton6.grid(row= 3,column=2, padx=5, pady=5)
boton_suma.grid(row= 3,column=3, padx=5, pady=5)

#linea 4
boton1.grid(row= 4,column=0, padx=5, pady=5)
boton2.grid(row= 4,column=1, padx=5, pady=5)
boton3.grid(row= 4,column=2, padx=5, pady=5)
boton_resta.grid(row= 4,column=3, padx=5, pady=5)

#linea 5
boton0.grid(row= 5,column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row= 5,column=2,  padx=5, pady=5)
boton_igual.grid(row= 5,column=3,  padx=5, pady=5)






ventanta.mainloop()