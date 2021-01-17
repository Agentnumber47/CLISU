from hashlib import md5
from os import get_terminal_size as gts
from os import listdir as ls
from os import makedirs
from os import rmdir as rm
from os import system as sys
import yaml

def header():
    shell_columns = gts().columns
    # print("\033[36m")
    sys("clear")
    print(f"#     CLISU     #".center(shell_columns, "#"))
    # print("\033[39m")
    print("")
    return

def rmvdir(x_path):
    try:
        if len(ls(x_path)) == 0: rm(x_path) # If the directory is empty, delete it
    except:
        pass
    finally:
        return

def mkdir(x_path):
    try:
        makedirs(x_path)
    except:
        pass
    finally:
        return

def fingerprinter(x_path):
    BLOCK_SIZE = 65536
    hash_method = md5()
    with open(x_path, 'rb') as input_file:
        buf = input_file.read(BLOCK_SIZE)
        while len(buf) > 0:
            hash_method.update(buf)
            buf = input_file.read(BLOCK_SIZE)

    return hash_method.hexdigest()

def yaml_load(path):
    with open(path) as f:
        data = yaml.full_load(f)
    return data

def yaml_save(name, data):
    with open(f"./profiles/{name}.yaml", 'w') as f:
        yaml_dump = yaml.dump(data, f)

def err(e, pause=True):
    if pause:
        input(f"{e}\n")
    else:
        print(f"{e}")
    return


# /home/sev/synctest PC/
