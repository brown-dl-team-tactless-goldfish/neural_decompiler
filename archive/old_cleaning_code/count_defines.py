import os
import shutil


current_file_path = os.path.dirname(os.path.realpath(__file__))
code_dir_path = f"{current_file_path}/C_FILES"


count = 0
for file_name in sorted(list(os.listdir(code_dir_path))): 
    path = f"{code_dir_path}/{file_name}"

    with open(path, "r") as f:
        try:

            c_code = f.read()
            cpp_unique_str = "#define"

            if cpp_unique_str in c_code:
                count += 1
        
        except:
            pass

print(count)