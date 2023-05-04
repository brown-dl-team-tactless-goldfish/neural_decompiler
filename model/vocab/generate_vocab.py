import os, sys
sys.path.insert(0, '')
from model.transformer.dataprocess import DataLoader, write_vocab_as_csv

current_dir = os.path.dirname(os.path.realpath(__file__))

def generate_load_data():
    print("Testing load_data")

    c_filedir_relative_path = "../../data/leetcode_data_FINAL/C_COMPILED_FILES"
    c_filedir_path = f"{current_dir}/{c_filedir_relative_path}"
    asm_filedir_relative_path = "../../data/leetcode_data_FINAL/ASM_COMPILED_FILES"
    asm_filedir_path = f"{current_dir}/{asm_filedir_relative_path}"

    dataloader = DataLoader(c_path=c_filedir_path, asm_path=asm_filedir_path)

    c_csv_filedir_relative_path = "c_vocab.csv"
    asm_csv_filedir_relative_path = "asm_vocab.csv"
    
    write_vocab_as_csv(dataloader.asm_vocab, f"{current_dir}/{asm_csv_filedir_relative_path}")
    write_vocab_as_csv(dataloader.c_vocab, f"{current_dir}/{c_csv_filedir_relative_path}")

    print(dataloader.stats)
    # print(dataloader.asm_vocab)

if __name__ == '__main__':
    generate_load_data()

    