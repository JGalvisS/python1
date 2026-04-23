"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213022_760
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
#Bienvenida
print("Bienvenido a la heladería de la fiesta de Pepito")
#Solicitar el dinero disponible
while True:
    try:
        dinero_disponible=int(input("¿Cuanto dinero tienes disponible?"))
        if dinero_disponible>0:
            break
    except:
        print("Vuelve a intentarlo, por favor.")
#Listas de compra
helados=["vaso de Helado","choco cono","paleta Drácula","polet","platillo"]
precios=[2500,2000,3800,4500,1800]
#Contadores
cantidad_helados=0
tipo_helados_comprados=[0,0,0,0,0]
dinero_gastado=0
dinero_gastado_por_helado=[0,0,0,0,0]
valor_promedio=0
#Solitar el helado deseado
while dinero_disponible>0:
    while True:
        try:
            helado=int(input(f"""   CARTA DE HELADOS
1- {helados[0]}         ${precios[0]}
2- {helados[1]}             ${precios[1]}
3- {helados[2]}         ${precios[2]}
4- {helados[3]}                  ${precios[3]}
5- {helados[4]}               ${precios[4]}
6- Dejar de comprar
Actualmente el dinero que tiene disponible es de ${dinero_disponible} pesos.
Selecciona el helado que te gustaria comprar: """))
            if helado>0 and helado<=6:
                break
        except:
            print("Vuele a intentarlo, por favor.")
    #Falta de fondos
    if dinero_disponible<1799:
        print(f"Actualmente el dinero que tiene disponible es de ${dinero_disponible} pesos. No es suficiente dinero para ningun helado.")
        break
    #Procesamiento del helado
    match helado:
        case 1:
            if dinero_disponible>=precios[0]:
                dinero_disponible-=precios[0]
                cantidad_helados+=1
                tipo_helados_comprados[0]+=1
                dinero_gastado+=precios[0]
                dinero_gastado_por_helado[0]+=precios[0]
            else:
                print("No hay dinero suficiente para comprar este helado.")
        case 2:
            if dinero_disponible>=precios[1]:
                dinero_disponible-=precios[1]
                cantidad_helados+=1
                tipo_helados_comprados[1]+=1
                dinero_gastado+=precios[1]
                dinero_gastado_por_helado[1]+=precios[1]
            else:
                print("No hay dinero suficiente para comprar este helado.")
        case 3:
            if dinero_disponible>=precios[2]:
                dinero_disponible-=precios[2]
                cantidad_helados+=1
                tipo_helados_comprados[2]+=1
                dinero_gastado+=precios[2]
                dinero_gastado_por_helado[2]+=precios[2]
            else:
                print("No hay dinero suficiente para comprar este helado.")
        case 4:
            if dinero_disponible>=precios[3]:
                dinero_disponible-=precios[3]
                cantidad_helados+=1
                tipo_helados_comprados[3]+=1
                dinero_gastado+=precios[3]
                dinero_gastado_por_helado[3]+=precios[3]
            else:
                print("No hay dinero suficiente para comprar este helado.")
        case 5:
            if dinero_disponible>=precios[4]:
                dinero_disponible-=precios[4]
                cantidad_helados+=1
                tipo_helados_comprados[4]+=1
                dinero_gastado+=precios[4]
                dinero_gastado_por_helado[4]+=precios[4]
            else:
                print("No hay dinero suficiente para comprar este helado.")
        case 6:
            break
#Promedio 
if cantidad_helados>0:            
    valor_promedio=dinero_gastado//cantidad_helados
#Resumen por pantalla        
print(f"""  RESUMEN DE COMPRA
Helados comprados:
{tipo_helados_comprados[0]} {helados[0]} ${dinero_gastado_por_helado[0]}
{tipo_helados_comprados[1]} {helados[1]}     ${dinero_gastado_por_helado[1]}
{tipo_helados_comprados[2]} {helados[2]} ${dinero_gastado_por_helado[2]}
{tipo_helados_comprados[3]} {helados[3]}          ${dinero_gastado_por_helado[3]}
{tipo_helados_comprados[4]} {helados[4]}       ${dinero_gastado_por_helado[4]}
Para un tota de ${dinero_gastado} pesos.
Total de helados comprados:  {cantidad_helados}.
Valor promedio de los helado ${valor_promedio} pesos.
Dinero sobrante ${dinero_disponible} pesos.""")            