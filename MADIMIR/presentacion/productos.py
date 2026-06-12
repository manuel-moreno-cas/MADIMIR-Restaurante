from tkinter import *
from datos.almacenamiento import productos
from datos.producto_db import guardar_producto_bd

def abrir_productos():

    def guardar_producto():

        nombre = entry_nombre.get()
        precio = entry_precio.get()
        categoria = entry_categoria.get()

        if nombre == "" or precio == "" or categoria == "":
            print("Complete todos los campos")
            return

        producto = {
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria
        }

        productos.append(producto)
        guardar_producto_bd(
            nombre,
            precio,
            categoria
        )

        lista_productos.insert(
            END,
            f"{nombre} - ${precio} - {categoria}"
        )

        print("\nPRODUCTOS REGISTRADOS:")
        for p in productos:
            print(p)

        # Limpiar campos
        entry_nombre.delete(0, END)
        entry_precio.delete(0, END)
        entry_categoria.delete(0, END)

    ventana = Toplevel()
    ventana.title("Productos")
    ventana.geometry("700x600")
    ventana.configure(bg="#121212")

    Label(
        ventana,
        text="GESTIÓN DE PRODUCTOS",
        font=("Arial", 20, "bold"),
        fg="#D4AF37",
        bg="#121212"
    ).pack(pady=20)

    Label(
        ventana,
        text="Nombre del producto",
        fg="white",
        bg="#121212"
    ).pack()

    entry_nombre = Entry(
        ventana,
        width=40
    )
    entry_nombre.pack(pady=10)

    Label(
        ventana,
        text="Precio",
        fg="white",
        bg="#121212"
    ).pack()

    entry_precio = Entry(
        ventana,
        width=40
    )
    entry_precio.pack(pady=10)

    Label(
        ventana,
        text="Categoría",
        fg="white",
        bg="#121212"
    ).pack()

    entry_categoria = Entry(
        ventana,
        width=40
    )
    entry_categoria.pack(pady=10)

    Button(
        ventana,
        text="Guardar",
        command=guardar_producto,
        bg="#D4AF37",
        fg="black",
        width=15
    ).pack(pady=20)

    Label(
        ventana,
        text="Productos Registrados",
        fg="#D4AF37",
        bg="#121212",
        font=("Arial", 12, "bold")
    ).pack(pady=(20, 5))

    lista_productos = Listbox(
        ventana,
        width=60,
        height=8,
        bg="#1E1E1E",
        fg="white"
    )
    lista_productos.pack()