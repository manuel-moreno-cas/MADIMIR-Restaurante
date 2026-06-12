from tkinter import *
from datos.conexion import conectar

def abrir_consultas():

    ventana = Toplevel()
    ventana.title("Consultar Pedidos")
    ventana.geometry("900x600")
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
        width=120,
        height=20,
        bg="#1E1E1E",
        fg="white",
        font=("Arial", 10)
    )

    lista.pack(pady=20)

    try:

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT id_pedido,
                   cliente,
                   producto,
                   cantidad,
                   total
            FROM pedidos
        """)

        pedidos = cursor.fetchall()

        if len(pedidos) == 0:

            lista.insert(
                END,
                "No hay pedidos registrados"
            )

        else:

            for pedido in pedidos:

                lista.insert(
                    END,
                    f"Pedido #{pedido[0]} | Cliente: {pedido[1]} | Producto: {pedido[2]} | Cantidad: {pedido[3]} | Total: ${pedido[4]}"
                )

        conexion.close()

    except Exception as e:

        lista.insert(
            END,
            f"Error al consultar: {e}"
        )