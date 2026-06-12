import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera interfaz")

texto = tk.Label(ventana, text="Hola Mundo")
texto.pack()

boton = tk.Button(ventana, text="Aceptar")
boton.pack()

ventana.mainloop()