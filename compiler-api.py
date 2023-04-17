import os
import requests

# path to all the source codes
sources_path = 'sources'
assembly_path = 'assembly'

# set up the Compiler Explorer API endpoint using gcc 8.3 for C
url = 'https://godbolt.org/api/compiler/cg83/compile'

# set up the request headers
headers = {'Content-type': 'application/json'}

# inputs are assembly, labels are the C code that produced the assembly
# inputs, labels = [], []

# for every source code in our folder
for source_file in os.listdir(sources_path):
    f = open(sources_path + "/" + source_file, 'r')
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
        # inputs.append(asm)
        # labels.append(code)

        # write the assembly for this source code to our folder, with [ASM] in front
        with open(assembly_path + '/[ASM] ' + source_file, mode='w') as out:
            out.write(asm)
    else:
        print('FAILED ON THE FOLLOWING C FILE: ', source_file)
        print(f'Error {response.status_code}: {response.reason}')
        break


