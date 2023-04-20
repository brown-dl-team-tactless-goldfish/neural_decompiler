import os
import re


current_file_path = os.path.dirname(os.path.realpath(__file__))
code_dir_path = f"{current_file_path}/c_code"
new_dir_path = f"{current_file_path}/cleaned_c"


for file_name in sorted(list(os.listdir(code_dir_path))): 
    path = f"{code_dir_path}/{file_name}"
    new_path = f"{new_dir_path}/{file_name}"

    with open(path, "r") as f:
        lines = f.read()

    lines = re.sub(r'\/\*[\s\S]*?\*\/', '', lines)
    lines = re.sub(r'//.*\n', '\n', lines)
    lines = re.sub(r'\s+', ' ', lines).strip()

    with open(new_path, "w") as g:
        g.write(lines)


