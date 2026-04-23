"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213022_760
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
#Bienvenida
print("Bienvenido al sistema administrativo de su conjunto residencial")

#Solicitudes al Administrador la cantidad de vecinos a revisar
while True:
    try:
        cantidad_vecinos= int(input("Administrador, ingrese la cantidad de vecinos: "))
        if cantidad_vecinos>0:
            break
    except:
        print("Vuele a intentarlo, por favor.")
        
#Solicitar al aAdministrador el valor de la cuota por residente
while True:
    try:
        valor_residente= int(input("Administrador, ingrese el valor a pagar por cada uno de los residentes: "))
        if valor_residente >0:
            break
    except:
        print("Vuele a intentarlo, por favor.")
        
#Contadores
vecinos_cumplidos=0
vecinos_morosos=0
total_adeudado=0

#Registro de cada vecino
for vecino in range(cantidad_vecinos):
    #Solicitar la cantidad de residentes en la unidad
    while True:
        try:
            cantidad_residentes=int(input("Vecino, ingrese la cantidad de residentes en su unidad residencial: "))
            if cantidad_residentes>0:
                break
        except:
            print("Vuele a intentarlo, por favor.")
    #Determina el valor de la cuota
    valor_cuota=valor_residente*cantidad_residentes
    #Estado de cuenta
    while True:
        pagado=str(input(f"Vecino, su cuota es de ${valor_cuota} pesos.\n¿Ya pagó? si o no: "))
        normalizado=pagado.strip().lower()
        if normalizado in ["si","no"]:
            break
        else:
            print("Vuele a intentarlo, por favor.")
    #Proceso suma a contadores
    if normalizado=="si":
        vecinos_cumplidos+=1
    elif normalizado=="no":
        vecinos_morosos+=1
        total_adeudado+=valor_cuota

print(f"{vecinos_cumplidos} Vecinos se encuentran al día")
print(f"{vecinos_morosos} Vecinos son morosos")
print(f"El total adeudado por los vecinos morosos es de ${total_adeudado}")