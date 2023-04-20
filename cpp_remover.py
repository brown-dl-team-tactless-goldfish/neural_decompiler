import os
import shutil


current_file_path = os.path.dirname(os.path.realpath(__file__))
code_dir_path = f"{current_file_path}/code"



for file_name in sorted(list(os.listdir(code_dir_path))): 
    path = f"{code_dir_path}/{file_name}"

    with open(path, "r") as f:
        try:

            c_code = f.read()
            cpp_unique_str = "class Solution"
            if cpp_unique_str in c_code:
                shutil.move(path, f"cpp_code/{file_name}")
        
        except:
            shutil.move(path, f"cpp_code/{file_name}")

