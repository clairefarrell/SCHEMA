import os
import yaml

outputpath = '/Users/clairefarrell/POD'
yamlfile = 'src/DirectoryStructures/facebook_directory_structure.yaml'

def dict_to_dir(data, path=str()):
    dest = os.path.join(os.getcwd(), path)
    if isinstance(data, dict):
        for k, v in data.items():
            os.makedirs(os.path.join(dest, k))
            dict_to_dir(v, os.path.join(path, str(k)))
    elif isinstance(data, list):
        for i in data:
            if isinstance(i, dict):
                dict_to_dir(i, path)
            else:
                with open(os.path.join(dest, i), "a"):
                    os.utime(os.path.join(dest, i), None)
    if isinstance(data, dict):
        return list(data.keys())[0]

try:
    with open(yamlfile, "r") as f:
        try:
            d = yaml.load(f)
            dest = dict_to_dir(data=d, path=outputpath)
            print("Directory created at {}".format(outputpath if outputpath else os.path.join(os.getcwd(), dest)))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)