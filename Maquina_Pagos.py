print("Arriendo Estacionamientos 🚗\n")

fondo_cambios = 40000

registro_ventas = 0
registro_descuento = 0

vehiculo1 = "Auto"
vehiculo2 = "Camioneta"
vehiculo3 = "Camión"
vehiculo4 = "Motocicleta"

costo_vehiculo1 = 2000
costo_vehiculo2 = 3000
costo_vehiculo3 = 4000
costo_vehiculo4 = 890

correo = ""
ingreso_dinero = 0
vuelto = 0
dinero_acumulado = 0

seleccion_vehiculo = 1
vehiculo_seleccionado = ""
costo_vehiculo_seleccionado = 0


descuento_A = 0.99 # 100% - 1%

descuento_E = 1.01 # 100% + 1%

descuento_i = 0.94 # 100% - 6%

descuento_O = 1.002 # 100% + 0.2%

descuento_U = 0.995 # 100% - 0.5%

descuento_B = 0.993 # 100% - 0.7%

descuento_L = 1.002 # 100% + 0.2%

descuento_M = 0.987 # 100% - 1.3%

descuento_X = 0.98 # 100% - 2%

descuento_Y = 0.979 # 100% - 2.1%

descuento_Z = 0.997 # 100% - 0.3%

descuento_punto = 1.01 # 100% + 1%






while True:
    correo = input("Ingresa tu correo >> ")

    if correo == "3312":
        print("\n**************************************************")
        print("Cierre completado. \n")
        print(f"TOTAL DINERO RECAUDADO: {registro_ventas}")
        print(f"FONDOS PARA CAMBIOS: {fondo_cambios} \n")
        print("**************************************************")
        break

    elif len(correo) < 8 or len(correo) > 30:
        print("Ingresa un correo que contenga entre 8 y 30 caracteres.\n")

    else: print(f"Correo Registrado. {correo}")
    

    print(f"""Listado de Vehiculos
        
            1.{vehiculo1} ---> {costo_vehiculo1}
            2.{vehiculo2} ---> {costo_vehiculo2}
            3.{vehiculo3} ---> {costo_vehiculo3}
            4.{vehiculo4} ---> {costo_vehiculo4} \n""")

    try:
        while seleccion_vehiculo > 0 or seleccion_vehiculo < 6:
            seleccion_vehiculo = int(input("Selecciona vehiculo indicando su número. \n >> "))
                                        

            if seleccion_vehiculo == 1:
                vehiculo_seleccionado = vehiculo1
                costo_vehiculo_seleccionado = costo_vehiculo1

            elif seleccion_vehiculo == 2:
                vehiculo_seleccionado = vehiculo2
                costo_vehiculo_seleccionado = costo_vehiculo2

            elif seleccion_vehiculo == 3:
                vehiculo_seleccionado = vehiculo3
                costo_vehiculo_seleccionado = costo_vehiculo3

            elif seleccion_vehiculo == 4:
                vehiculo_seleccionado = vehiculo4
                costo_vehiculo_seleccionado = costo_vehiculo4


            elif seleccion_vehiculo > 4 or seleccion_vehiculo < 1:
                print("Selecciona el número correspondiente. \n")
                continue


            print(f"Vehiculo seleccionado: {vehiculo_seleccionado}")
            break
    except ValueError: print("Ha ocurrido un error de caracteres, intenta nuevamente.")



#descuento_A = 0.99 (99%) # 100% - 1%
#descuento_E = 1.01 (101%) # 100% + 1%
#descuento_i = 0.94 (94%) # 100% - 6%
#descuento_O = 1.002 (100,2%) # 100% + 0.2%
#descuento_U = 0.995 (99,5%) # 100% - 0.5%
#descuento_B = 0.993 (99,3%) # 100% - 0.7%
#descuento_L = 1.002 (100,2%) # 100% + 0.2%
#descuento_M = 0.987 (98,7%) # 100% - 1.3%
#descuento_X = 0.98 (98%) # 100% - 2%
#descuento_Y = 0.979 (%) # 100% - 2.1%
#descuento_Z = 0.997 (%) # 100% - 0.3%
#descuento_punto = 1.01 (%) # 100% + 1%

    for letra in correo:                            
        if letra == "@":    
            break
        elif letra == "A":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_A

        elif letra == "E":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_E 

        elif letra == "i":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_i

        elif letra == "O":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_O

        elif letra == "U":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_U

        elif letra == "B":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_B

        elif letra == "L":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_L

        elif letra == "M":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_M

        elif letra == "X":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_X

        elif letra == "Y":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_Y

        elif letra == "Z":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_Z

        elif letra == ".":
            costo_vehiculo_seleccionado = costo_vehiculo_seleccionado * descuento_punto
            
    
    print("Ingresa el dinero (se aceptan montos entre $1 a $10.000) \n")

    print(f"COSTE CON DESCUENTO (Sí aplica): {costo_vehiculo_seleccionado:.0f}")

    ingreso_dinero = int(input(">> "))

    if ingreso_dinero < 1 or ingreso_dinero > 10000:
        print("Ingresa el dinero correspondiente (entre $1 a $10.000) \n")

        

    elif ingreso_dinero > costo_vehiculo_seleccionado:
        vuelto = ingreso_dinero - costo_vehiculo_seleccionado
        fondo_cambios = fondo_cambios - (ingreso_dinero - costo_vehiculo_seleccionado)

        


    print(f"Coste Estacionamiento ${costo_vehiculo_seleccionado}\n")
    print(f"DINERO INGRESADO: ${ingreso_dinero}\n")
    print(f"SU VUELTO: ${vuelto}")

    registro_ventas += costo_vehiculo_seleccionado



       


    














    


    
        






