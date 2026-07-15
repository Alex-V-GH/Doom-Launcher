import os
import subprocess

def debgprint(text):
    print("[DEBUG_start]================================================")
    print(text)
    print("[DEBUG_end]==================================================")

def listar(folder, tyype = 0):
    opcione = []
    opciones = []
    opcione.append ("Ninguno")
    if not os.path.isdir(folder):
        print(f"No existe la carpeta {folder}")
        return
    for archivo in os.listdir(folder):
        opcione.append(archivo)
    if tyype == 1:
        debgprint("tyype = 1")
        for opcion in opcione:
            if opcion.lower().endswith(".exe"):
                opciones.append(opcion)
    else:
        opciones = opcione
        debgprint(opcione)
        debgprint(opciones)
    return opciones


def select_port(base_folder):
    opciones = listar(os.path.join(base_folder,"Ports"), 1)
    index = 0
    for opcion in opciones:
        print(f"{index}: {opcion}")
        index += 1
    port = opciones [int(input("Cual sourceport desea elegir?\n"))]
    return port

def select_convertion(base_folder):
    opciones = listar(os.path.join(base_folder,"Midcon"))
    index = 0
    for opcion in opciones:
        print(f"{index}: {opcion}")
        index += 1
    conv = opcion [int(input("Desea elegir alguno de estos mods?\n*Nota: Estos corren solos, sin otros aditamientos.\n"))] + " "

    return conv

def select_modes(base_folder):
    opciones = listar(os.path.join(base_folder,"Modes"))
    index = 0
    modes = []
    for opcion in opciones:
        print(f"{index}: {opcion}")
        index += 1
    while mode is not "Ninguno":
        mode = opcion [int(input("Desea elegir algun modo?\n*Nota: Estos son stackeables, usar con atención a compatibilidades.\n"))]
        if mode is not "Ninguno":
            modes.append(os.path.join(base_folder,"Modes",mode))
    modess = ""
    for mod in modes:
        modess = modess + mod + " "
    return modess

def select_maps(base_folder):
    opciones = listar(os.path.join(base_folder,"Maps"))
    index = 0
    for opcion in opciones:
        print(f"{index}: {opcion}")
        index += 1
    maps = opcion [int(input("Desea elegir algun map pack?\n*Nota: UNO SOLO.\n"))]
    if port == "Ninguno":
        maps = ""
    return maps

def save_command(command):
    if input("Desea guardar esta configuración de arranque?\ns/n\n")=="s":
        comb_name = input("cual es el nombre de esta combinacion?\n")
        with open("dl_config.txt", "w", encoding="utf-8") as f:
            f.write(f"{comb_name}={command}")


if __name__ == "__main__":
    if input("desea recuperar su ultima configuracion?\ns/n\n")== "s":
        with open("dl_config.txt", "r", encoding="utf-8") as f:
            linea = f.read().strip()
        comb_name, command = linea.split("=", 1)
        print(f"ejecutando {comb_name}")

    else:
        base_folder = os.getcwd()
        port = os.path.join(base_folder,"Ports",select_port(base_folder))
        convertion = ""
        modes = ""
        map_pack = ""
        conv = select_convertion(base_folder)
        if conv != "Ninguno":
            convertion = os.path.join(base_folder,"Midconv",conv)
        else:
            modes = select_modes(base_folder)
            map_pack = os.path.join(base_folder,"Maps",select_maps(base_folder))
        debgprint(port)
        debgprint(convertion)
        debgprint(modes)
        debgprint(map_pack)

        command = f'{port} -file {convertion}{modes}{map_pack}'
        debgprint(command)
        save_command(command)

    print(command)
    subprocess.run(command, shell=True)