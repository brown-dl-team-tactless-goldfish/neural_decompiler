import os
import requests

# path to all the source codes
current_file_path = os.path.dirname(os.path.realpath(__file__))
uncompiled_path = f'{current_file_path}/cleaned_c'
assembly_path = f'{current_file_path}/compiled'
c_path = 'data/c'

# set up the Compiler Explorer API endpoint using gcc 8.3 for C
url = 'https://godbolt.org/api/compiler/cg83/compile'

# set up the request headers
headers = {'Content-type': 'application/json'}

# inputs are assembly, labels are the C code that produced the assembly
# inputs, labels = [], []

api_fail = 0
compile_fail = 0
success =0

# for every source code in our folder
for original_file_name in sorted(list(os.listdir(uncompiled_path))):
    f = open(uncompiled_path + "/" + original_file_name, 'r')
    file_name = original_file_name.split('.')[0] + '.txt'
    lines = f.readlines()
    code = ''.join(lines) # C source code

    # set up the request body -- we want ATT syntax and -w to surpress warnings!
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
            # write the assembly for this source code to our data folder, with [ASM] in front
            with open(assembly_path + '/[ASM] ' + file_name, mode='w') as out:
                out.write(asm)


            # write this source code to our data folder
            # with open(c_path + '/' + file_name, mode='w') as out:
            #     out.write(code)

            # remove this from our uncompiled folder for future uses of this script
            f.close()
            success += 1

            # os.remove(uncompiled_path + '/' + original_file_name)
        print(f"success: {success} | compiler fails: {compile_fail} | file: {file_name}")
    else:
        # print('ERROR! API failed while on the following file: ', original_file_name)
        # print(f'Error {response.status_code}: {response.reason}')

        api_fail += 1
        print(f"api fails: {api_fail}")



print(f"api fails: {api_fail}")
print(f"compiler fails: {compile_fail}")