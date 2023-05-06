import os

current_dir = os.path.dirname(os.path.realpath(__file__))

c_vocab_filepath = f"{current_dir}/c_vocab.csv"
new_c_vocab_filepath = f"{current_dir}/new_c_vocab.csv"
asm_vocab_filepath = f"{current_dir}/asm_vocab.csv"
new_asm_vocab_filepath = f"{current_dir}/new_asm_vocab.csv"

with open(asm_vocab_filepath, 'r') as f:
    lines = f.read()

lines = lines.split('\n')

new_lines = [lines[0]]

for line_num, line in enumerate(lines[1:]):
    comma_index = 0
    for i in range(len(line)):
        if line[i] == ',':
            comma_index = i
    
    line = line[:comma_index]

    line += f",{line_num}"

    new_lines.append(line)


with open(new_asm_vocab_filepath, 'w') as f:
    f.write("\n".join(new_lines))
    

