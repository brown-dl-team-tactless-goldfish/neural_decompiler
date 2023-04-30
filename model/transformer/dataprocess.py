import os, re
import numpy as np
from nltk.tokenize import wordpunct_tokenize

START_TOKEN = "<START>"
END_TOKEN = "<STOP>"
PAD_TOKEN = "<PAD>"

C_PUNCT = [' ', ':', ';', '=', '~', '+', '-', '*', '/', ',', '.', 
            '<', '>', '&', '|', '%', '?', '{', '}', '^', '!', 
            '[', ']', '(', ')']

class Translator:
    """
    Translator: Tokenization, etc.
    """

    def __init__(self):
        pass

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
        c_code = self.clean_c(c_code)
        c_code_lines = c_code.splitlines()
        c_tokens = []

        # generates tokens
        for line in c_code_lines:
            line_tokens = wordpunct_tokenize(line)

            c_tokens.extend(line_tokens + ["\n"])

        for i, token in enumerate(c_tokens):
            if self.check_c_token(token) == True:

                c_tokens.pop(i)

                # print("found exception: ", token)

                for j, char in enumerate(token):

                    # print(char)

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
        
        @params
        - asm_code: string of code

        @returns
        - asm_tokens: list of tokens extracted from c_code
        """
        
        asm_tokens = []

        # replace >= 2 spaces with 1 space
        asm_code = re.sub(r'\s{2,}', ' ', asm_code)
        asm_code = re.sub(r'\n', ' ', asm_code)

        asm_tokens = asm_code.split(" ")

        # add start token to beginning
        asm_tokens.insert(0, START_TOKEN)
        
        # add end token to end
        asm_tokens.append(END_TOKEN)

        return asm_tokens
    
    def generate_numpy_array_from_vocab(self, vocab, code_tokens, max_length):
        """
        Generates an np array of token sequences in their integer
        representation.

        @params
        - vocab: dict{token: int_value}
        - code_tokens: list of tokens
        - max_length: arg for chopping off extra data after max length

        @returns
        - out: np.array of values from the appropriate vocabulary dictionary
        """

        out = np.ones(max_length)
        out = out * vocab[PAD_TOKEN]

        for i, token in enumerate(code_tokens):
            if i >= max_length:
                break

            out[i] = vocab[token]

        return out

class DataLoader(DataProcessor):
    """
    DATALOADER: Loads and preprocesses training data.
    """
    
    # fields
    c_path = ""
    asm_path = ""
    c_vocab = {}
    asm_vocab = {}
    stats = {
        'num_examples': 0,
        'max_c_code_length': 0,         # in number of tokens
        'max_asm_code_length': 0,       # in number of tokens
        'avg_c_code_length': 0,         # in number of tokens
        'avg_asm_code_length': 0        # in number of tokens
    }

    def __init__(self, c_path = "", asm_path = ""):
        """
        Upon initialization, generates the C and ASM vocabularies (dictionaries
        of mappings from tokens to integer values)

        @params
        - c_path: full path to the directory containing all C code
        - asm_path: full path to the directory containing all ASM code

        @returns
        - None
        """
        super().__init__()

        self.c_path = c_path
        self.asm_path = asm_path

        c_count, asm_count = (0, 0)
        for f in os.listdir(c_path):
            c_count += 1
        for f in os.listdir(asm_path):
            asm_count += 1
        if c_count != asm_count:
            raise Exception("The C and Assembly directories do not have " + \
                "the same number of files.")
        self.stats['num_examples'] = c_count

        self.generate_c_vocabulary()
        self.generate_asm_vocabulary()

    def generate_c_vocabulary(self):
        """
        Generates the C vocabulary (a dictionary of mappings from 
        tokens to integer values)

        @params
        - None

        @returns
        - self.c_vocab: list of tokens extracted from c_code
        """

        c_vocab_tokens_set = set()
        avg_tokens = 0
        for file_name in sorted(os.listdir(self.c_path)):
        
            with open(f"{self.c_path}/{file_name}", "r") as c_file:
                c_code = c_file.read()

            tokens = self.tokenize_c(c_code)

            avg_tokens += len(tokens)

            if len(tokens) > self.stats['max_c_code_length']:
                self.stats['max_c_code_length'] = len(tokens)

            c_vocab_tokens_set = c_vocab_tokens_set.union(set(tokens))

        self.stats['avg_c_code_length'] = avg_tokens / \
            self.stats['num_examples']
        
        c_vocab_tokens_list = sorted(list(c_vocab_tokens_set))
        c_vocab_tokens_list.insert(0, PAD_TOKEN)

        for i, token in enumerate(c_vocab_tokens_list):
            self.c_vocab[token] = i

        return self.c_vocab
    
    def generate_asm_vocabulary(self):
        """
        Generates the ASM vocabulary (a dictionary of mappings from 
        tokens to integer values)

        @params
        - None

        @returns
        - self.asm_vocab: list of tokens extracted from c_code
        """

        asm_vocab_tokens_set = set()
        avg_tokens = 0
        for file_name in sorted(os.listdir(self.asm_path)):
        
            with open(f"{self.asm_path}/{file_name}", "r") as asm_file:
                asm_code = asm_file.read()

            tokens = self.tokenize_asm(asm_code)
            avg_tokens += len(tokens)

            if len(tokens) > self.stats['max_asm_code_length']:
                self.stats['max_asm_code_length'] = len(tokens)

            asm_vocab_tokens_set = asm_vocab_tokens_set.union(set(tokens))
        
        self.stats['avg_asm_code_length'] = avg_tokens / \
            self.stats['num_examples']

        asm_vocab_tokens_list = sorted(list(asm_vocab_tokens_set))
        asm_vocab_tokens_list.insert(0, PAD_TOKEN)

        for i, token in enumerate(asm_vocab_tokens_list):
            self.asm_vocab[token] = i

        return self.asm_vocab

    def load_data(self):
        """
        Returns all necessary data for the transformer model.

        @params:
        - None

        @returns:
        - c_vals: np.array of size (num_examples, max_c_code_length)
        - asm_vals: np.array of size (num_examples, max_asm_code_length)
        - self.stats: stats dict 
        """

        c_vals = np.zeros(shape=(
            self.stats['num_examples'], 
            self.stats['max_c_code_length']
        ))

        asm_vals = np.zeros(shape=(
            self.stats['num_examples'], 
            self.stats['max_asm_code_length']
        ))

        for i, c_filename in enumerate(sorted(os.listdir(self.c_path))):
            with open(f"{self.c_path}/{c_filename}", "r") as c_file:
                c_code = c_file.read()
            c_tokens = self.tokenize_c(c_code)

            c_arr = self.generate_numpy_array_from_vocab(self.c_vocab, c_tokens, 
                                                self.stats['max_c_code_length'])
            c_vals[i, :] = c_arr
        
        for i, asm_filename in enumerate(sorted(os.listdir(self.asm_path))):
            with open(f"{self.asm_path}/{asm_filename}", "r") as asm_file:
                asm_code = asm_file.read()
            asm_tokens = self.tokenize_asm(asm_code)

            asm_arr = self.generate_numpy_array_from_vocab(self.asm_vocab, 
                                                           asm_tokens, 
                                            self.stats['max_asm_code_length'])
            asm_vals[i, :] = asm_arr
    
        return c_vals, asm_vals, self.stats

