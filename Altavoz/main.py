bandas=[]

opcion=None

while(opcion != 5):
    print("***FESTIVAL ALTAVOZ***")
    print("***********************")
    print("1.Registrar Banda")
    print("2.Ver el cartel del festival")
    print("3.Buscar Banda")
    print("4.Modificar Banda")
    print("5.Finalizar")

    opcion=int(input("Digita una opcion: "))
    if opcion == 1:
        banda={}
        #Se llena el objeto de banda 
        banda["id"]=int(input("Digite el id: "))
        banda["nombre"]=input("Nombre: ")
        banda["genero"]=input("Genero:")
        banda["costo"]=int(input("Costo: "))
        banda["Clasificacion"]=input("Clasificacion: ")
       
       #Como agrego un  diccionario a una lista
        bandas.append(banda)
        
    elif opcion == 2:

        #Recorriendo una lista para imprimir sus elementos
        for bandaAuxiliar in bandas:
            print(f"{bandaAuxiliar["id"]}--{bandaAuxiliar["nombre"]}")
        
    elif opcion == 3:
        
        #Buscando un elemento dentro de una lista
        BandaBuscada=input("Digita la banda que quieres buscar: ")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"]== BandaBuscada:
                print("oe la encontre")
            else:
                print("no lo encontraste")
    elif opcion == 4:
        pass
    elif opcion ==5:
        pass
    else:
        print("Opcion invalida")

