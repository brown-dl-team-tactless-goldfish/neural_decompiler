import os
import re


current_file_path = os.path.dirname(os.path.realpath(__file__))
code_dir_path = f"{current_file_path}/c_code"
new_dir_path = f"{current_file_path}/cleaned_c"


includes = (
    "stdlib.h",
    "stdio.h",
    "string.h",
    "stdbool.h",
    "stdint.h",
    "math.h"
)


def is_includes(s: str):
    for i in includes:
        if i in s:
            return True
    return False


for file_name in sorted(list(os.listdir(code_dir_path))): 
    path = f"{code_dir_path}/{file_name}"
    new_path = f"{new_dir_path}/{file_name}"

    with open(path, "r") as f:
        lines = f.read()

    lines = re.sub(r'\/\*[\s\S]*?\*\/', '', lines)
    lines = re.sub(r'//.*\n', '\n', lines)
    lines = re.sub(r'[ \t]{2,}', '', lines).strip()
    lines = re.sub(r'\n+', '\n', lines)

    lines = '\n'.join([line for line in lines.split('\n') if "print" not in line and not is_includes(line)])


    top = "#include<stdlib.h>\n#include<stdio.h>\n#include<string.h>\n#include<stdbool.h>\n#include<math.h>\n#include<stdint.h>\n"
    lines = top + lines


    with open(new_path, "w") as g:
        g.write(lines)
