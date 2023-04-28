import os, re
from nltk.tokenize import wordpunct_tokenize


START_TOKEN = "<START>"
END_TOKEN = "<END>"

C_PUNCT = [
    "(", ")", "+", "-", "{", "}", "/", "*", "&", "[", "]"
]


class DataLoader:
    """
    A class that loads and preprocesses training data
    """
    
    # fields
    c_path = ""
    asm_path = ""

    c_vocab = {}
    asm_vocab = {}

    def __init__(self, c_path = "", asm_path = ""):
        self.c_path = c_path
        self.asm_path = asm_path

    def generate_c_vocabulary(self):

        for file_name in sorted(list(os.listdir(self.c_path))):
        
            with open(f"{self.c_path}/{file_name}", "r") as c_file:
                c_code = c_file.read()

        return
    
    
    def generate_asm_vocabulary(self):
        
        for file_name in sorted(list(os.listdir(self.asm_path))):
        
            with open(f"{self.asm_path}/{file_name}", "r") as asm_file:
                asm_code = asm_file.read()

        return
    
    def clean_c(self, c_code):
        """
        Removes all includes and tabs from the code

        @params
        - c_code: string of code

        @returns
        - c_code: string of code that has been cleaned
        """
        
        c_code = re.sub(r'#include\s*(<|")\s*.*?\s*(>|")', '', c_code)
        c_code = re.sub(r'\t', '', c_code)
        c_code = re.sub(r' {2,}', ' ', c_code)

        return c_code
    
    def tokenize_c(self, c_code):
        """
        Tokenization of components of the C file to unique integer values
        
        @params
        - c_code: string of code

        @returns
        - c_tokens: list of tokens extracted from c_code
        """

        c_code_lines = c_code.splitlines()

        c_tokens = []

        # generates tokens
        for line in c_code_lines:
            line_tokens = wordpunct_tokenize(line)

            c_tokens.extend(line_tokens + ["\n"])

        for i, token in enumerate(c_tokens):
            if self.check_c_token(token) == True:

                c_tokens.pop(i)

                print("found exception: ", token)

                for j, char in enumerate(token):

                    print(char)

                    c_tokens.insert(i + j, char)

        # removes all newlines at the beginning of the code
        while c_tokens[0] == "\n":
            c_tokens.pop(0)

        # removes all newlines from the end of the code
        while c_tokens[-1] == "\n":
            c_tokens.pop()
        
        # add a start token to the beginning of the code
        c_tokens.insert(0, START_TOKEN)

        # add an end token to the end of the code
        c_tokens.append(END_TOKEN)

        return c_tokens
    
    def check_c_token(self, token):
        """
        Returns true if the token needs to be split further.
        """
        # handles cases such as '++)'
        if re.match('[^\w\s]+(?=[^\w\s])', token):
            return True
        return False


    def tokenize_asm(self, asm_code):
        """
        Tokenization of components of the ASM file to unique integer values
        """
        
        asm_tokens = []

        # replace >= 2 spaces with 1 space
        asm_code = re.sub(r'\s{2,}', ' ', asm_code)
        asm_code = re.sub(r'\n', ' ', asm_code)

        asm_tokens = asm_code.split(" ")

        return asm_tokens


