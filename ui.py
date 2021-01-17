from dumb import header, yaml_load
import check

QUIT = ['quit', 'exit', 'q', 'x']

def profile_list_menu(profiles):
    display_names = [yaml_load(f"./profiles/{i}.yaml")['name'] for i in profiles]
    while True:
        header()
        print("Available profiles:")
        [print(f"   - {i}") for i in display_names]
        entry = input("\n").lower().strip()
        if entry in QUIT:
            exit()
        elif entry in profiles:
            return entry
        else:
            err("Profile not found")

def capture_directory(direction, map=True):
    while True:
        header()
        entry = input(f"What is the directory you want to sync {direction}?\n\n").strip()
        if entry.lower() in QUIT: exit()

        x_path, x_items = check.verify(entry, map)
        if x_path: return x_path, x_items
        else: continue

def capture_name():
    while True:
        header()
        entry = input("What would you like to name this profile?\n\n").strip()
        if entry.lower() in QUIT: exit()
        if check.Name(entry):
            yaml_name = check.Yaml(entry)
            if not yaml_name: continue
            else: return entry, yaml_name
        else:
            continue
