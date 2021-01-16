#! /usr/bin/env python

#### CLISU v 0.1.1
#### Code by: Agentnumber47
#### Nickname: [0.1] Ground Zero [Scaled back from earlier attempts and rebuilding to higher glory]
#### Source: https://github.com/Agentnumber47/CLISU
#### Support me! https://ko-fi.com/agentnumber47
#### Differences between 0.1.1 and 0.1: Added file integrity check

# from colorama import init
import argparse
from dumb import fingerprinter, header, mkdir, rmvdir, yaml_load, yaml_save
import os
from shutil import copy, move
import yaml

# Entry Point #1
def terminal(args):
    # Grab and map directories
    path, items = capture_directory("from")
    host = Machine(path, items)
    path, items = capture_directory("to")
    parasite = Machine(path, items)

    # Begin syncing process
    header()
    sync(host, parasite)
    return

def capture_directory(direction, map=True):
    while True:
        header()
        entry = input(f"What is the directory you want to sync {direction}?\n\n")
        if entry.lower() == "x":
            exit()

        x_path, x_items = verify(entry, map)
        if not x_path: err(f"'{entry}' doesn't exist or is inaccessible")
        else: break
    return x_path, x_items


# Entry Point #2
def run(args):

    path, items = verify(args.run[0])
    if not path:
        err(f"ERROR: '{args.run[0]}' doesn't exist or is inaccessible", pause=False)
        return
    host = Machine(path, items)

    path, items = verify(args.run[1])
    if not path:
        err(f"ERROR: '{args.run[1]}' doesn't exist or is inaccessible", pause=False)
        return

    parasite = Machine(path, items)
    sync(host, parasite)
    return


def verify(x_path, map=True):
    try:
        if os.path.isdir(x_path) == False:
            return False, False
        else:
            if not x_path.endswith("/"): x_path = f"{x_path}/"
            if map:
                return x_path, generate_map(x_path)
            else:
                return x_path, False
    except:
        return False, False

def sync(host, parasite):
    for ld in host.items:
        item = ld # Do this or python will flip the fuck out

        ### Item found on both drives
        if item in parasite.items:
            hi, pi = render(item, host, parasite)
            if hi['relative path'] != pi['relative path']:
                # If the items are identical, move to match host map
                if fingerprinter(hi['full path']) == fingerprinter(pi['full path']):
                    mkdir(hi['directory mirror'])
                    move(pi['full path'], hi['path mirror'])
                    for i in [pi['directory'], pi['directory mirror']]: rmvdir(i)
        else:
            copy(host_items[item]['path'].replace("./", host_path), host_items[item]['path'].replace("./", parasite_path))

    print("Sync Successful!")
    return

def render(item, x, y):
    # x = '/path/to/x/file.txt', y = '/path/to/y/fyle.txt'

    # './file.txt', './fyle.txt'
    x_relpath, y_relpath = x.items[item]['path'], y.items[item]['path']

    # '/path/to/x/file.txt', '/path/to/y/fyle.txt'
    x_full_path, y_full_path = x.items[item]['path'].replace('./', x.path), y.items[item]['path'].replace('./', y.path) #

    # '/path/to/y/file.txt', '/path/to/x/fyle.txt'
    x_full_path_mirror, y_full_path_mirror = x.items[item]['path'].replace('./', y.path), y.items[item]['path'].replace('./', x.path)

    # '/path/to/x/', '/path/to/y/'
    x_directory, y_directory = x_full_path.replace(item, ""), y_full_path.replace(item, "")

    x_directory_mirror, y_directory_mirror = x_full_path_mirror.replace(item, ""), y_full_path_mirror.replace(item, "")

    x_render = {
    'relative path' : x_relpath,
    'full path' : x_full_path,
    'path mirror' : x_full_path_mirror,
    'directory' : x_directory,
    'directory mirror' : x_directory_mirror
    }
    y_render = {
    'relative path' : y_relpath,
    'full path' : y_full_path,
    'path mirror' : y_full_path_mirror,
    'directory' : y_directory,
    'directory mirror' : y_directory_mirror
    }
    return x_render, y_render


def generate_map(x_path):
    media = {}
    for root, dirs, files in os.walk(x_path):
        for name in files:
            if not "/." in root and not name.startswith("."):
                file_base = os.path.join(root, name) ## Root = path | Name = file
                media[file_base.split("/")[-1]] = {"path": file_base.replace(f"{x_path}", "./")}

    return media

def profile(args):
    list_add = ['a', 'add', '+']
    list_change = ['c', 'change', 'edit']
    list_delete = ['d', 'rm', 'delete', 'remove', '-']
    list_list = ['l', 'list', 'all']
    if args.profile[0].lower() in ['h', 'help']:
        print("Purpose: To utilize predefined parameters to perform sync functions.")
        print("Use: './clisu.py --profile FUNCTION'")
        print(f"\nAdd {[i for i in list_add]}:\n     Add a profile\n     OPTIONAL: 'add [NAME] [/from/dir] [/to/dir]'")
        print(f"Change {[i for i in list_change]}:\n     Change a profile\n     OPTIONAL: 'change [NAME]'")
        print(f"Delete {[i for i in list_delete]}:\n     Delete a profile\n     OPTIONAL: 'delete [NAME]'")
        print(f"List {[i for i in list_list]}:\n     List created profiles")
        print("")
    elif args.profile[0].lower() in list_add:
        if len(args.profile) == 1:
            while True:
                header()
                name = input("What would you like to name this profile?\n\n")
                if name_check(name):
                    yaml_name = yaml_check(name)
                    # for char in name.lower():
                    #     if char in "0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z - _".split(" "): yaml_name += char
                    #     if f"{yaml_name}.yaml" in list_profiles(): input("Profile name taken")
                    if not yaml_name: continue
                    else: break
                else:
                    continue
            data = {'name':name}
            data['host'] = capture_directory("from", map=False)[0]
            data['parasite'] = capture_directory("to", map=False)[0]
            yaml_save(yaml_name, data)
            return

        elif len(args.profile) == 4:
            if name_check(args.profile[1]):
                print("Proper")
            else:
                print("FALSE")

        else:
            err("Incorrect use.\nUse either:\n     './clisu.py --profile add'\nOR\n     './clisu.py --profile add [NAME] [/from/dir] [/to/dir]'", pause=False)
    elif args.profile[0].lower() in list_change:
        pass

    else:
        print("No valid function selected. Run '-p help' for available functions.")

def name_check(name, pause=True):
    if name == "":
        err("Profile name cannot be blank", pause)
        return False
    elif name.lower() == "x": exit()
    elif len(name) > 20:
        err("Profile name too long", pause)
        return False
    else:
        return True

def yaml_check(name, pause=True):
    yaml_name = ""
    for char in name.lower():
        if char in "0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z - _".split(" "): yaml_name += char
    if f"{yaml_name}.yaml" in list_profiles():
        err("Profile name taken", pause)
        return False
    else:
        return yaml_name

def err(e, pause=True):
    if pause:
        input(f"\n{e}\n")
    else:
        print(f"\n{e}\n")
    return

def list_profiles():
    profile_dir = os.listdir('./profiles')
    try:
        for file in profile_dir:
            if not file.endswith(".yaml"):
                profile_dir.remove(file)
    except:
        pass
    finally:
        return profile_dir

def main():
    # Check for proper setup
    if not os.path.isfile('./config.yaml'):
        with open(f"./config.yaml", 'w') as f: yaml_dump = yaml.dump({'default' : False}, f)
    mkdir('./profiles')

    parser = argparse.ArgumentParser(description = "CLISU (CLI Synchronization Utility)")

    parser.add_argument("-t", "--terminal", nargs = "*", metavar = "", type = str, help = "run with prompts in terminal")
    parser.add_argument("-r", "--run", nargs = 2, metavar = ('/path/from', '/path/to'), type = str, help = "run without prompts")
    parser.add_argument("-p", "--profile", nargs = "*", metavar = "FUNCTION", type = str, help = "profile functions")
    ## Defaults

    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.terminal != None: terminal(args)
    elif args.run != None: run(args)
    elif args.profile != None: profile(args)

    return

class Machine:
    def __init__(self, path, items):
        self.items = items
        self.path = path


if __name__ == '__main__':
    main()
