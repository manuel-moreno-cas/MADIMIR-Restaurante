from tkinter import *
from datos.almacenamiento import pedidos
from datos.pedido_db import guardar_pedido_bd

def abrir_pedidos():

    def registrar_pedido():

        cliente = entry_cliente.get()
        producto = entry_producto.get()
        cantidad = entry_cantidad.get()

        if cliente == "" or producto == "" or cantidad == "":
            print("Complete todos los campos")
            return

        try:
            cantidad_num = int(cantidad)
        except:
            print("Cantidad inválida")
            return

        total = cantidad_num * 25000

        pedido = {
            "cliente": cliente,
            "producto": producto,
            "cantidad": cantidad_num,
            "total": total
        }

        pedidos.append(pedido)
        guardar_pedido_bd(
            cliente,
            producto,
            cantidad_num,
            total
        )

        lista_pedidos.insert(
            END,
            f"{cliente} | {producto} | Cant: {cantidad_num} | Total: ${total}"
        )

        factura.config(
            text=
            f"""
FACTURA

Cliente: {cliente}

Producto: {producto}

Cantidad: {cantidad_num}

TOTAL: ${total}

Gracias por preferir MADIMIR
"""
        )

        entry_cliente.delete(0, END)
        entry_producto.delete(0, END)
        entry_cantidad.delete(0, END)

    ventana = Toplevel()

    ventana.title("Pedidos")
    ventana.geometry("800x700")
    ventana.configure(bg="#121212")

    Label(
        ventana,
        text="GESTIÓN DE PEDIDOS",
        font=("Arial",20,"bold"),
        fg="#D4AF37",
        bg="#121212"
    ).pack(pady=20)

    Label(
        ventana,
        text="Cliente",
        fg="white",
        bg="#121212"
    ).pack()

    entry_cliente = Entry(
        ventana,
        width=40
    )
    entry_cliente.pack(pady=10)

    Label(
        ventana,
        text="Producto",
        fg="white",
        bg="#121212"
    ).pack()

    entry_producto = Entry(
        ventana,
        width=40
    )
    entry_producto.pack(pady=10)

    Label(
        ventana,
        text="Cantidad",
        fg="white",
        bg="#121212"
    ).pack()

    entry_cantidad = Entry(
        ventana,
        width=40
    )
    entry_cantidad.pack(pady=10)

    Button(
        ventana,
        text="GENERAR FACTURA",
        command=registrar_pedido,
        bg="#D4AF37",
        fg="black",
        width=20
    ).pack(pady=20)

    lista_pedidos = Listbox(
        ventana,
        width=80,
        height=6,
        bg="#1E1E1E",
        fg="white"
    )

    lista_pedidos.pack()

    factura = Label(
        ventana,
        text="",
        justify=LEFT,
        fg="white",
        bg="#121212",
        font=("Arial",11)
    )

    factura.pack(pady=20)