#! /usr/bin/env python
#### CLISU v 0.1
#### Code by: Agentnumber47
#### Nickname: Ground Zero [Scaled back from earlier attempts and rebuilding to higher glory]
# from colorama import init
import argparse
import os
import shutil

def terminal(args):
    # Grab and map the host directory
    while True:
        header()
        host_path = input("What is the master directory? [Ex. /path/to/dir]\n")
        if host_path.lower() == "x":
            exit()

        host = verify(host_path)
        if not host: input(f"\n'{host_path}' doesn't exist or is inaccessible\n")
        else: break

    # Grab and map the parasite directory
    while True:
        header()
        parasite_path = input("What is the directory you want to sync to?\n")
        if parasite_path.lower() == "x":
            exit()

        parasite = verify(parasite_path)
        if not parasite: input(f"\n'{parasite_path}' doesn't exist or is inaccessible\n")
        else: break

    # Begin syncing process
    header()
    sync(host_path, host, parasite_path, parasite)

def run(args):
    host_path = args.run[0]
    host = verify(host_path)
    if not host:
        print(f"ERROR: '{host_path}' doesn't exist or is inaccessible")
        return

    parasite_path = args.run[1]
    parasite = verify(parasite_path)
    if not parasite:
        print(f"ERROR: '{parasite_path}' doesn't exist or is inaccessible")
        return

    sync(host_path, host, parasite_path, parasite)


def verify(x_path):
    if os.path.isdir(x_path) == False:

        return False
    else:
        if not x_path.endswith("/"): x_path += "/"
        return generate_map(x_path)

def sync(host_path, host, parasite_path, parasite):
    for ld in host:
        item = ld # Do this or python will flip the fuck out

        ### Item found on both drives
        if item in parasite:
            if host[item]['path'] != parasite[item]['path']:
                # try:
                old_path = parasite[item]['path'].replace("./", parasite_path)
                old_path_mirror = parasite[item]['path'].replace("./", host_path)
                new_path = host[item]['path'].replace("./", parasite_path)
                try:
                    os.makedirs(new_path.replace(item, ""))
                except:
                    pass
                shutil.move(old_path, new_path)
                if len(os.listdir(old_path.replace(item, ""))) == 0: os.rmdir(old_path.replace(item, ""))
                if len(os.listdir(old_path_mirror.replace(item, ""))) == 0: os.rmdir(old_path_mirror.replace(item, ""))
                # except:
                #     pass
        else:
            shutil.copy(host[item]['path'].replace("./", host_path), host[item]['path'].replace("./", parasite_path))

    print("Sync Successful!")


def header():
    shell_columns = os.get_terminal_size().columns
    # print("\033[36m")
    os.system("clear")
    print(f"#     CLISU     #".center(shell_columns, "#"))
    # print("\033[39m")
    print("")
    return

def generate_map(x_path):
    media = {}
    for root, dirs, files in os.walk(x_path):
        for name in files:
            if not "/." in root and not name.startswith("."):
                file_base = os.path.join(root, name) ## Root = path | Name = file
                media[file_base.split("/")[-1]] = {"path": file_base.replace(f"{x_path}", "./")}

    return media


def main():
    parser = argparse.ArgumentParser(description = "CLISU (CLI Synchronization Utility)")

    parser.add_argument("-t", "--terminal", nargs = "*", metavar = "", type = str, help = "run with prompts in terminal")
    parser.add_argument("-r", "--run", nargs = 2, metavar = ('/path/from', '/path/to'), type = str, help = "run without prompts")

    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.terminal != None:
        terminal(args)
    elif args.run != None:
        run(args)

if __name__ == '__main__':
    main()
