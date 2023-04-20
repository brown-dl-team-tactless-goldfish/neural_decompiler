import os
import sys


current_file_path = os.path.dirname(os.path.realpath(__file__))
code_dir_path = f"{current_file_path}/"

for file_name in sorted(list(os.listdir(code_dir_path))): 
    path = f"{code_dir_path}/{file_name}"

    print(path)

    with open(path, "r") as f:
        c_code = f.read()
        "class Solution"
        if 