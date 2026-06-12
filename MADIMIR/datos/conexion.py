import pyodbc


def conectar():

    conexion = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=DESKTOP-7G48LTN;"
        "DATABASE=MADIMIR;"
        "Trusted_Connection=yes;"
    )

    return conexion