from claseFunciones import Funciones
from tkinter import *

root = Tk()
root.title("Calculadora")
root.resizable(0,0)
root.geometry("459x495+700+250")
root.config(background='#7A89C9')
var1 = Entry(root)
var1.grid(row=0,column=0,padx=0,pady=0,ipady=15)
var1.grid(row=1, columnspan=6, sticky=W+E)
var1.config(font=("Calibri 16"), justify='right', borderwidth=5)

funciones= Funciones(var1) # Instancia de la clase

# Botones de los números y signos

Button(root, text="1", width=15, height=5, command=lambda:funciones.operacion("1")).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", width=15, height=5, command=lambda:funciones.operacion("2")).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", width=15, height=5, command=lambda:funciones.operacion("3")).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", width=15, height=5, command=lambda:funciones.operacion("4")).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", width=15, height=5, command=lambda:funciones.operacion("5")).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", width=15, height=5, command=lambda:funciones.operacion("6")).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", width=15, height=5, command=lambda:funciones.operacion("7")).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", width=15, height=5, command=lambda:funciones.operacion("8")).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", width=15, height=5, command=lambda:funciones.operacion("9")).grid(row=4, column=2, sticky=W+E)

Button(root, text="AC", width=15, height=5, command=lambda:funciones.limpiar(2)).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", width=15, height=5, command=lambda:funciones.operacion("0")).grid(row=5, column=1, sticky=W+E)
Button(root, text="←", width=15, height=5, command=lambda:funciones.undo()).grid(row=5, column=2, sticky=W+E)

Button(root, text="+", width=15, height=5, command=lambda:funciones.operacion("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", width=15, height=5, command=lambda:funciones.operacion("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="/", width=15, height=5, command=lambda:funciones.operacion("/")).grid(row=4, column=3, sticky=W+E)
Button(root, text="*", width=15, height=5, command=lambda:funciones.operacion("*")).grid(row=5, column=3, sticky=W+E)

Button(root, text="=", width=15, height=5, command=lambda:funciones.operacion("=")).grid(row=6, columnspan=6, sticky=W+E)

root.mainloop()
