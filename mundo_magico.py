"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213022_760
Programa: Ingenieria de Sistmeas
Codigo fuente: autoria propia
"""
#Bienvenida 
print("Bienvenido a la juguetería Mundo Magico, realizamos envios nacionales como parte de nuestra campaña Sonrisas por correo.")

#Solicitar la cantidad de de payasos
while True:
    try:
        payasos= int(input("Para conocer el peso total de su pedido, ingrese la cantidad de payasos de tela que desea ordenar: "))
        if payasos>0:
            break
    except:
        print("Vuele a intentarlo, por favor.")
        
#Solicitar la cantidad de muñecas
while True:
    try:
        munecas= int(input("Ingrese la cantidad de muñecas clásica que desea ordenar: "))
        if munecas > 0:
            break
    except:
        print("Vuelve a intentarlo, por favor.")
        
#Calcular el peso total.
peso_payasos= payasos*112
peso_munecas= munecas*75
peso_total = peso_payasos + peso_munecas
print( f"El peso total de su pedido es {peso_total} gramos")       
