from tkinter import *
from presentacion.productos import abrir_productos
from presentacion.pedidos import abrir_pedidos
from presentacion.consultas import abrir_consultas

# Crear ventana
ventana = Tk()
ventana.title("MADIMIR - Gourmet Restaurant")
ventana.geometry("1000x700")
ventana.configure(bg="#121212")
ventana.resizable(False, False)

# Título principal
titulo = Label(
    ventana,
    text="MADIMIR",
    font=("Times New Roman", 36, "bold"),
    fg="#D4AF37",
    bg="#121212"
)
titulo.pack(pady=(60, 10))

# Subtítulo
subtitulo = Label(
    ventana,
    text="GOURMET RESTAURANT",
    font=("Arial", 14),
    fg="white",
    bg="#121212"
)
subtitulo.pack(pady=(0, 50))

# Marco para botones
frame_botones = Frame(
    ventana,
    bg="#121212"
)
frame_botones.pack()

# Funciones temporales
def productos():
    print("Ventana Productos")

def pedidos():
    print("Ventana Pedidos")

def consultar():
    print("Ventana Consultar")

# Estilo botones
def crear_boton(texto, comando):
    return Button(
        frame_botones,
        text=texto,
        command=comando,
        font=("Arial", 14, "bold"),
        bg="#D4AF37",
        fg="black",
        width=25,
        height=2,
        cursor="hand2",
        relief="flat"
    )

# Botones
btn_productos = crear_boton("PRODUCTOS", abrir_productos)
btn_productos.pack(pady=15)

btn_pedidos = crear_boton("PEDIDOS", abrir_pedidos)
btn_pedidos.pack(pady=15)

btn_consultar = crear_boton(
    "CONSULTAR PEDIDOS",
    abrir_consultas
)
btn_consultar.pack(pady=15)

btn_salir = crear_boton("SALIR", ventana.destroy)
btn_salir.pack(pady=15)

# Pie de página
footer = Label(
    ventana,
    text="Sistema de Gestión de Pedidos",
    font=("Arial", 10),
    fg="gray",
    bg="#121212"
)
footer.pack(side=BOTTOM, pady=20)

ventana.mainloop()