"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213022_760
Programa: Ingenieria de Sistemas
Codigo fuente: UNAD, adaptacion del estudiante.
"""
VENTAS_POR_MES = {"enero": 1500, "febrero": 2200, "marzo": 1800}
LIMITE_BONO = 5000
#Solicita nombre, mes actual y una cantidad vendida para almacenamiento.
def solicitar_datos():
    """Solicita un nombre, mes actual y una cantidad vendida."""
    nombre_vendedor = input("Ingrese su nombre: ")
    try:
        mes_actual=input("Ingrese el mes actulal: ")
        cantidad_nueva = int(input(f"Ingrese las ventas de {mes_actual}: "))
    except:
        print("Entrada inválida, usando 0.")
        cantidad_nueva = 0
    return nombre_vendedor, cantidad_nueva, mes_actual
#Agrega la venta al diccionario de ventas y lo devuelve actualiazado
def agregar_ventas(datos_actuales, mes, monto):
    """Agrega un nuevo mes de ventas al diccionario."""
    datos_actuales[mes] = monto
    return list(datos_actuales.values())
#Revisa si las ventas totales son suficientes para el bono y calcula su valor si es así.
def revisar_bono(ventas_totales, limite, nuevas_ventas):
    """Verifica si el vendedor califica para un bono."""
    numero_meses = len(VENTAS_POR_MES_NUEVO)
    promedio_ventas = ventas_totales / numero_meses
    if promedio_ventas >= limite:
        monto_bono = int(nuevas_ventas * 0.30)
        print(f"""________________________________________________________________
        ¡Felicidades! Ganaste un bono de: {monto_bono}
________________________________________________________________""")
    else:
        print("Siga esforzándose para el bono.")
#Imprime resumen por pantalla.        
while True:
    try:
        vendedor, nuevas_ventas, mes_actual = solicitar_datos()
        VENTAS_POR_MES_NUEVO = agregar_ventas(VENTAS_POR_MES, mes_actual, nuevas_ventas)
        total_anual = sum(VENTAS_POR_MES_NUEVO)
        revisar_bono(total_anual, LIMITE_BONO, nuevas_ventas) #linea corregida: nombre de variable LIMITE_BONO_INCORRECTO
        print(f"RESUMEN DE VENTAS:\nVendedor: {vendedor}")
        for mes, ventas in VENTAS_POR_MES.items():
            print(f"Ventas de {mes}: {ventas}")
        print(f"Total ventas anual: {total_anual}")
        break
    except Exception as e:
        print("Ocurrió un problema, intentando de nuevo.")