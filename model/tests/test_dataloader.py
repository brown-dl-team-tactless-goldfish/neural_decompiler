import os, sys
sys.path.insert(0, '')
from model.transformer.dataprocess import DataLoader


current_dir = os.path.dirname(os.path.realpath(__file__))

def test_c_tokenization():
    c_filedir_relative_path = "../tiny_dataset/C"
    c_filedir_path = f"{current_dir}/{c_filedir_relative_path}"

    # make a DataLoader object to test the helper functions
    dataloader = DataLoader(c_path=c_filedir_path)

    with open(f"{c_filedir_path}/two-sum-1.txt", "r") as f:
        c_code = f.read()

    c_code = dataloader.clean_c(c_code)
    tokens = dataloader.tokenize_c(c_code)

    print(tokens)

def test_c_token_check():
    token = "hello++"

    dataloader = DataLoader()

    print(dataloader.check_c_token(token))

def test_asm_tokenization():

    asm_filedir_relative_path = "../tiny_dataset/ASM"
    asm_filedir_path = f"{current_dir}/{asm_filedir_relative_path}"

    dataloader = DataLoader()

    with open(f"{asm_filedir_path}/ASM_two-sum-1.txt", "r") as f:
        asm_code = f.read()

    tokens = dataloader.tokenize_asm(asm_code)

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

    c_filedir_relative_path = "../tiny_dataset/C"
    c_filedir_path = f"{current_dir}/{c_filedir_relative_path}"
    asm_filedir_relative_path = "../tiny_dataset/ASM"
    asm_filedir_path = f"{current_dir}/{asm_filedir_relative_path}"

    dataloader = DataLoader(c_path=c_filedir_path, asm_path=asm_filedir_path)

    print(dataloader.stats)
    print(dataloader.load_data()[0])

if __name__ == "__main__":
    # test_c_tokenization()
    # test_c_token_check()
    # test_asm_tokenization()
    # test_c_vocab()
    # test_asm_vocab()
    test_load_data()
