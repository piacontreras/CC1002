import random
from Tkinter import *
import sys
import csv


ventana =Tk()
ventana.title ("El ahorcado")
frameprincipal=Frame(ventana)
frameprincipal.pack()


canvas=Canvas(ventana, width=600, height=600, bg="white")
canvas.create_rectangle(100, 50, 150, 600, fill="green")
canvas.create_rectangle(100,50, 400, 60, fill="green")
canvas.create_rectangle(395, 50, 405, 100, fill="green")
canvas.pack()

#dibujo_muneco: num(0-4)->dibujo
#permite que a medida que se vaya cumpliendo ciertas condiciones
#se vaya dibujando el ahorcado
#ejemplo:dibujo_muneco(4) debería dibujar la cabeza
def dibujo_muneco(x):
    if x==4:
        canvas.create_oval(350, 100, 450, 200, fill="red")
    if x==3:
        canvas.create_line(320, 240, 480, 240, fill="black")
    if x==2:
        canvas.create_line(400, 200, 400, 330, fill="black")
    if x==1:
        canvas.create_line(400, 330, 340, 400, fill="black")
    if x==0:
        canvas.create_line(400, 330, 460, 400, fill="black")
    return
    
        
listaPalabras=[0]*10
p=0
palabra= open("palabras.txt")
linea=csv.reader(palabra, delimiter=" ")
p=palabra.read()
e=random.choice(p)
for fila in linea:
    listaPalabras[0]=fila[0]
    p+=1
    random.choice(listaPalabra)
    i=[0]
    for i in range(0, len(listaPalabras)):
        print listaPalabras[i]
cantidad=len(e)
palabra.close()

listaPalabras=["laberinto", "cocodrilo", "nandu", "zapatilla", "bicicleta", "armadillo", "aconcagua", "sencillo", "zorzal", "compromiso"]
palabraElegida=random.choice(listaPalabras)
tupalabra=""
vidas=5
print palabraElegida
print len(palabraElegida)
print [palabraElegida]

i=0
while i<len(palabraElegida):
    letra=palabraElegida[i]
    i=i+1
    print letra
cantidad=len(palabraElegida)

#ayuda al momento de poder ingresar la letra
def letras(x):
    letra=texto.get()
    letrasJugadas.config(text=letra)
    return

#rayitas:str->"_"
#rayitas crea la cantidad de lineas por letra de cada palabraElegida(al azar)
#ejemplo:rayitas(nandu) debería devolver _ _ _ _ _
def rayitas():
    return "_"*cantidad

#permite comenzar el juego de nuevo
def jugarDeNuevo():
    etiqueta.config(text="")
    return

for letra in palabraElegida:
    if(letra in palabraElegida==True):
        letra in rayitas
    else:
        vidas-=1
        dibujo_muneco(vidas)
        

titulo=Label(frameprincipal, text="El ahorcado")
titulo.pack(side=LEFT)

etiqueta=Label(ventana, text="Ingrese letra:")
etiqueta.pack()

texto=StringVar()
letra=Entry(ventana, textvariable=texto)
letra.bind("<Return>", letras)
letra.pack()

Palabra=Label(ventana, text="Palabra: "+ rayitas())
Palabra.pack()

letrasJugadas=Label(ventana, text="Letras Jugadas: ")
letrasJugadas.pack()

LetrasJugadas=Label(ventana)
LetrasJugadas.pack()

boton=Button(frameprincipal, text="Empezar de nuevo", command=jugarDeNuevo)
boton.pack()


ventana.mainloop()
