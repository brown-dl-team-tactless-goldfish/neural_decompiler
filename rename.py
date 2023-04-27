import re
import os

folder_path = 'C_FILES'
reserved_list = set(['auto', 'else', 'long', 'switch', 'break',	'enum',	'register',	'typedef', 
                    'case', 'extern', 'return', 'union', 'char', 'float', 'short', 'unsigned', 
                    'const', 'for', 'signed', 'void', 'continue', 'goto', 'sizeof', 'volatile', 
                    'default', 'if', 'static', 'while', 'do', 'int', 'struct', 'double', 'NULL', 'nullptr', 
                    'bool', 'true', 'false', 'int8_t', 'uint8_t', 'int16_t', 'uint16_t', 'int32_t', 'uint32_t', 
                    'int64_t', 'uint64_t', 'size_t', 'size_t', 'ssize_t', 'NAN', 'INFINITY', 'M_PI', 'SIZE_MAX'])

operators = [' ', ';', '=', '~', '+', '-', '*', '/', ',', '.', 
            '<', '>', '&', '|', '%', '?', '{', '}', '^', '!', 
            '[', ']', '(', ')', '\n']

for filename in sorted(list(os.listdir(folder_path))):
    with open(folder_path + '/' + filename, 'r') as f:
        FINAL_SRC_CODE = f.read()

    # get rid of structs 
    src_code = re.sub(r'struct\s+\w+\s*{([^}]*)}', '', FINAL_SRC_CODE)

    ##### GET ALL PARAM NAMES #####
    param_names = src_code

    while '{' in param_names:
        param_names = re.sub(r'\{[^{}]*\}', '', param_names)

    func_names = set([x.split('(')[0] for x in param_names.strip().split() if '(' in x])
    param_names = re.findall(r'\((.*?)\)', param_names)
    param_names = [[i.strip().split()[-1].split('*')[-1] for i in x.split(',')] for x in param_names]

    temp = []

    for x in param_names:
        temp.extend(x)

    param_names = temp

    # print("PARAM NAMES: ", param_names)

    ### GET ALL VAR NAMES AND COMBINE THEM TO GET ALL NAMES TO CONVERT ####
    variable_names = [x for x in re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*(?=[ ,;=\[])", src_code) if x not in reserved_list]
    # print("VAR NAMES: ", variable_names)

    all_names = sorted([elt for elt in set(param_names + variable_names) if elt not in func_names])
    # print("ALL NAMES: ", all_names)

    #### CHECK FOR ALL INSTANCES OF THIS VARIABLE NAME AND REPLACE IT #######
    all_checks = []
    var_names_to_new_vars = {}

    for i, var_name in enumerate(all_names):
        var_names_to_new_vars[var_name] = 'var_' + str(i)

        for op1 in operators:
            for op2 in operators:
                all_checks.append(op1 + var_name + op2)

    for to_check in all_checks:
        before = to_check[0]
        after = to_check[-1]
        between = to_check[1:-1]
        FINAL_SRC_CODE = FINAL_SRC_CODE.replace(to_check, before + var_names_to_new_vars[between] + after)

    with open(folder_path + '/' + filename, 'w') as out:
        out.write(FINAL_SRC_CODE)

    break
    # print(FINAL_SRC_CODE)