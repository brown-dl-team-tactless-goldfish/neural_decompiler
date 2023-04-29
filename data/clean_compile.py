import os
import re
import shutil
import requests



reserved_list = set(['auto', 'else', 'long', 'switch', 'break',	'enum',	'register',	'typedef', 'inline',
            'case', 'extern', 'return', 'union', 'char', 'float', 'short', 'unsigned', 
            'const', 'for', 'signed', 'void', 'continue', 'goto', 'sizeof', 'volatile', 
            'default', 'if', 'static', 'while', 'do', 'int', 'struct', 'double', 'NULL', 'nullptr', 
            'bool', 'true', 'false', 'int8_t', 'uint8_t', 'int16_t', 'uint16_t', 'int32_t', 'uint32_t', 
            'int64_t', 'uint64_t', 'size_t', 'size_t', 'ssize_t', 'NAN', 'INFINITY', 'M_PI', 'SIZE_MAX'])

operators = [' ', ':', ';', '=', '~', '+', '-', '*', '/', ',', '.', 
            '<', '>', '&', '|', '%', '?', '{', '}', '^', '!', 
            '[', ']', '(', ')', '\n', '\t']




class CodeCleanerCompiler:
    """
    CodeCleanerCompiler {CLASS}:
    - Handles all cleaning of scraped data
    - Compiles the C code to ASM via the Compiler Explorer API
    - Renames variables appropriately
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

    def rename(self, c_folder):

        folder_path = f"{self.current_file_path}/{c_folder}"

        for filename in sorted(list(os.listdir(folder_path))):
            if filename == '.DS_Store':
                continue

            print(filename, end='\r', flush=True)
            # print(filename)
            with open(folder_path + '/' + filename, 'r') as f:
                FINAL_SRC_CODE = f.read()

            # get rid of structs 
            src_code = re.sub(r'struct\s+\w+\s*{([^}]*)}', '', FINAL_SRC_CODE)

            ##### GET ALL PARAM NAMES #####
            param_names = src_code
            count = 0

            while '{' in param_names:
                if count >= 100000:
                    print()
                    print("removed ", folder_path + '/' + filename)
                    os.remove(folder_path + '/' + filename)
                    break
                    
                count += 1

                param_names = re.sub(r'\{[^{}]*\}', '', param_names)

            func_names = set([x.split('(')[0] for x in \
                              param_names.strip().split() if '(' in x])
            func_names = set([x.replace('*', '') for x in func_names])
            func_names = set([x for x in func_names if x not in \
                              reserved_list and x not in operators])

            if '' in func_names:
                func_names.remove('')

            ### REPLACE FUNC NAMES
            for i, func_name in enumerate(func_names):
                FINAL_SRC_CODE = FINAL_SRC_CODE.replace(func_name, 
                                                        'func_' + str(i + 1))

            # print("FUNC NAMES", func_names)
            param_names = re.findall(r'\((.*?)\)', param_names)
            # print(param_names)
            param_names = [[i.strip().split()[-1] for i in x.split(',')] for x \
                           in param_names if x != '' and x[0] not in operators]

            temp = []

            for x in param_names:
                temp.extend(x)

            param_names = [x.replace('*', '') for x in temp]
            param_names = set([x for x in param_names if x not in \
                               reserved_list and x not in operators])

            # print("PARAM NAMES: ", param_names)

            ### GET ALL VAR NAMES AND COMBINE THEM TO GET ALL NAMES TO CONVERT ####
            variable_names = [x for x in re.findall(
                r"[a-zA-Z_][a-zA-Z0-9_]*(?=[ ,;=\[])", src_code) \
                    if x not in reserved_list and x not in operators]
            variable_names = set([x.replace('*', '') for x in variable_names])

            # print("VAR NAMES: ", variable_names)\

            all_names = sorted([elt for elt in \
                                param_names.union(variable_names) if elt not \
                                    in func_names and not elt.isdigit()])

            if '' in all_names:
                all_names.remove('')

            # print("ALL NAMES: ", all_names)

            #### CHECK FOR ALL INSTANCES OF THIS VARIABLE NAME AND REPLACE IT 
            all_checks = []
            var_names_to_new_vars = {}

            for i, var_name in enumerate(all_names):
                var_names_to_new_vars[var_name] = 'var_' + str(i)

                for op1 in operators:
                    for op2 in operators:
                        all_checks.append(op1 + var_name + op2)

            FINAL_SRC_CODE = FINAL_SRC_CODE[112:]

            for to_check in all_checks:
                before = to_check[0]
                after = to_check[-1]
                between = to_check[1:-1]
                FINAL_SRC_CODE = FINAL_SRC_CODE.replace(to_check, before + \
                                        var_names_to_new_vars[between] + after)

            FINAL_SRC_CODE = '''#include<stdlib.h>
                #include<stdio.h>
                #include<string.h>
                #include<stdbool.h>
                #include<stdint.h>
                #include<math.h>\n''' + FINAL_SRC_CODE

            FINAL_SRC_CODE = FINAL_SRC_CODE.replace('\t', '')

            with open(folder_path + '/' + filename, 'w') as out:
                out.write(FINAL_SRC_CODE)

def clean():
    ccc = CodeCleanerCompiler()
    ccc.remove_cpp("extra_code", "extra_c_code")
    ccc.clean_code("extra_c_code", "extra_cleaned_c_code")

def compile():
    ccc = CodeCleanerCompiler()
    ccc.compile("leetcode_data/C_FILES", "leetcode_data/C_COMPILED_FILES", 
                "leetcode_data/ASM_COMPILED_FILES")
    
def rename():
    ccc = CodeCleanerCompiler()
    ccc.rename("leetcode_data/C_FILES")

if __name__ == "__main__":
    # clean()
    compile()