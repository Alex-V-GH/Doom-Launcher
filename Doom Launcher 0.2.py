import subprocess

def give_file(type,name):
    file, port = type[name]
    print(file)
    print(port)

def clean_lists(port):
    global map_packs_clean
    map_packs_clean = map_packs
    global full_clean
    full_clean = full
    global gameplay_clean
    gameplay_clean = gameplay
    print(2)

def recon():
    print("esta funcion hace reconocimiento de nuevos archivos/ports")
    global full
    global map_packs
    global gameplay
    global ports
    global path_base
    global path_full
    global path_maps
    global path_gp

    path_base = "D:\Juegos\Doom"
    path_full = path_base + "\Whole"
    path_maps = path_base + "\Map Packs"
    path_gp = path_base + "\Modes"

    ports = {
    "Zandronum": "\zandronum\zandronum.exe",
    "GZDoom": "\gzdoom\gzdoom.exe"
    }
    full = {
    "Pass": ("", "zg"),
    "After Doom": ("After Doom.pk3", "g"),
    "Country Cide": ("CountryCide.pk3", "g"),
    "Lullaby": ("Lullaby.pk3", "g"),
    "Shadow Hell": ("Shadow Hell.wad", "g"),
    "Town Infection": ("Town Infection.wad", "g"),
    "Void": ("Void.wad", "zg")
    }
    map_packs = {
        "None": ("", "zg"),
        "1 Monster": ("1 Monster.wad", "g"),
        "City of Corpses": ("City of Corpses.WAD", "z"),
        "Cyberdemons Castle": ("Cyberdemons Castle.wad", "g"),
        "Doom 2 Reloaded": ("Doom 2 Reloaded.wad", "z"),
        "Doom The Way Id Did": ("Doom The Way Id Did.wad", "g"),
        "Hell on Earth Starter Pack": ("Hell on Earth Starter Pack.wad", "z"),
        "Hellbound": ("Hellbound.wad", "g"),
        "Nerve": ("NERVE.WAD", "z"),
        "Reloaded": ("Reloaded.wad", "g"),
        "Scythe 2": ("Scythe 2.wad", "z"),
        "The Facility": ("The Facility.wad", "g"),
        "Visions Of Eternity": ("Visions Of Eternity.wad", "z"),
    }
    gameplay = {
        "Vanilla": ("", "zg"),
        "Brutal": ("brutalv21.9.0.pk3", "z"),
        "Complex": ("complex-doom.v26a2.pk3", "z"),
        "Legendary": ("lca-v1.5.9.6.pk3", "z"),
    }
    #leer, comparar y reescribir si necesita?
    

def main():
    recon()
    selected = []
    loop_gameplay = "y"

    print("=== Doom Launcher (locked edition) ===")
    print("Available ports:")

    for i, name in enumerate(ports.keys(), 1):
        print(f"{i}. {name}")

    #selected_port = ports(input("Select your port:"))

    port_list = list(ports.keys())
    choice = int(input("Select your port (number): ")) - 1
    selected_port_name = port_list[choice]
    selected_port = ports[selected_port_name]


    #MIGUEL CARDAMONE ES EL IMBECIL? SUBIO UN MANUAL DE PYTHON, DICE.
    clean_lists (selected_port)




    # FULL MOD SELECTION
    print("choose the number of a full mod")
    for i, name in enumerate(full_clean.keys(), 1):
        print(f"{i} --> {name}")
    full_list = list(full_clean.keys())
    choice = int(input("Select (number): ")) - 1
    selected_file_name = full_list[choice]
    file_path, port_flag = full_clean[selected_file_name]
    add_file = path_full + "\\" + file_path if file_path else ""
    if add_file:
        selected.append(add_file)


    if not selected:
        # MAP PACK SELECTION
        print("choose the number of a map pack")
        for i, name in enumerate(map_packs_clean.keys(), 1):
            print(f"{i} --> {name}")
        maps_list = list(map_packs_clean.keys())
        choice = int(input("Select (number): ")) - 1
        selected_file_name = maps_list[choice]
        file_path, port_flag = map_packs_clean[selected_file_name]
        add_file = path_maps + "\\" + file_path if file_path else ""
        if add_file:
            selected.append(add_file)


        # GAMEPLAY SELECTION
        while(loop_gameplay=="y"):
            print("Now choose any gameplay mod")
            for i, name in enumerate(gameplay_clean.keys(), 1):
                print(f"{i} --> {name}")
            gp_list = list(gameplay_clean.keys())
            choice = int(input("Select (number): ")) - 1
            selected_file_name = gp_list[choice]
            file_path, port_flag = gameplay_clean[selected_file_name]
            add_file = path_gp + "\\" + file_path if file_path else ""
            if add_file:
                selected.append(add_file)
            loop_gameplay = input("select another gameplay mod? Y/N").lower()
            print (loop_gameplay)

    # Armar el comando
    cmd = [path_base + selected_port, "-file"] + selected
    print("\nEjecutando:", " ".join(cmd))

    # Ejecutar el programa en bash
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    main()
