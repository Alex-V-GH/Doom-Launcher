import os
import subprocess

ruta_base = r"D:\Juegos\Doom"
COMMAND = ""


def listar_ports():
    ruta = os.path.join(ruta_base, "Ports")
    ports = {}

    if not os.path.isdir(ruta):
        print("No existe la carpeta Ports")
        return

    for i, archivo in enumerate(os.listdir(ruta), start=1):
        if archivo.lower().endswith(".exe"):
            ports[i] = archivo

    for i, p in ports.items():
        print(i, "--->", p)

    esperar_input(ports, "port", ruta)


def listar_mods(tipo):
    ruta = os.path.join(ruta_base, tipo)
    piezas = {}

    if not os.path.isdir(ruta):
        print(f"No existe la carpeta {tipo}")
        return

    for i, archivo in enumerate(os.listdir(ruta), start=1):
        if os.path.isfile(os.path.join(ruta, archivo)):
            piezas[i] = archivo

    for i, p in piezas.items():
        print(i, "--->", p)

    esperar_input(piezas, tipo, ruta)


def esperar_input(lista, text, ruta):
    global COMMAND

    try:
        eleccion = int(input(f"Elija su {text}: "))
        archivo = lista[eleccion]
    except ValueError:
        print("Entrada inválida (no es un número)")
        return
    except KeyError:
        print("Opción inexistente")
        return
    print(f"Elegiste {archivo}")
    r_final = os.path.join(ruta, archivo)

    if text == "port":
        COMMAND += f'"{r_final}" '
        COMMAND += "-file "
    else:
        COMMAND += f'"{r_final}" '


# ===== EJECUCIÓN =====

listar_ports()
listar_mods("midcon")
listar_mods("maps")
listar_mods("modes")

print("\nCOMANDO FINAL:")
print(COMMAND)

subprocess.run(COMMAND, shell=True)