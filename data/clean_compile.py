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

# to be added to all C files in preprocessing, provides general utility + easy compilation
includes = \
    ["#include<stdlib.h>",
    "#include<stdio.h>",
    "#include<string.h>",
    "#include<stdbool.h>",
    "#include<stdint.h>",
    "#include<math.h>"]

includes_str = '\n'.join(includes) + '\n'

def unique(elements):
    '''
    Removes duplicates from collection while preserving order if elements are ordered, 
    returned as a list
    '''
    ans, seen = [], set()

    for elt in elements:
        if elt not in seen:
            ans.append(elt)
            seen.add(elt)

    return ans

def create_folder(folder_name):
    ''' Try to make a new folder with the given folder name '''
    try:
        os.mkdir(folder_name)
    except:
        pass

def clean_code(original_folder, new_folder):
    '''
    For every C file in the original folder, clean it (remove unnecessary spaces, newlines, 
    includes, comments, prints, etc.) and move it to the new folder
    '''
    create_folder(new_folder)

    def is_includes(s: str):
        return sum([1 if include in s else 0 for include in includes]) > 0

    for file_name in sorted(list(os.listdir(original_folder))): 
        with open(f'{original_folder}/{file_name}', 'r') as f:
            lines = f.read()

        # removal of excess tabs, spaces, etc
        lines = re.sub(r'[ \t]{2,}', '', lines).strip()
        lines = re.sub(r'\n+', '\n', lines)

        # handles comment removal
        lines = re.sub(r'\/\*[\s\S]*?\*\/', '', lines) + '\n'
        lines = re.sub(r'//.*\n', '\n', lines)

        # get rid of prints + includes
        lines = '\n'.join([line for line in lines.split('\n') if \
                            'print' not in line and not is_includes(line)])

        # add our includes back!
        lines = includes_str + lines

        with open(f'{new_folder}/{file_name}', "w") as out:
            out.write(lines)

def remove_cpp(original_folder, new_folder):
    """
    Copies all files that are not obviously C++ from the 
    original folder into the new folder. 
    """
    create_folder(new_folder)

    for file_name in sorted(list(os.listdir(original_folder))): 
        try:
            with open(f'{original_folder}/{file_name}', 'r') as f:
                c_code = f.read()

            # some common hints that the code is cpp
            if not("class Solution" in c_code or "public:" in c_code or "vector<" in c_code):
                shutil.copy(f'{original_folder}/{file_name}', f'{new_folder}/{file_name}')
        except:
            pass

def compile(original_folder, filtered_C_folder, compiled_ASM_folder):
    """
    Attempts to compile each C file in original_folder. 
    Copies all compile-able C code into filtered_C_folder, 
    Copies all compiled ASM code into compiled_ASM_folder
    """
    create_folder(filtered_C_folder)
    create_folder(compiled_ASM_folder)

    url = 'https://godbolt.org/api/compiler/cg83/compile'
    headers = {'Content-type': 'application/json'}
    api_fail = compile_fail = success = 0

    # for every source code in our folder
    for file_name in sorted(list(os.listdir(original_folder))):
        with open(f'{original_folder}/{file_name}', 'r') as f:
            lines = f.readlines()

        file_name = file_name.split('.')[0] + '.txt'
        code = ''.join(lines) # C source code

        # set up the request body -- we want ATT syntax and -w to suppress warnings
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
            # start from 68 to skip the "compilation by compiler explorer" message
            asm = response.text[68:]

            # check for compilation failure in the asm!
            if asm[0:20] == '<Compilation failed>':
                # print('ERROR! Compilation failed on the following file: ', original_file_name, end="")
                compile_fail += 1
            else:
                # write the assembly for this source code to our data folder, with ASM_ in front
                with open(f'{compiled_ASM_folder}/ASM_{file_name}', mode='w') as out:
                    out.write(asm)

                # move successfully compiled C file to filtered folder
                shutil.move(f'{original_folder}/{file_name}', f'{filtered_C_folder}/{file_name}')
                success += 1
            
            print(f"success: {success} | compiler fails: {compile_fail} | file: {file_name}")
        else:
            api_fail += 1
            print(f"api fails: {api_fail}")

def rename_vars(FINAL_SRC_CODE, elements, replace_str):
    '''
    Given some code and a set of existing variable names, rename them to 
    replace_str_{i} for i = 0, 1, to n (e.g. var_1, var_2, var_3, ...)
    '''
    all_checks = []
    var_names_to_new_vars = {}

    for i, var_name in enumerate(elements):
        var_names_to_new_vars[var_name] = replace_str + str(i)

        for op1 in operators:
            for op2 in operators:
                all_checks.append(op1 + var_name + op2)

    for to_check in all_checks:
        before = to_check[0]
        after = to_check[-1]
        between = to_check[1:-1]

        FINAL_SRC_CODE = FINAL_SRC_CODE.replace(to_check, before + \
                                var_names_to_new_vars[between] + after)
    
    return FINAL_SRC_CODE

def rename_structs(FINAL_SRC_CODE):
    '''
    Renames all structs in given source code to struct_1, struct_2, ...
    More specifically,
    A = struct x {};
    B = struct {} y;
    C = struct x {} y;
    D = typedef struct x {};
    E = typedef struct {} y;
    F = typedef struct x {} y;

    We need to rename F, E, C, A to maintain maintain consistent variable names (var_i)
    and struct type definitions (e.g. struct_i var_j = ..., not var_i var_j = ...)
    '''
    A = set(re.findall(r'struct\s+\w+\s*{[^}]*}\s*;', FINAL_SRC_CODE)) # 1064
    B = set(re.findall(r'struct\s*{[^}]*}\s*\w+;', FINAL_SRC_CODE)) # 216
    C = set(re.findall(r'struct\s+\w+\s*{[^}]*}\s*\w+;', FINAL_SRC_CODE)) # 121
    D = set(re.findall(r'typedef struct\s+\w+\s*{[^}]*}\s*;', FINAL_SRC_CODE)) # 3
    E = set(re.findall(r'typedef struct\s*{[^}]*}\s*\w+;', FINAL_SRC_CODE)) # 3
    F = set(re.findall(r'typedef struct\s+\w+\s*{[^}]*}\s*\w+;', FINAL_SRC_CODE)) # 3

    # only need to rename these (see above)
    F = {x.split('}')[-1].replace(';', '').strip(): x.split('{')[0].split()[-1].strip() for x in F}
    E = {x.split('}')[-1].replace(';', '').strip() for x in E}
    C = {x.split('}')[-1].replace(';', '').strip(): x.split('{')[0].split()[-1].strip() for x in C}
    A = {x.split('{')[0].split()[-1].strip() for x in A}

    FINAL_SRC_CODE = rename_vars(FINAL_SRC_CODE, F, 'struct_')
    FINAL_SRC_CODE = rename_vars(FINAL_SRC_CODE, E, 'struct_')
    FINAL_SRC_CODE = rename_vars(FINAL_SRC_CODE, C.values(), 'struct_')
    FINAL_SRC_CODE = rename_vars(FINAL_SRC_CODE, A, 'struct_')

    return FINAL_SRC_CODE

def rename(original_folder, new_folder):
    '''
    For every C file in the original folder, clean it (remove unnecessary spaces, newlines, 
    includes, comments, prints, etc.) and move it to the new folder
    '''
    create_folder(new_folder)

    for filename in sorted(list(os.listdir(original_folder))):
        print(filename, end='\r', flush=False)

        with open(f'{original_folder}/{filename}', 'r') as f:
            # get rid of spaces in parentheses for cleaning + no includes!
            FINAL_SRC_CODE = f.read().replace(' (', '(').replace(' )', ')')[112:]
        
        ##### GET ALL PARAM NAMES #####
        func_declarations = FINAL_SRC_CODE
        count = to_break = 0 # don't break

        # get rid of unbalanced braces and get function headers (destroy braces)
        while '{' in func_declarations:
            if count >= 100:
                print("removed ", filename)
                os.remove(f'{original_folder}/{filename}')
                to_break = True
                break
                
            count += 1
            func_declarations = re.sub(r'\{[^{}]*\}', '', func_declarations)

        if to_break:
            continue
        
        func_names = [x.split('(')[0] for x in func_declarations.strip().split() if '(' in x]
        func_names = [x.split('*')[-1] for x in func_names]
        func_names = set([x for x in func_names if x not in reserved_list and x not in operators and x != ''])

        ### REPLACE FUNC NAMES (not alphanumeric before, must be a parenthentical after)
        for i, func_name in enumerate(func_names):
            FINAL_SRC_CODE = re.sub(f"(?<=[^\w]){func_name}(?=[()])", 'func_' + str(i + 1), FINAL_SRC_CODE)

        param_names = re.findall(r'\((.*?)\)', func_declarations)
        param_names = [[i.strip().split()[-1] for i in x.split(',')] for x \
                        in param_names if x != '' and x[0] not in operators]
        param_names = '@@@'.join(['@@@'.join(x) for x in param_names]).split('@@@') # fold append workaround
        param_names = [x.split('*')[-1] for x in param_names if x != '']
        param_names = set([x for x in param_names if x not in reserved_list and x not in operators])

        ### GET ALL VAR NAMES AND COMBINE THEM TO GET ALL NAMES TO CONVERT ####
        variable_names = [x for x in re.findall(
            r"[a-zA-Z_][\w]*(?=[ ,;=\[\n\{])", FINAL_SRC_CODE) \
                if x not in reserved_list and x not in operators]

        variable_names = set([x.replace('*', '') for x in variable_names])
        all_names = set([x for x in param_names.union(variable_names) \
                            if x != '' and not x[0].isdigit() and x[0:5] != 'func_'])
        
        #### CHECK FOR ALL INSTANCES OF THIS VARIABLE NAME AND REPLACE IT
        FINAL_SRC_CODE = rename_vars(FINAL_SRC_CODE, all_names, 'var_')
        FINAL_SRC_CODE = rename_structs(FINAL_SRC_CODE)
        FINAL_SRC_CODE = includes_str + FINAL_SRC_CODE

        with open(f'{new_folder}/{filename}', 'w') as out:
            out.write(FINAL_SRC_CODE)

if __name__ == "__main__":
    # typical workflow looks like:
    # remove_cpp()  | original -> new
    # clean()       | original -> new
    # rename()      | original -> new
    # clean()       | original -> new
    # compile()     | original -> filtered -> new

    # clean_code('data/chatgpt_alternates', 'data/chatgpt_alternates')
    # compile('data/chatgpt_alternates', 'data/chatgpt_alternates_temp', 'data/chatgpt_alternates_ASM')
    rename('/Users/taiga.forestry/Downloads/systems/dl_final_project/data/ASM_tests','/Users/taiga.forestry/Downloads/systems/dl_final_project/data/ASM_tests')