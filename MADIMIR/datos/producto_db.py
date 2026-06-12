from datos.conexion import conectar

def guardar_producto_bd(nombre, precio, categoria):

    print("ENTRÓ A guardar_producto_bd")

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO productos
        (nombre, precio, categoria)
        VALUES (?, ?, ?)
        """,
        (nombre, precio, categoria)
    )

    conexion.commit()

    print("PRODUCTO GUARDADO EN SQL SERVER")

    conexion.close()