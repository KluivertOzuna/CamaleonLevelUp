import tkinter#libreria util para la GUI
import random
#ventana
ventana = tkinter.Tk()
ventana.geometry("700x350")
ventana.title("Camaleón :)") 
colors = ["green","yellow","gray","blue","cyan","purple","white"]
#funcion
def changeColor():
 #ventana.config(background="black")
 randomcolors = random.choice(colors)
 ventana.config(background=randomcolors)
 clr = tkinter.Label(ventana,text = randomcolors, font = "cambria 25", width=6, height=2,fg="white",bg="gray" )
 clr.place(x = 490,y = 40)
#boton y Etiqueta
background = tkinter.Label(ventana,text= "Background Color:",font = "italic 25", width=25, height=2, fg="white", bg="gray")
background.place(x = 120, y = 40)
boton = tkinter.Button(ventana, text = "Click me!",width=25, height=2, command = changeColor)
boton.place(x = 300, y = 200)

ventana.mainloop()