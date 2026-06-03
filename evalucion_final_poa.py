"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213022_760
Programa: Ingenieria de Sistemas
Codigo fuente: UNAD, adaptacion del estudiante.
"""
MATRIZ = [
    ["A001","destornillador",10,19],
    ["A002","martillo",6,10],
    ["A003","bisturi",22,15],
    ["A004","alicate",10,10],
    ["A005","flexometro",25,15],
    ["A006","taladro",3,10]
]
def socilitar_articulos():
    productos = []
    for i in MATRIZ:
        stock_actual = i[2]
        stock_minimo = i[3]
        if stock_actual < stock_minimo:
            faltante = stock_minimo - stock_actual
        if stock_actual >= stock_minimo:
            faltante = 0
        pedido = [faltante,i[1]]
        productos.append(pedido)
    for i in productos:
        print(f""" {i[0]}            {i[1]} """)
print("""_______________________________
    SOLICITUD DE ARTICULOS 
________________________________                     
CANTIDAD      ARTICULO""")
socilitar_articulos()