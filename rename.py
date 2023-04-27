import re

src_code = '''
int comparator(const void *a, const void *b)
{
    int l = *(const int*)a;
    int r = *(const int*)b;
    return l-r;
}
int** threeSum(int* arr, int size, int* returnSize) 
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
code = src_code

while '{' in code:
    code = re.sub(r'\{[^{}]*\}', '', code)  

code = re.findall(r'\((.*?)\)', code)
code = ', '.join(code)
code = code.split(', ')
print(code)
param_names = [x.split(' ')[-1].split('*')[-1] for x in code]
print(param_names)

variable_names = sorted(set(re.findall(r"(?<=[ \(])[a-z]+(?=[, ;+*\/\)])", src_code)).union(set(param_names)))

reserved_list = set(['auto', 'else', 'long', 'switch', 'break',	'enum',	'register',	'typedef', 'case', 	'extern', 'return',	'union', 'char', 'float', 'short', 'unsigned', 'const', 'for', 'signed', 'void', 'continue', 'goto', 'sizeof', 'volatile', 'default', 'if', 'static', 'while', 'do', 'int',	'struct', 'double', 'NULL', 'nullptr'])

operators = [' ', ';', '=', '~', '+', '-', '*', '/', ',', '.', '<', '>', '&', '|', '%', '?', '{', '}', '^', '!', '[', ']', '(', ')']

variable_names = [x for x in variable_names if x not in reserved_list]

all_checks = []
var_names_to_new_vars = {}

for i, var_name in enumerate(variable_names):
    var_names_to_new_vars[var_name] = 'var_' + str(i)

    for op1 in operators:
        for op2 in operators:
            all_checks.append(op1 + var_name + op2)

for to_check in all_checks:
    before = to_check[0]
    after = to_check[-1]
    between = to_check[1:-1]
    src_code = src_code.replace(to_check, before + var_names_to_new_vars[between] + after)

print(src_code)