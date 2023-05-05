import os

def search(folder_path, conditions, remove=False):
    '''
    In a given folder of files (ASM or C), find + print all files
    which meet the given conditions
    '''
    count = 0

    for filename in sorted(list(os.listdir(folder_path))):
        with open(f'{folder_path}/{filename}', 'r') as f:
            FINAL_SRC_CODE = f.read()

        # if all conditions met, print filename + count!
        if conditions(FINAL_SRC_CODE):
            count += 1
            print(count, filename)

            if remove:
                os.remove(f'{folder_path}/{filename}')

if __name__ == "__main__":
    # example condition to search for in folder of code
    def conditions(FINAL_SRC_CODE):
        a = len(FINAL_SRC_CODE[112:]) < 10 # suspiciously small file!
        b = 'define' in FINAL_SRC_CODE # we don't want defines!

        return a and b

    folder_path = './data/leetcode_data_FINAL/C_COMPILED_FILES'
    search(folder_path, conditions)
