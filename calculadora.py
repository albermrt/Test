from tkinter import * #importamos toda la librería de interfaz de usuario

root = Tk()   
root.title('CALCULADORA!!!!')

e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

sumando=0
memory=0

def button_add(number):
    current=e.get()     # Guarda el número actual en el cuadro de dialogo
    e.delete(0,END)     # Borra el cuadro de diálogo
    e.insert(0,str(current) + str(number))  # inserta la concatenación del nuevo número que hemos pulsado más todo lo anterior
    return

def button_suma():
    global sumando #actúa sobre las variables globales
    sumando=e.get()
    e.delete(0,END)
    return 

def button_equal():
    sumando2=e.get()
    global memory
    e.delete(0,END)
    e.insert(0,int(sumando2)+int(sumando)+int(memory))
    memory2=int(sumando2)+int(sumando)+int(memory)
    memory=memory2
    return

def button_BORRAR():
    e.delete(0,END)
    global memory
    memory=0
    return

#definir botones
boton1=Button(root,text='1',padx=40,pady=20,command=lambda: button_add(1))
boton2=Button(root,text='2',padx=40,pady=20,command=lambda: button_add(2))
boton3=Button(root,text='3',padx=40,pady=20,command=lambda: button_add(3))
boton4=Button(root,text='4',padx=40,pady=20,command=lambda: button_add(4))
boton5=Button(root,text='5',padx=40,pady=20,command=lambda: button_add(5))
boton6=Button(root,text='6',padx=40,pady=20,command=lambda: button_add(6))
boton7=Button(root,text='7',padx=40,pady=20,command=lambda: button_add(7))
boton8=Button(root,text='8',padx=40,pady=20,command=lambda: button_add(8))
boton9=Button(root,text='9',padx=40,pady=20,command=lambda: button_add(9))
boton0=Button(root,text='0',padx=40,pady=20,command=lambda: button_add(0))
botonsuma=Button(root,text='+',padx=40,pady=20,command=button_suma)
botonigual=Button(root,text='=',padx=101,pady=20,command=button_equal)
botonlimpiar=Button(root,text='BORRAR',padx=87,pady=20,command=lambda: button_BORRAR())

#poner los botones en la ventana

boton1.grid(row=3, column=0)
boton2.grid(row=3, column=1)
boton3.grid(row=3, column=2)

boton4.grid(row=2, column=0)
boton5.grid(row=2, column=1)
boton6.grid(row=2, column=2)

boton7.grid(row=1, column=0)
boton8.grid(row=1, column=1)
boton9.grid(row=1, column=2)

boton0.grid(row=4, column=0)

botonsuma.grid(row=5, column=0)
botonigual.grid(row=5, column=1, columnspan=2)
botonlimpiar.grid(row=4, column=1, columnspan=2)



root.mainloop()