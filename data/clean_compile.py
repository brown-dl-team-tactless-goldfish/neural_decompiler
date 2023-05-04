import os
import re
import shutil
import requests

reserved_list = set(['auto', 'else', 'long', 'switch', 'break',	'enum',	'register',	'typedef', 'inline',
            'case', 'extern', 'return', 'union', 'char', 'float', 'short', 'unsigned', 'define', 'exit',
            'const', 'for', 'signed', 'void', 'continue', 'goto', 'sizeof', 'volatile', 'defined',
            'default', 'if', 'static', 'while', 'do', 'int', 'struct', 'double', 'NULL', 'nullptr', 
            'bool', 'true', 'false', 'uint', 'int8_t', 'uint8_t', 'int16_t', 'uint16_t', 'int32_t', 'uint32_t', 
            'int64_t', 'uint64_t', 'size_t', 'size_t', 'ssize_t', 'NAN', 'INFINITY', 'M_PI', 'SIZE_MAX',
            'INT32_MAX', 'INT32_MIN', 'RAND_MAX', 'INT_MAX', 'INT_MIN'])

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
        for i, original_file_name in enumerate(sorted(list(os.listdir(uncompiled_path)))):
            filepath = uncompiled_path + "/" + original_file_name
            f = open(filepath, 'r')
            file_name = original_file_name.split('.')[0] + '.txt'
            lines = f.readlines()
            code = ''.join(lines) # C source code
            x = ['01-matrix-0.txt', '01-matrix-1.txt', '01-matrix-11.txt', '01-matrix-12.txt', '01-matrix-13.txt', '01-matrix-2.txt', '01-matrix-4.txt', '01-matrix-5.txt', '01-matrix-7.txt', '01-matrix-9.txt', '2-keys-keyboard-0.txt', '2-keys-keyboard-10.txt', '2-keys-keyboard-13.txt', '2-keys-keyboard-2.txt', '2-keys-keyboard-3.txt', '2-keys-keyboard-4.txt', '2-keys-keyboard-5.txt', '2-keys-keyboard-6.txt', '2-keys-keyboard-8.txt', '2-keys-keyboard-9.txt', '24-game-0.txt', '24-game-1.txt', '3sum-10.txt', '3sum-11.txt', '3sum-14.txt', '3sum-2.txt', '3sum-3.txt', '3sum-5.txt', '3sum-6.txt', '3sum-8.txt', '3sum-closest-0.txt', '3sum-closest-1.txt', '3sum-closest-10.txt', '3sum-closest-11.txt', '3sum-closest-12.txt', '3sum-closest-14.txt', '3sum-closest-2.txt', '3sum-closest-6.txt', '3sum-closest-7.txt', '3sum-with-multiplicity-0.txt', '3sum-with-multiplicity-1.txt', '3sum-with-multiplicity-2.txt', '3sum-with-multiplicity-3.txt', '4sum-0.txt', '4sum-11.txt', '4sum-12.txt', '4sum-14.txt', '4sum-2.txt', '4sum-3.txt', '4sum-4.txt', '4sum-6.txt', '4sum-7.txt', '4sum-8.txt', '4sum-ii-0.txt', '4sum-ii-13.txt', '4sum-ii-8.txt', '4sum-ii-9.txt', 'a-number-after-a-double-reversal-0.txt', 'a-number-after-a-double-reversal-1.txt', 'a-number-after-a-double-reversal-11.txt', 'a-number-after-a-double-reversal-12.txt', 'a-number-after-a-double-reversal-13.txt', 'a-number-after-a-double-reversal-14.txt', 'a-number-after-a-double-reversal-2.txt', 'non-overlapping-intervals-8.txt', 'zuma-game-6.txt']
            if file_name == '000-TEST.txt':
                continue
            # print(file_name)
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
                    print(f"success: {success} | compiler fails: {compile_fail} | file: {file_name}")   
                else:
                    # write the assembly for this source code to our data 
                    # folder, with [ASM] in front
                    with open(assembly_path + '/ASM_' + file_name, 
                              mode='w') as out:
                        out.write(asm)

                    newfilepath = new_c_path + "/" + original_file_name

                    shutil.move(filepath, newfilepath)

                    f.close()
                    success += 1

                print(f"success: {success} | compiler fails: {compile_fail} | file: {file_name}")
            else:
                api_fail += 1
                print(f"api fails: {api_fail}")

    def rename_structs(self, FINAL_SRC_CODE):
        A = set(re.findall(r'struct\s+\w+\s*{[^}]*}\s*;', FINAL_SRC_CODE)) # 1064
        B = set(re.findall(r'struct\s*{[^}]*}\s*\w+;', FINAL_SRC_CODE)) # 216
        C = set(re.findall(r'struct\s+\w+\s*{[^}]*}\s*\w+;', FINAL_SRC_CODE)) # 121
        D = set(re.findall(r'typedef struct\s+\w+\s*{[^}]*}\s*;', FINAL_SRC_CODE)) # 3
        E = set(re.findall(r'typedef struct\s*{[^}]*}\s*\w+;', FINAL_SRC_CODE)) # 3
        F = set(re.findall(r'typedef struct\s+\w+\s*{[^}]*}\s*\w+;', FINAL_SRC_CODE)) # 3

        # find highest available struct count
        highest_struct_count = 1
        F = {x.split('}')[-1].replace(';', '').strip(): x.split('{')[0].split()[-1].strip() for x in F}
        E = {x.split('}')[-1].replace(';', '').strip() for x in E}
        C = {x.split('}')[-1].replace(';', '').strip(): x.split('{')[0].split()[-1].strip() for x in C}
        B = {x.split('}')[-1].replace(';', '').strip() for x in B}
        A = {x.split('{')[0].split()[-1].strip() for x in A}

        for elt in F:
            all_checks = []

            for op1 in operators:
                for op2 in operators:
                    all_checks.append(op1 + elt + op2)

            for to_check in all_checks:
                before = to_check[0]
                after = to_check[-1]
                between = to_check[1:-1]
                FINAL_SRC_CODE = FINAL_SRC_CODE.replace(to_check, before +'struct_' + str(highest_struct_count) + after)
            
            highest_struct_count += 1

        for elt in E:
            all_checks = []

            for op1 in operators:
                for op2 in operators:
                    all_checks.append(op1 + elt + op2)

            for to_check in all_checks:
                before = to_check[0]
                after = to_check[-1]
                between = to_check[1:-1]
                FINAL_SRC_CODE = FINAL_SRC_CODE.replace(to_check, before +'struct_' + str(highest_struct_count) + after)
            
            highest_struct_count += 1
        
        for val in C.values():
            all_checks = []

            for op1 in operators:
                for op2 in operators:
                    all_checks.append(op1 + val + op2)

            for to_check in all_checks:
                before = to_check[0]
                after = to_check[-1]
                between = to_check[1:-1]
                FINAL_SRC_CODE = FINAL_SRC_CODE.replace(to_check, before +'struct_' + str(highest_struct_count) + after)
            
            highest_struct_count += 1
        
        for elt in A:
            all_checks = []

            for op1 in operators:
                for op2 in operators:
                    all_checks.append(op1 + elt + op2)

            for to_check in all_checks:
                before = to_check[0]
                after = to_check[-1]
                between = to_check[1:-1]
                FINAL_SRC_CODE = FINAL_SRC_CODE.replace(to_check, before +'struct_' + str(highest_struct_count) + after)
            
            highest_struct_count += 1

        return FINAL_SRC_CODE
    
    def rename(self, c_folder):
        folder_path = f"{self.current_file_path}/{c_folder}"

        for filename in sorted(list(os.listdir(folder_path))):
            # print(filename, end='\r', flush=False)

            with open(folder_path + '/' + filename, 'r') as f:
                # get rid of spaces in parentheses for cleaning + no includes!
                FINAL_SRC_CODE = f.read().replace(' (', '(').replace(' )', ')')[112:]
            
            # get rid of structs for finding param names
            src_code = re.sub(r'struct\s+\w+\s*{([^}]*)}', '', FINAL_SRC_CODE)

            ##### GET ALL PARAM NAMES #####
            param_names = src_code
            count = 0
            to_break = False

            # get rid of unbalanced braces
            while '{' in param_names:
                if count >= 100000:
                    print("removed ", filename)
                    os.remove(folder_path + '/' + filename)
                    to_break = True
                    break
                    
                count += 1
                param_names = re.sub(r'\{[^{}]*\}', '', param_names)

            if to_break:
                continue
            
            func_names = set([x.split('(')[0] for x in \
                                param_names.strip().split() if '(' in x])
            func_names = set([x.split('*')[-1] for x in func_names])
            func_names = set([x for x in func_names if x not in \
                                reserved_list and x not in operators and x != ''])

            ### REPLACE FUNC NAMES
            for i, func_name in enumerate(func_names):
                FINAL_SRC_CODE = re.sub(f"(?<=[^a-zA-Z0-9_]){func_name}(?=[()])", 'func_' + str(i + 1), FINAL_SRC_CODE)
            # print("FUNC NAMES", func_names)

            param_names = re.findall(r'\((.*?)\)', param_names)
            param_names = [[i.strip().split()[-1] for i in x.split(',')] for x \
                            in param_names if x != '' and x[0] not in operators]

            temp = []

            for x in param_names:
                temp.extend(x)

            param_names = [x.split('*')[-1] for x in temp]
            param_names = set([x for x in param_names if x not in \
                                reserved_list and x not in operators])

            # print("PARAM NAMES: ", param_names)

            ### GET ALL VAR NAMES AND COMBINE THEM TO GET ALL NAMES TO CONVERT ####
            variable_names = [x for x in re.findall(
                r"[a-zA-Z_][a-zA-Z0-9_]*(?=[ ,;=\[\n\{])", FINAL_SRC_CODE) \
                    if x not in reserved_list and x not in operators]

            variable_names = set([x.replace('*', '') for x in variable_names])

            # print("VAR NAMES: ", variable_names)

            all_names = sorted(set([elt for elt in \
                                param_names.union(variable_names) \
                                if elt != '' and not elt.isdigit() and elt[0:5] != 'func_']))

            # print("ALL NAMES: ", all_names)

            #### CHECK FOR ALL INSTANCES OF THIS VARIABLE NAME AND REPLACE IT 
            all_checks = []
            var_names_to_new_vars = {}

            for i, var_name in enumerate(all_names):
                var_names_to_new_vars[var_name] = 'var_' + str(i)

                for op1 in operators:
                    for op2 in operators:
                        all_checks.append(op1 + var_name + op2)

            for _ in range(2):
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

            FINAL_SRC_CODE = FINAL_SRC_CODE.replace('\t', ' ') + '\n'

            if 'struct' in FINAL_SRC_CODE:
                FINAL_SRC_CODE = self.rename_structs(FINAL_SRC_CODE)

            with open(folder_path + '/' + filename, 'w') as out:
                out.write(FINAL_SRC_CODE)

def clean():
    ccc = CodeCleanerCompiler()
    # ccc.remove_cpp("extra_code", "extra_c_code")
    ccc.clean_code("test", "test")

def compile():
    ccc = CodeCleanerCompiler()
    ccc.compile("extra_data_FINAL/EXTRA_C_COMPILED_FILES", "extra_data_FINAL/EXTRA_C_COMPILED_FILES", 
                "extra_data_FINAL/EXTRA_ASM_COMPILED_FILES")
    
def rename():
    ccc = CodeCleanerCompiler()
    ccc.rename('leetcode_data_FINAL/C_COMPILED_FILES')
    # ccc.rename('test')

if __name__ == "__main__":
    # rename()
    # clean() 
    compile()