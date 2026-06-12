from tkinter import *
from datos.almacenamiento import pedidos

def abrir_consultas():

    ventana = Toplevel()
    ventana.title("Consultar Pedidos")
    ventana.geometry("800x600")
    ventana.configure(bg="#121212")

    Label(
        ventana,
        text="CONSULTA DE PEDIDOS",
        font=("Arial", 20, "bold"),
        fg="#D4AF37",
        bg="#121212"
    ).pack(pady=20)

    lista = Listbox(
        ventana,
        width=90,
        height=20,
        bg="#1E1E1E",
        fg="white",
        font=("Arial", 10)
    )

    lista.pack(pady=20)

    if len(pedidos) == 0:

        lista.insert(
            END,
            "No hay pedidos registrados"
        )

    else:

        for p in pedidos:

            lista.insert(
                END,
                f"Cliente: {p['cliente']} | Producto: {p['producto']} | Cantidad: {p['cantidad']}"
            )