import re

# src_code = '''
# #include<stdlib.h>
# #include<stdio.h>
# #include<string.h>
# #include<stdbool.h>
# #include<stdint.h>
# #include<math.h>
# bool help(int x, int* y,int *z) {
# }
# bool isMonotonic(int* nums, int numsSize) {
# int idx = 1;
# while(idx+1 < numsSize) {
# if(nums[idx-1] < nums[idx]) {
# while(idx+1 < numsSize && nums[idx] == nums[idx+1]) {
# idx++;
# }
# if(idx+1 < numsSize && nums[idx] > nums[idx+1]) return false;
# }
# if(nums[idx-1] > nums[idx]) {
# while(idx+1 < numsSize && nums[idx] == nums[idx+1]) {
# idx++;
# }
# if(idx+1 < numsSize && nums[idx] < nums[idx+1]) return false;
# }
# idx++;
# }
# return true;
# }
# '''

FINAL_SRC_CODE = '''
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
}

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
}

int comparator(const void *a,const void *b)
{
    int l = *(const int*)a;
    int r = *(const int*)b;
    return l-r;
}

int** threeSum(int* arr, int size,int* returnSize) 
{
    if(arr == NULL || size == 0)
        return NULL;

    qsort((void *)arr, size, sizeof(arr[0]),comparator );
    int count = 0;
    int **res = NULL;

    for(int i = 0; i < size; i++)
    {

        int start = i + 1;
        int end = size - 1;
        int sum;

        if(i > 0 && arr[i] == arr[i - 1])
            continue;

        while(start < end )
        {
            
            sum = arr[i] + arr[start] + arr[end];
            if(sum == 0)
            {
                count++;
                res = (int **)realloc(res, sizeof(int *) * count);
                res[count - 1] = (int *) malloc(sizeof(int)*3);
                res[count - 1][0] = arr[i];
                res[count - 1][1] = arr[start];
                res[count - 1][2] = arr[end];
                while(start < end && arr[start] == arr[start + 1])
                    start++;
                while(start < end && arr[end] == arr[end -1])
                    end--;
                
                start++;
                end--;
            }
            else if(sum > 0)
                end--;
            else
                start++;
        }
    }
    *returnSize = count;
    return res;
}
'''
src_code = re.sub(r'struct\s+\w+\s*{([^}]*)}', '', FINAL_SRC_CODE)

param_names = src_code
# func_names = set()
# struct_names = set()

while '{' in param_names:
    param_names = re.sub(r'\{[^{}]*\}', '', param_names)

func_names = set([x.split('(')[0] for x in param_names.strip().split() if '(' in x])
param_names = re.findall(r'\((.*?)\)', param_names)
param_names = [[i.strip().split()[-1].split('*')[-1] for i in x.split(',')] for x in param_names]

temp = []

for x in param_names:
    temp.extend(x)

param_names = temp

print("PARAM NAMES: ", param_names)

reserved_list = set(['auto', 'else', 'long', 'switch', 'break',	'enum',	'register',	'typedef', 
                     'case', 'extern', 'return', 'union', 'char', 'float', 'short', 'unsigned', 
                     'const', 'for', 'signed', 'void', 'continue', 'goto', 'sizeof', 'volatile', 
                     'default', 'if', 'static', 'while', 'do', 'int',	'struct', 'double', 'NULL', 'nullptr', 
                     'bool', 'true', 'false', 'int8_t', 'uint8_t', 'int16_t', 'uint16_t', 'int32_t', 'uint32_t', 
                     'int64_t', 'uint64_t', 'size_t', 'size_t', 'ssize_t', 'NAN', 'INFINITY', 'M_PI', 'SIZE_MAX'])

operators = [' ', ';', '=', '~', '+', '-', '*', '/', ',', '.', 
             '<', '>', '&', '|', '%', '?', '{', '}', '^', '!', 
             '[', ']', '(', ')', '\n']

variable_names = [x for x in re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*(?=[ ,;=\[])", src_code) if x not in reserved_list]
print("VAR NAMES: ", variable_names)

all_names = sorted([elt for elt in set(param_names + variable_names) if elt not in func_names])
print("ALL NAMES: ", all_names)

all_checks = []
var_names_to_new_vars = {}

for i, var_name in enumerate(all_names):
    var_names_to_new_vars[var_name] = 'var_' + str(i)

    for op1 in operators:
        for op2 in operators:
            all_checks.append(op1 + var_name + op2)

for to_check in all_checks:
    before = to_check[0]
    after = to_check[-1]
    between = to_check[1:-1]
    FINAL_SRC_CODE = FINAL_SRC_CODE.replace(to_check, before + var_names_to_new_vars[between] + after)

print(FINAL_SRC_CODE)



# code = src_code

# while '{' in code:
#     code = re.sub(r'\{[^{}]*\}', '', code)  

# code = re.findall(r'\((.*?)\)', code)
# code = ', '.join(code)
# code = code.split(', ')

# param_names = [x.split(' ')[-1].split('*')[-1] for x in code]
# print("PARAM NAMES", param_names)

# variable_names = sorted(set(re.findall(r"(?<=[ \(])[a-z]+(?=[, ;+*\/\)])", src_code)).union(set(param_names)))
# reserved_list = set(['auto', 'else', 'long', 'switch', 'break',	'enum',	'register',	'typedef', 'case', 	'extern', 'return',	'union', 'char', 'float', 'short', 'unsigned', 'const', 'for', 'signed', 'void', 'continue', 'goto', 'sizeof', 'volatile', 'default', 'if', 'static', 'while', 'do', 'int',	'struct', 'double', 'NULL', 'nullptr', 'true', 'false'])

# operators = [' ', ';', '=', '~', '+', '-', '*', '/', ',', '.', '<', '>', '&', '|', '%', '?', '{', '}', '^', '!', '[', ']', '(', ')', '\n']

# variable_names = [x for x in variable_names if x not in reserved_list]
# print("ALL VAR NAMES", variable_names)

# all_checks = []
# var_names_to_new_vars = {}

# for i, var_name in enumerate(variable_names):
#     var_names_to_new_vars[var_name] = 'var_' + str(i)

#     for op1 in operators:
#         for op2 in operators:
#             all_checks.append(op1 + var_name + op2)

# print("ALL CHECKS", all_checks)
# for to_check in all_checks:
#     before = to_check[0]
#     after = to_check[-1]
#     between = to_check[1:-1]
#     src_code = src_code.replace(to_check, before + var_names_to_new_vars[between] + after)

# print(src_code)