import os
import subprocess
"'"
def debgprint(text):
    print("[DEBUG_start]================================================")
    print(text)
    print("[DEBUG_end]==================================================")


def listar(folder, tyype=0):
    opciones = ["Ninguno"]
    if not os.path.isdir(folder):
        print(f"No existe la carpeta {folder}")
        return []
    for archivo in os.listdir(folder):
        opciones.append(archivo)

    if tyype == 1:
        result = ["Ninguno"]
        for opcion in opciones:
            if opcion == "Ninguno":
                continue
            ruta = os.path.join(folder, opcion)  # FIX: unir folder + nombre antes de listar/chequear
            if os.path.isdir(ruta):
                for opcion_real in os.listdir(ruta):
                    if opcion_real.lower().endswith(".exe"):
                        result.append(os.path.join(opcion, opcion_real))  # FIX: guarda subcarpeta/exe.exe
            elif opcion.lower().endswith(".exe"):  # FIX: soporta exe suelto directo en Ports/
                result.append(opcion)
        return result
    else:
        return opciones


def select_port(base_folder):
    opciones = listar(os.path.join(base_folder, "Ports"), 1)
    for index, opcion in enumerate(opciones):
        print(f"{index}: {opcion}")
    port = opciones[int(input("Cual sourceport desea elegir?\n"))]
    return port


def select_convertion(base_folder):
    opciones = listar(os.path.join(base_folder, "Midcon"))  # FIX: nombre de carpeta consistente con el main
    for index, opcion in enumerate(opciones):
        print(f"{index}: {opcion}")
    # FIX: indexaba "opcion" (string suelto del for) en vez de "opciones" (la lista)
    conv = opciones[int(input("Desea elegir alguno de estos mods?\n*Nota: Estos corren solos, sin otros aditamientos.\n"))]
    return conv  # FIX: ya no le pego el " " acá, eso se maneja al armar el comando


def select_modes(base_folder):
    opciones = listar(os.path.join(base_folder, "Modes"))
    for index, opcion in enumerate(opciones):
        print(f"{index}: {opcion}")
    modes = []
    mode = None  # FIX: inicializar antes del while (si no, NameError en la primera evaluación)
    while mode != "Ninguno":  # FIX: comparar strings con != en vez de "is not"
        # FIX: indexaba "opcion" en vez de "opciones"
        mode =opciones[int(input("Desea elegir algun modo?\n*Nota: Estos son stackeables, usar con atención a compatibilidades.\n"))]
        if mode != "Ninguno":
            modes.append(os.path.join(base_folder, "Modes", mode))
    return '"' + " ".join(modes) + '"'


def select_maps(base_folder):
    opciones = listar(os.path.join(base_folder, "Maps"))
    for index, opcion in enumerate(opciones):
        print(f"{index}: {opcion}")
    # FIX: indexaba "opcion" en vez de "opciones"
    maps = opciones[int(input("Desea elegir algun map pack?\n*Nota: UNO SOLO.\n"))]
    if maps == "Ninguno":  # FIX: comparaba con "port", que ni existe en esta función
        maps = ""
    return maps


def save_command(command):
    if input("Desea guardar esta configuración de arranque?\ns/n\n") == "s":
        comb_name = input("cual es el nombre de esta combinacion?\n")
        with open("dl_config.txt", "w", encoding="utf-8") as f:
            f.write(f"{comb_name}={command}")


if __name__ == "__main__":
    if input("desea recuperar su ultima configuracion?\ns/n\n") == "s":
        with open("dl_config.txt", "r", encoding="utf-8") as f:
            linea = f.read().strip()
        comb_name, command = linea.split("=", 1)
        print(f"ejecutando {comb_name}")

    else:
        base_folder = os.getcwd()
        port = os.path.join(base_folder, "Ports", select_port(base_folder))
        convertion = ""
        modes = ""
        map_pack = ""

        conv = select_convertion(base_folder)
        if conv != "Ninguno":
            convertion = '"' + os.path.join(base_folder, "Midcon", conv) + '"'
        else:
            modes = select_modes(base_folder)
            maps = select_maps(base_folder)
            if maps:
                map_pack = '"' + os.path.join(base_folder, "Maps", maps) + '"'

        debgprint(port)
        debgprint(convertion)
        debgprint(modes)
        debgprint(map_pack)

        # FIX: armado del comando con espacios explícitos entre partes, filtrando vacíos
        partes = [p for p in [convertion, modes, map_pack] if p]
        command = f'{port} -file ' + " ".join(partes) if partes else port

        debgprint(command)
        save_command(command)

    print(command)
    subprocess.run(command, shell=True)
