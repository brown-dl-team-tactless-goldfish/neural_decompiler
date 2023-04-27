import os
import re
import shutil
import requests

class CodeCleanerCompiler:
    """
    CodeCleanerCompiler {CLASS}:
    - Handles all cleaning of scraped data
    - Compiles the 
    """

    def __init__(self):
        self.current_file_path = os.path.dirname(os.path.realpath(__file__))

    def clean_code(self, original_folder, new_folder):

        code_dir_path = f"{self.current_file_path}/{original_folder}"
        new_dir_path = f"{self.current_file_path}/{new_folder}"

        try:
            os.mkdir(new_dir_path)
        except:
            pass

        # to be added to the top of the file, does not affect compilation
        # but without, sometimes code will not compile
        includes = (
            "stdlib.h",
            "stdio.h",
            "string.h",
            "stdbool.h",
            "stdint.h",
            "math.h",
        )
        
        includes_as_str = ""
        for include in includes:
            includes_as_str += f"#include<{include}>\n"

        def is_includes(s: str):
            for i in includes:
                if i in s:
                    return True
            return False

        for file_name in sorted(list(os.listdir(code_dir_path))): 
            if file_name == '.DS_Store':
                continue 

            path = f"{code_dir_path}/{file_name}"
            new_path = f"{new_dir_path}/{file_name}"

            # read file
            with open(path, "r") as f:
                lines = f.read()

            # handles comment removal
            lines = re.sub(r'\/\*[\s\S]*?\*\/', '', lines)
            lines = re.sub(r'//.*\n', '\n', lines)
            lines = re.sub(r'[ \t]{2,}', '', lines).strip()
            lines = re.sub(r'\n+', '\n', lines)

            # reformat of tabs, spaces, etc
            lines = '\n'.join([line for line in lines.split('\n') if \
                               "print" not in line and not is_includes(line)])

            lines = includes_as_str + lines

            with open(new_path, "w") as g:
                g.write(lines)

    def remove_cpp(self, original_folder, new_folder):
        """
        Copies all files that are not obviously C++ from the 
        original folder into the new folder. 
        """

        code_dir_path = f"{self.current_file_path}/{original_folder}"
        new_dir_path = f"{self.current_file_path}/{new_folder}"

        try:
            os.mkdir(new_dir_path)
        except:
            pass

        for file_name in sorted(list(os.listdir(code_dir_path))): 
            path = f"{code_dir_path}/{file_name}"

            try:
                with open(path, "r") as f:
                    c_code = f.read()
                cpp_unique_str = "class Solution"

                # some common hints that the code is cpp
                if not(cpp_unique_str in c_code or "public:" in c_code or \
                    "vector<" in c_code):
                    shutil.copy(path, new_dir_path)
            
            except:
                shutil.copy(path, new_dir_path)

    def compile(self, original_folder, filtered_C_folder, compiled_ASM_folder):
        """
        Attempts to compile each C file in original_folder. 
        Copies all compile-able C code into filtered_C_folder, 
        Copies all compiled ASM code into compiled_ASM_folder
        """

        url = 'https://godbolt.org/api/compiler/cg83/compile'
        headers = {'Content-type': 'application/json'}


        uncompiled_path = f'{self.current_file_path}/{original_folder}'
        new_c_path = f'{self.current_file_path}/{filtered_C_folder}'
        assembly_path = f'{self.current_file_path}/{compiled_ASM_folder}'

        try:
            os.mkdir(new_c_path)
        except:
            pass

        try:
            os.mkdir(assembly_path)
        except:
            pass


        api_fail = 0
        compile_fail = 0
        success = 0

        # for every source code in our folder
        for original_file_name in sorted(list(os.listdir(uncompiled_path))):
            filepath = uncompiled_path + "/" + original_file_name
            f = open(filepath, 'r')
            file_name = original_file_name.split('.')[0] + '.txt'
            lines = f.readlines()
            code = ''.join(lines) # C source code

            # set up the request body -- we want ATT syntax and -w to 
            # surpress warnings!
            req_body = {
                "source": code,
                "options": {
                    "userArguments": "-w",
                    "filters": {
                        "intel": False
                    }
                }
            }

            response = requests.post(url, headers=headers, json=req_body)

            if response.ok:
                # start from 68 to skip the "compilation by compiler explorer" 
                # message
                asm = response.text[68:]

                # check for compilation failure in the asm!
                if asm[0:20] == '<Compilation failed>':
                    # print('ERROR! Compilation failed on the following file: ',
                    #  original_file_name, end="")
                    compile_fail += 1
                    
                else:
                    # write the assembly for this source code to our data 
                    # folder, with [ASM] in front
                    with open(assembly_path + '/ASM_' + file_name, 
                              mode='w') as out:
                        out.write(asm)

                    newfilepath = new_c_path + "/" + original_file_name

                    shutil.copy(filepath, newfilepath)

                    f.close()
                    success += 1

                print(f"success: {success} | compiler fails: {compile_fail} | file: {file_name}")
            else:
                api_fail += 1
                print(f"api fails: {api_fail}")

def clean():
    ccc = CodeCleanerCompiler()
    ccc.remove_cpp("extra_code", "extra_c_code")
    ccc.clean_code("extra_c_code", "extra_cleaned_c_code")

def compile():
    ccc = CodeCleanerCompiler()
    ccc.compile("gfg_cleaned_c_code", "GFG_C_FILES", "GFG_ASM_FILES")

if __name__ == "__main__":
    # clean()
    compile()