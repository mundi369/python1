from cProfile import label
from cgitb import text
import tkinter
from tkinter import* 
from tkinter import messagebox
import pymysql
import customtkinter

def menu_pantalla():
  global pantalla
  pantalla = Tk()
  pantalla.geometry("400x300")
  pantalla.title("Bienvenido")
  image=PhotoImage(file ="./imagen1/icono.gif")
  image=image.subsample(2,2)
  label1= Label(image=image)
  label1.pack()

  Label(text="acceso al sistema", bg="navy" , fg="white", width="300", height="3",font=("calibrí",15)).pack()
  Label(text="").pack()

  Button(text="iniciar secion", height="2", width="30",command=inicio_secion).pack()
  Label(text="").pack()

  Button(text="registrarse", height="2", width="30").pack()

  pantalla.mainloop()

def inicio_secion():
  global pantalla1
  pantalla1 = Toplevel(pantalla)
  pantalla1.geometry("400x 250")
  pantalla1.title("inicio de secion")


  Label(pantalla1, text= "por favor ingrese usiario y contraseña").pack()
  Label(pantalla1, text= "").pack()
 
  global nombreusuario_verify
  global contraseña_usuario_verify

  nombreusuario_verify= StringVar()
  contraseña_usuario_verify= StringVar()
  

  global nombre_usuario_entry
  global contraseña_usuario_entry

  Label(pantalla1, text="Usuario").pack()
  nombre_usuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
  nombre_usuario_entry.pack()
  Label(pantalla1).pack()

  Label(pantalla1, text="contraseña").pack()
  contraseña_usuario_entry = Entry(pantalla1, textvariable=contraseña_usuario_verify)
  contraseña_usuario_entry.pack()
  Label(pantalla1).pack()
  Button(pantalla1, text="Iniciar sesion").pack()



menu_pantalla()  
  
  

  
  



