import os
import sys
import yaml


def dir_to_dict(path):
    directory = {}
    for dirname, dirnames, filenames in os.walk(path):

        dn = os.path.basename(dirname)
        directory[dn] = []
        if dirnames:
            for d in dirnames:
                directory[dn].append(dir_to_dict(path=os.path.join(path, d)))
            for f in filenames:
                    if ".DS_Store" not in f:
                        directory[dn].append(f)
        else:
            directory[dn] = filenames
        return directory


inputpath = '/Users/clairefarrell/College/TCD/DISS/facebook-academic-data'
filepath = "src/DirectoryStructures"
filename= "/facebook_directory_structure.yaml"
yamlfile = filepath+filename

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, filepath)
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

try:
    with open(yamlfile, "w") as f:
        try:
            yaml.dump(dir_to_dict(path=inputpath), f, default_flow_style=False)
            print("Dictionary written to {}.yaml".format(yamlfile))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
