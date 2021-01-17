import dumb
from os.path import isdir
from os.path import join as path_join
from os import listdir, walk

def Name(name, pause=True):
    if name == "":
        dumb.err("Profile name cannot be blank", pause)
        return False
    elif name.lower() == "x": exit()
    elif len(name) > 20:
        dumb.err("Profile name too long", pause)
        return False
    else:
        return True

def verify(x_path, map=True, pause=True):
    try:
        if isdir(x_path) == False:
            dumb.err(f"'{x_path}' doesn't exist or is inaccessible", pause)
            return False, False
        else:
            if not x_path.endswith("/"): x_path = f"{x_path}/"
            if map:
                return x_path, generate_map(x_path)
            else:
                return x_path, False
    except:
        return False, False

def generate_map(x_path):
    media = {}
    for root, dirs, files in walk(x_path):
        for name in files:
            if not "/." in root and not name.startswith("."):
                file_base = path_join(root, name) ## Root = path | Name = file
                media[file_base.split("/")[-1]] = {"path": file_base.replace(f"{x_path}", "./")}

    return media

def Yaml(name, pause=True):
    yaml_name = ""
    for char in name.lower():
        if char in "0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z - _".split(" "): yaml_name += char
    if f"{yaml_name}.yaml" in audit_profiles():
        dumb.err("Profile name taken", pause)
        return False
    else:
        return yaml_name

def audit_profiles():
    profile_dir = listdir('./profiles')
    try:
        for file in profile_dir:
            if not file.endswith(".yaml"):
                profile_dir.remove(file)
    except:
        pass
    finally:
        return profile_dir
