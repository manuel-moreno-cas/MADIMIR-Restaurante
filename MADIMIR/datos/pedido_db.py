from datos.conexion import conectar

def guardar_pedido_bd(cliente, producto, cantidad, total):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO pedidos
        (cliente, producto, cantidad, total)

        VALUES (?, ?, ?, ?)
        """,
        (
            cliente,
            producto,
            cantidad,
            total
        )
    )

    conexion.commit()

    print("PEDIDO GUARDADO EN SQL SERVER")

    conexion.close()