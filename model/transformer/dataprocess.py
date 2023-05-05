import os, re, csv
import numpy as np
import tensorflow as tf
from nltk.tokenize import wordpunct_tokenize

START_TOKEN = "<START>"
END_TOKEN = "<STOP>"
PAD_TOKEN = "<PAD>"
UNK_TOKEN = "<UNK>"
C_NUM_TOKEN = "<CNUM>"

C_PUNCT = [' ', ':', ';', '=', '~', '+', '-', '*', '/', ',', '.', 
            '<', '>', '&', '|', '%', '?', '{', '}', '^', '!', 
            '[', ']', '(', ')']

VALID_NUMS = [0, 1, 2]

class Translator:
    """
    TRANSLATOR: Tokenization, etc.
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
    
    def tokenize_c(self, c_code, asm_string_to_token=None, asm_num_to_token=None):
        """
        Tokenization of components of the C file to strings
        
        @params
        - c_code: string of code
        - asm_string_to_token: 1-to-1 mapping of string literals to tokens (can be used with tokenizing ASM)
        - asm_num_to_token: 1-to-1 mapping of numbers to tokens (can be used when tokenizing C)

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


        if asm_string_to_token and asm_num_to_token:
            for i, token in enumerate(c_tokens):

                try:
                    test_str_token = '"' + token + '"'
                    # print(test_str_token)
                    if test_str_token in asm_string_to_token:
                        c_tokens[i] = asm_string_to_token[test_str_token]
                        continue
                except:
                    pass

                if token in asm_num_to_token:
                    c_tokens[i] = asm_num_to_token[token]

        # filtering things
        new_tokens = []
        for token in c_tokens:

            # skips
            if token in ('""', '\n'):
                continue

            # replacing numerics
            if self.c_token_is_numeric(token):
                new_tokens.append(C_NUM_TOKEN)
                continue

            new_tokens.append(token)

        c_tokens = new_tokens

        
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
        if re.match(r'[^\w\s]+(?=[^\w\s])', token):
            return True
        return False
    
    def c_token_is_numeric(self, token):
        """
        Returns true if the token is:
        - number
        - hex (e.g. 0xffffffff)
        - binary (e.g. 0x11)
        """
        token = token.lower()
        if re.match(r'^0b[01]+$', token):
            return True
        if re.match(r'^0x[0-9a-f]+$', token):
            return True
        try:
            int(token)
            return True
        except:
            return False
        
    def detokenize_c_from_tensor(self, c_vals, c_vocab):
        """
        Given a tensor (of ints) and vocab, output string of C code
        """
        out = []

        c_vals = c_vals.numpy()
        c_vals = c_vals.flatten()

        c_index_to_strtoken  = {v: k for k, v in c_vocab.items()}

        for i in range(len(c_vals)):
            out.append(c_index_to_strtoken[c_vals[i]])

        return " ".join(out)

    def tokenize_asm(self, asm_code):
        """
        Tokenization of components of the ASM file to strings
        
        @params
        - asm_code: string of code

        @returns
        - asm_tokens: list of tokens extracted from asm_code
        - asm_string_to_token: 1-to-1 mapping of string literals to tokens (can be used with tokenizing ASM)
        - asm_num_to_token: 1-to-1 mapping of numbers to tokens (can be used when tokenizing C)
        """

        # replace >= 2 spaces with 1 space
        asm_code = re.sub(r'\n', ' ', asm_code)
        asm_code = re.sub(r'\s{2,}', ' ', asm_code)
        asm_code = re.sub(r'\t', ' ', asm_code)
        asm_tokens = asm_code.split(" ")

        # we add to this list rather than deleting from asm_tokens
        new_asm_tokens = []

        # (str) true_string: (str) string_token
        asm_string_to_token = {}
        # (str) true_num: (str) num_token
        asm_num_to_token = {}
        # (str) true_mem_movement: (str) mem_token
        asm_mem_to_token = {}

        for asm_token in asm_tokens:
            # remove strange split cases
            if asm_token in ('', '"', '""'):
                continue

            # print(asm_token)

            # remove commas from end, if applicable
            if asm_token[-1] == ",":
                asm_token = asm_token[:-1]


            need_to_check = True



            if need_to_check:

            # TOKENIZING STRINGS
            # "any string" -> <STRING_1>

            # C code will follow same tokenizing convention:
            # if str_ASM == str_C:
            #   str_ASM -> <STRING_1>
            #   str_C -> <STRING_1>

                if asm_token in asm_string_to_token:
                    asm_token = asm_string_to_token[asm_token]
                    need_to_check = False

                elif self.asm_token_is_string(asm_token):

                    # add to dict
                    asm_string_to_token[asm_token] = f'<STRING_{len(asm_string_to_token)}>'
                    asm_token = asm_string_to_token[asm_token]
                    need_to_check = False

            
            if need_to_check:

            # TOKENIZING NUMBERS
            # $num -> $<NUMBER_1>
            # num -> <NUMBER_1>

            # C code will follow same tokenizing convention:
            # if num_ASM == num_C:
            #   num_ASM -> <NUMBER_1>
            #   num_C -> <NUMBER_1>

                test_asm_token_num = self.asm_token_num_handler(asm_token)
                if test_asm_token_num:
                    
                    num_test_token1 = asm_token         # if looks like num
                    num_test_token2 = asm_token[1:]     # if looks like $num

                    if num_test_token1 in asm_num_to_token:
                        asm_token = asm_num_to_token[num_test_token1]
                    elif num_test_token2 in asm_num_to_token:
                        asm_token = '$' + asm_num_to_token[num_test_token2]
                    else:
                        asm_num_to_token[test_asm_token_num] = f'<NUMBER_{len(asm_num_to_token)}>'
                        asm_token = asm_num_to_token[test_asm_token_num]

                    need_to_check = False


            if need_to_check:

            # TOKENIZING MEMORY
            # mem(%reg) -> <MEMORY_1>(%reg)

            # No need to worry about preserving 1-to-1 for C

                test_asm_mem_num = self.asm_token_memory_handler(asm_token)
                if test_asm_mem_num:

                    mem_test_token = asm_token.split('(')[0]
                    rest = asm_token.split('(')[1]

                    if test_asm_mem_num in asm_mem_to_token:

                        first = asm_mem_to_token[mem_test_token]

                        asm_token = first + '(' + rest

                    else:
                        asm_mem_to_token[test_asm_mem_num] = f'<MEMORY_{len(asm_mem_to_token)}>'
                        asm_token = asm_mem_to_token[test_asm_mem_num] + '(' + rest

                
            new_asm_tokens.append(asm_token)


        asm_tokens = new_asm_tokens

        # add start token to beginning
        asm_tokens.insert(0, START_TOKEN)
        
        # add end token to end
        asm_tokens.append(END_TOKEN)

        return asm_tokens, asm_string_to_token, asm_num_to_token
    

    def asm_token_is_string(self, asm_token):
        """
        @params
        - asm_token: string of asm token

        @returns
        - True if is string literal, False otherwise
        """
        return re.match(r'"([^"]*)"', asm_token)


    def asm_token_num_handler(self, asm_token):
        """
        @params
        - asm_token: string of asm token

        @returns
        - Number (int) if is numeric (either $num or num), None otherwise
        """

        try:
            # case of just num
            test = int(asm_token)
            if test in VALID_NUMS:
                return None
            return str(test)
        except:
            if asm_token[0] != '$':
                return None
            else: 
                # case of $num
                asm_token = asm_token[1:]
                try:
                    test = int(asm_token)
                    if test in VALID_NUMS:
                        return None
                    return str(test)
                except:
                    return None
    
    def asm_token_memory_handler(self, asm_token):
        """
        @params
        - asm_token: string of asm token

        @returns
        - Memory (string) if is string literal, None otherwise
        """
        if re.match(r'.*\(.*\)', asm_token):
            return asm_token.split('(')[0]
        else:
            return None

    
    def generate_tensor_from_vocab(self, vocab, code_tokens, max_length=2000):
        """
        Generates a tensor of token sequences in their integer
        representation.

        @params
        - vocab: dict{token: int_value}
        - code_tokens: list of tokens
        - max_length: arg for chopping off extra data after max length

        @returns
        - out: np.array of values from the appropriate vocabulary dictionary
        """

        out = np.ones(max_length)
        out = out * np.float64(vocab[PAD_TOKEN])

        for i, token in enumerate(code_tokens):
            if i >= max_length:
                break

            if token in vocab:
                out[i] = vocab[token]
            else:
                out[i] = vocab[UNK_TOKEN]

        return tf.convert_to_tensor(out, dtype=tf.int64)
    

class DataLoader(Translator):
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
        'avg_asm_code_length': 0,        # in number of tokens
        'c_vocab_size': 0,
        'asm_vocab_size': 0
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
        for _ in os.listdir(c_path):
            c_count += 1
        for _ in os.listdir(asm_path):
            asm_count += 1
        if c_count != asm_count:
            raise Exception("The C and Assembly directories do not have " + \
                "the same number of files.")
        self.stats['num_examples'] = c_count

        self.generate_vocabulary()



    def generate_c_vocabulary(self):
        """
        DEPRECATED!

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

            print(f"\rReading C file: {file_name}\t\t\t", end="")
        
            with open(f"{self.c_path}/{file_name}", "r") as c_file:
                c_code = c_file.read()

            
            # c_code = self.clean_c(c_code)
            # test = re.sub("\n", "", c_code)
            # if len(test) == 0:
            #     continue

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

        self.stats['c_vocab_size'] = len(c_vocab_tokens_list)

        print()
        return self.c_vocab
    
    def generate_asm_vocabulary(self):
        """
        DEPRECATED!

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

            print(f"\rReading ASM file: {file_name}\t\t\t", end="")
        
            with open(f"{self.asm_path}/{file_name}", "r") as asm_file:
                asm_code = asm_file.read()

            # test = re.sub("\n", "", asm_code)
            # if len(test) == 0:
            #     continue

            tokens, _, _ = self.tokenize_asm(asm_code)
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

        self.stats['asm_vocab_size'] = len(asm_vocab_tokens_list)

        print()
        return self.asm_vocab
    

    def generate_vocabulary(self):
        """
        Generates the ASM and C vocabulary (a dictionary of mappings from 
        tokens to integer values) all at once

        @params
        - None

        @returns
        - self.asm_vocab: list of tokens extracted from asm_code
        - self.c_vocab: list of tokens extracted from c_code
        """
        asm_vocab_tokens_set = set()
        c_vocab_tokens_set = set()
        asm_avg_tokens = 0
        c_avg_tokens = 0

        for asm_file_name in sorted(os.listdir(self.asm_path)):
            # c_file_name = "_".join(asm_file_name.split('_')[1:])
            c_file_name = asm_file_name[4:]

            print(f"\rASM file: {asm_file_name} | C file: {c_file_name} \t\t\t", end="")

            with open(f"{self.asm_path}/{asm_file_name}", "r") as asm_file:
                asm_code = asm_file.read()

            with open(f"{self.c_path}/{c_file_name}", "r") as c_file:
                c_code = c_file.read()

            asm_tokens, asm_string_to_token, asm_num_to_token = self.tokenize_asm(asm_code)
            c_tokens = self.tokenize_c(c_code, asm_string_to_token, asm_num_to_token)

            asm_vocab_tokens_set = asm_vocab_tokens_set.union(set(asm_tokens))
            c_vocab_tokens_set = c_vocab_tokens_set.union(set(c_tokens))

            asm_avg_tokens += len(asm_tokens)
            c_avg_tokens += len(c_tokens)

            if len(asm_tokens) > self.stats['max_asm_code_length']:
                self.stats['max_asm_code_length'] = len(asm_tokens)

            if len(c_tokens) > self.stats['max_c_code_length']:
                self.stats['max_c_code_length'] = len(c_tokens)

        asm_vocab_tokens_list = sorted(list(asm_vocab_tokens_set))
        asm_vocab_tokens_list.remove(START_TOKEN)
        asm_vocab_tokens_list.remove(END_TOKEN)
        asm_vocab_tokens_list.insert(0, UNK_TOKEN)
        asm_vocab_tokens_list.insert(0, END_TOKEN)
        asm_vocab_tokens_list.insert(0, START_TOKEN)
        asm_vocab_tokens_list.insert(0, PAD_TOKEN)

        c_vocab_tokens_list = sorted(list(c_vocab_tokens_set))
        c_vocab_tokens_list.remove(START_TOKEN)
        c_vocab_tokens_list.remove(END_TOKEN)
        c_vocab_tokens_list.insert(0, UNK_TOKEN)
        c_vocab_tokens_list.insert(0, END_TOKEN)
        c_vocab_tokens_list.insert(0, START_TOKEN)
        c_vocab_tokens_list.insert(0, PAD_TOKEN)

        for i, token in enumerate(asm_vocab_tokens_list):
            self.asm_vocab[token] = i
        for i, token in enumerate(c_vocab_tokens_list):
            self.c_vocab[token] = i

        self.stats['avg_asm_code_length'] = asm_avg_tokens / \
            self.stats['num_examples']
        self.stats['avg_c_code_length'] = c_avg_tokens / \
            self.stats['num_examples']
        self.stats['asm_vocab_size'] = len(asm_vocab_tokens_list)
        self.stats['c_vocab_size'] = len(c_vocab_tokens_list)

        print()

        return self.asm_vocab, self.c_vocab



    def load_data(self, asm_vocab=None, c_vocab=None, max_asm_len=500, max_c_len=500):
        """
        Returns all necessary data for the transformer model.

        @params:
        - asm_vocab: Assembly vocabulary
        - c_vocabulary: C vocabulary

        @returns:
        - asm_vals: np.array of size (num_examples, max_c_code_length)
        - c_vals: np.array of size (num_examples, max_asm_code_length)
        - self.stats: stats dict 
        """

        if asm_vocab is None:
            asm_vocab = self.asm_vocab

        if c_vocab is None:
            c_vocab = self.c_vocab

        c_vals = np.zeros(shape=(
            self.stats['num_examples'], 
            max_c_len
        ))

        asm_vals = np.zeros(shape=(
            self.stats['num_examples'], 
            max_asm_len
        ))

        for i, asm_file_name in enumerate(sorted(os.listdir(self.asm_path))):
            c_file_name = asm_file_name[4:]

            with open(f"{self.asm_path}/{asm_file_name}", "r") as asm_file:
                asm_code = asm_file.read()

            with open(f"{self.c_path}/{c_file_name}", "r") as c_file:
                c_code = c_file.read()

            asm_tokens, asm_string_to_token, asm_num_to_token = self.tokenize_asm(asm_code)
            c_tokens = self.tokenize_c(c_code, asm_string_to_token, asm_num_to_token)

            

            asm_arr = self.generate_tensor_from_vocab(asm_vocab, 
                                                           asm_tokens, 
                                                           max_asm_len)
            c_arr = self.generate_tensor_from_vocab(c_vocab, c_tokens, 
                                                max_c_len)
        


            asm_vals[i, :] = asm_arr
            c_vals[i, :] = c_arr
    
        return asm_vals.astype(int), c_vals.astype(int), self.stats
    
    
def write_vocab_as_csv(vocab, file_path):

    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Key', 'Value'])
        for key, value in vocab.items():
            writer.writerow([key, value])

def read_vocab_from_csv(file_path):
    """
    Returns a dictionary of vocab
    """

    with open(file_path, mode='r') as file:

        # Create a CSV reader object
        reader = csv.reader(file)

        # Create an empty dictionary to store the key-value pairs
        data = {}

        # Iterate over each row in the CSV file
        for row in reader:

            if row[0] == "Key" or row[1] == "Value":
                continue
            
            # Add the key-value pair to the dictionary
            data[row[0]] = row[1]
    
    return data


def partition_into_batches(X, Y, batch_size): 
    '''
    Randomly partitions dataset into batches each containing batch_size examples
    '''

    # get number of training examples
    num_examples = X.shape[0]

    # generate a random permutation of size m for nums 0 to (m-1)
    rand_idx = np.random.permutation(np.arange(num_examples))

    # reorder X_temp, Y_temp in the exact same way
    # we cannot just shuffle both because we need each X_i to correspond
    # to the correct Y_i
    X_temp = tf.gather(X, rand_idx)
    Y_temp = tf.gather(Y, rand_idx)

    X_batches = []
    Y_batches = []

    # we will consider batches that are of length batch_size only
    num_batches = int(np.floor(num_examples / batch_size))

    for i in range(num_batches):
        X_batches.append(X_temp[(i*batch_size):((i+1)*batch_size)])
        Y_batches.append(Y_temp[(i*batch_size):((i+1)*batch_size)])

    return X_batches, Y_batches


