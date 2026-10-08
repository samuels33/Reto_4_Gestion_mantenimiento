aeronaves = {
    "HK-4087": {
        "modelo": "A320neo",
        "horas_de_vuelo": 0,
        "componentes": [
            {
                "pieza": "motor_derecho",
                "horas_uso": 0,
                "limite_de_horas": 1200
            },
            {
                "pieza": "motor_izquierdo",
                "horas_uso": 0,
                "limite_de_horas": 1200
            },
            {
                "pieza": "tren_de_aterrizaje",
                "horas_uso": 0,
                "limite_de_horas": 250
            },
            {
                "pieza": "neumaticos",
                "horas_uso": 0,
                "limite_de_horas": 50
            },
            {
                "pieza": "discos_frenos",
                "horas_uso": 0,
                "limite_de_horas": 150
            }
        ]
    },

    "HJ-264": {
        "modelo": "zenith",
        "horas_de_vuelo": 0,
        "componentes": [
            {
                "pieza": "motor",
                "horas_uso": 0,
                "limite_de_horas": 1000
            },
            {
                "pieza": "tren_de_aterrizaje",
                "horas_uso": 0,
                "limite_de_horas": 350
            },
            {
                "pieza": "neumaticos",
                "horas_uso": 0,
                "limite_de_horas": 100 
            },
            {
                "pieza": "discos_frenos",
                "horas_uso": 0,
                "limite_de_horas": 200  
            }
        ]
    },

    "N264AB": {
        "modelo": "B777X",
        "horas_de_vuelo": 0,
        "componentes": [
            {
                "pieza": "motor_derecho",
                "horas_uso": 0,
                "limite_de_horas": 1200
            },
            {
                "pieza": "motor_izquierdo",
                "horas_uso": 0,
                "limite_de_horas": 1200
            },
            {
                "pieza": "tren_de_aterrizaje",
                "horas_uso": 0,
                "limite_de_horas": 350
            },
            {
                "pieza": "neumaticos",
                "horas_uso": 0,
                "limite_de_horas": 50
            },
            {
                "pieza": "discos_frenos",
                "horas_uso": 0,
                "limite_de_horas": 150
            }
        ]
    }
}


while True:
    print("--- OPCIONES ---")
    print("1. Ingresar nueva aeronave")
    print("2. Agregar componentes a aeronave")
    print("3. Registrar horas de vuelo y revisar mantenimiento")
    print("4. Salir")
    opcion = input("Ingrese una opcion (1-4): ")

    if opcion == "1":
        matricula = input("Ingrese la matricula de la nueva aeronave: ").upper()
        if matricula in aeronaves:
            print("La aeronave ya existe.")
        else:
            modelo = input("Ingrese el modelo: ")
            aeronaves[matricula] = {
                "modelo": modelo,
                "horas_de_vuelo": 0,
                "componentes": []
            }
            print(f"Aeronave {matricula} ingresada con exito.")

    elif opcion == "2":
        print("Aeronaves disponibles:", list(aeronaves.keys()))
        matricula = input("Ingrese la matricula de la aeronave: ").upper()
        if matricula in aeronaves:
            pieza = input("Ingrese el nombre del componente: ").lower()
            limite = float(input("Ingrese el limite de horas del componente: "))
            aeronaves[matricula]["componentes"].append({
                "pieza": pieza,
                "horas_uso": 0,
                "limite_de_horas": limite
            })
            print(f"Componente {pieza} agregado a {matricula}.")
        else:
            print("La matricula ingresada no existe.")

    elif opcion == "3":
        print("Aeronaves disponibles:", list(aeronaves.keys()))
        matricula = input("Ingrese la matricula de la aeronave: ").upper()

        if matricula in aeronaves: 
            aeronave_seleccionada = aeronaves[matricula]
            print(f"Modelo: {aeronave_seleccionada["modelo"]}")

            horas_de_vuelo = float(input("Ingrese las horas de vuelo de la aeronave: "))
            aeronave_seleccionada["horas_de_vuelo"] += horas_de_vuelo

            # 1. Sumar horas a todos los componentes
            for componente in aeronave_seleccionada["componentes"]:
                componente["horas_uso"] += horas_de_vuelo

            print("---Horas de la aeronave despues del vuelo:---")
            for componente in aeronave_seleccionada["componentes"]:
                print(f"- {componente['pieza']}: {componente['horas_uso']} / {componente['limite_de_horas']} horas")

            # 2. Revisar mantenimiento
            print("---Revision de mantenimientos:---")
            for componente in aeronave_seleccionada["componentes"]: 
                if componente["horas_uso"] >= componente["limite_de_horas"]:
                    print(f"¡ALERTA! Requiere mantenimiento: {componente["pieza"]}")
                    mantenimiento = input("¿Desea realizar el mantenimiento? (si/no): ").lower()
                    
                    if mantenimiento == "si":
                        componente["horas_uso"] = 0
                        print(f"Mantenimiento realizado con exito en {componente["pieza"]}.")

            # 3. Mostrar el estado final de todas las partes
            print(f"---ESTADO FINAL DE LOS COMPONENTES DE {matricula}:---")
            for componente in aeronave_seleccionada["componentes"]:
                print(f"- {componente['pieza']}: {componente['horas_uso']} horas")

        else:
            print("La matricula ingresada no existe.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion invalida.")
