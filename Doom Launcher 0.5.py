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
    in_not_0 = 999
    while in_not_0 != 0:
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
        if text == "modes":
            in_not_0 = in_not_0 * eleccion
        else:
            in_not_0 = 0
       
def guardar_comb():
    print("desea guardar la combinacion?")
    if input()=="s":
        print("cual es el nombre de esta combinacion?")
        comb_name = input()
        with open("dl_config.txt", "w", encoding="utf-8") as f:
            f.write(f"{comb_name}={COMMAND}")

# ===== EJECUCIÓN =====

print("desea recuperar su ultima configuracion?")
if input()== "s":
    with open("dl_config.txt", "r", encoding="utf-8") as f:
        linea = f.read().strip()
    comb_name, COMMAND = linea.split("=", 1)
    print(f"ejecutando {comb_name}")
else:
    listar_ports()
    listar_mods("midcon")
    listar_mods("maps")
    listar_mods("modes")
    guardar_comb()
print(COMMAND)
subprocess.run(COMMAND, shell=True)
