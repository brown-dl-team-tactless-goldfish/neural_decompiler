import os, sys
sys.path.insert(0, '')


import random
from model.transformer.dataprocess import DataLoader, Tokenizer, write_vocab_as_csv, read_vocab_from_csv


current_dir = os.path.dirname(os.path.realpath(__file__))



c_path = f"{current_dir}/../../data/leetcode_data_FINAL/C_COMPILED_FILES"
asm_path = f"{current_dir}/../../data/leetcode_data_FINAL/ASM_COMPILED_FILES"




def get_random_file(dir_path):
    """
    Returns index of and random string of file within a directory
    """
    files = sorted(os.listdir(dir_path))

    num_files = len(files)

    idx = random.randint(0, num_files-1)

    with open(f"{dir_path}/{files[idx]}", "r") as f:
        code = f.read()

    return idx, code

def read_file(file_path):
    with open(file_path, "r") as f:
        code = f.read()
    return code


def test_c_tokenization():
    """
    DEPRECATED
    """

    c_filedir_relative_path = "../tiny_dataset/C"
    c_filedir_path = f"{current_dir}/{c_filedir_relative_path}"

    # make a DataLoader object to test the helper functions
    dataloader = Tokenizer()

    with open(f"{c_filedir_path}/two-sum-1.txt", "r") as f:
        c_code = f.read()

    c_code = dataloader.clean_c(c_code)
    tokens = dataloader.tokenize_c(c_code)

    print(tokens)

def test_c_token_check():
    token = "hello++"

    dataloader = Tokenizer()

    print(dataloader.check_c_token(token))

def test_asm_tokenization():
    """
    DEPRECATED
    """

    asm_filedir_relative_path = "../tiny_dataset/ASM"
    asm_filedir_path = f"{current_dir}/{asm_filedir_relative_path}"

    dataloader = Tokenizer()

    with open(f"{asm_filedir_path}/ASM_arithmetic-subarrays-2.txt", "r") as f:
        asm_code = f.read()

    tokens, _, _ = dataloader.tokenize_asm(asm_code)

    print(tokens)

def test_c_vocab():
    c_filedir_relative_path = "../tiny_dataset/C"
    c_filedir_path = f"{current_dir}/{c_filedir_relative_path}"
    asm_filedir_relative_path = "../tiny_dataset/ASM"
    asm_filedir_path = f"{current_dir}/{asm_filedir_relative_path}"

    dataloader = DataLoader(c_path=c_filedir_path, asm_path=asm_filedir_path)

    print(dataloader.generate_c_vocabulary())


def test_asm_vocab():
    c_filedir_relative_path = "../tiny_dataset/C"
    c_filedir_path = f"{current_dir}/{c_filedir_relative_path}"
    asm_filedir_relative_path = "../tiny_dataset/ASM"
    asm_filedir_path = f"{current_dir}/{asm_filedir_relative_path}"

    dataloader = DataLoader(c_path=c_filedir_path, asm_path=asm_filedir_path)

    print(dataloader.generate_asm_vocabulary())

def test_load_data():
    print("Testing load_data")

    c_filedir_relative_path = "../../data/leetcode_data_FINAL/C_COMPILED_FILES"
    c_filedir_path = f"{current_dir}/{c_filedir_relative_path}"
    asm_filedir_relative_path = "../../data/leetcode_data_FINAL/ASM_COMPILED_FILES"
    asm_filedir_path = f"{current_dir}/{asm_filedir_relative_path}"

    dataloader = DataLoader(c_path=c_filedir_path, asm_path=asm_filedir_path)

    c_csv_filedir_relative_path = "../vocab/c_vocab.csv"
    asm_csv_filedir_relative_path = "../vocab/asm_vocab.csv"
    
    write_vocab_as_csv(dataloader.asm_vocab, f"{current_dir}/{asm_csv_filedir_relative_path}")
    write_vocab_as_csv(dataloader.c_vocab, f"{current_dir}/{c_csv_filedir_relative_path}")

    print(dataloader.stats)
    # print(dataloader.asm_vocab)
    print(dataloader.load_data()[0])





def test_tokenization():

    tokenizer = Tokenizer()

    idx, asm_code = get_random_file(asm_path)
    c_code = read_file(f"{c_path}/{sorted(os.listdir(c_path))[idx]}")
    print(asm_code)
    print()
    print(c_code)
    print()
    asm_tokens, asm_string_to_token, asm_num_to_token = tokenizer.tokenize_asm(asm_code)
    c_tokens = tokenizer.tokenize_c(c_code, asm_string_to_token, asm_num_to_token)
    print("ASM:")
    print(asm_tokens)
    print()
    print("C:")
    print(c_tokens)
    print()
    print(asm_string_to_token)
    print(asm_num_to_token)


def manual_tokenize_test():
    tokenizer = Tokenizer()

    asm_code = '''
func_2:
        pushq   %rbp
        movq    %rsp, %rbp
        movl    %edi, -4(%rbp)
        movl    -4(%rbp), %eax
        addl    $5, %eax
        popq    %rbp
        ret
func_1:
        pushq   %rbp
        movq    %rsp, %rbp
        subq    $8, %rsp
        movl    %edi, -4(%rbp)
        movl    -4(%rbp), %eax
        movl    %eax, %edi
        call    func_2
        leave
        ret
    '''

    c_code = '''
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdint.h>
#include<math.h>
int func_2(int var_0) {
return var_0 + 5;
}
int func_1(int var_0) {
return func_2(var_0);
}
    '''

    out, one, two = tokenizer.tokenize_asm(asm_code)
    print(", ".join(out))

    print()

    out = tokenizer.tokenize_c(c_code, one, two)
    print(", ".join(out))







def test_read_csv():
    asm_vocab_dir = "../vocab/new_asm_vocab.csv"
    c_vocab_dir = "../vocab/new_c_vocab.csv"

    asm_vocab_path = f"{current_dir}/{asm_vocab_dir}"
    c_vocab_path = f"{current_dir}/{c_vocab_dir}"

    ASM_VOCAB = read_vocab_from_csv(asm_vocab_path)
    C_VOCAB = read_vocab_from_csv(c_vocab_path)

    print(ASM_VOCAB)
    print(C_VOCAB)


def vocab_generation_from_dataload():
    c_filedir_relative_path = "../../data/leetcode_data_FINAL/C_COMPILED_FILES"
    c_filedir_path = f"{current_dir}/{c_filedir_relative_path}"
    asm_filedir_relative_path = "../../data/leetcode_data_FINAL/ASM_COMPILED_FILES"
    asm_filedir_path = f"{current_dir}/{asm_filedir_relative_path}"
    asm_vocab_path = f"{current_dir}/../vocab/new_asm_vocab.csv"
    c_vocab_path = f"{current_dir}/../vocab/new_c_vocab.csv"

    dataloader = DataLoader(c_path=c_filedir_path, asm_path=asm_filedir_path)

    ASM_VOCAB = read_vocab_from_csv(asm_vocab_path)
    C_VOCAB = read_vocab_from_csv(c_vocab_path)

    asm_vals, c_vals, stats = dataloader.load_data(ASM_VOCAB, C_VOCAB)

    print(asm_vals)
    print(c_vals)





if __name__ == "__main__":
    # test_c_tokenization()
    # test_c_token_check()
    # test_asm_tokenization()
    # test_c_vocab()
    # test_asm_vocab()
    # test_load_data()
    # test_read_csv()
    # vocab_generation_from_dataload()
    # test_tokenization()
    manual_tokenize_test()


