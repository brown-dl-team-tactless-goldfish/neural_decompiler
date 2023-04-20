#define MAX_ELEMENTS 1000 

typedef struct
{
    int arr[MAX_ELEMENTS];
    int top;
}Stack;

int isStackEmpty(Stack * tmp_stack)
{
    if(tmp_stack->top == -1)
        return 1;
    else
        return 0;
}

int isStackFull(Stack * tmp_stack)
{
    if(tmp_stack->top == MAX_ELEMENTS-1)
        return 1;
    else
        return 0;
}

void push(Stack * tmp_stack, int element)
{
    if(isStackFull(tmp_stack))
        return;
    
    tmp_stack->arr[++(tmp_stack->top)] = element;
}

int pop(Stack * tmp_stack)
{
    if(isStackEmpty(tmp_stack))
        return INT_MIN;
    
    return tmp_stack->arr[(tmp_stack->top)--];
}

int peek(Stack * tmp_stack, int index)
{
    return tmp_stack->arr[index];
}

int calPoints(char ** ops, int opsSize)
{
    int i=0;
    Stack tmp_stack;
    tmp_stack.top = -1;
    
    while(i<opsSize)
    {
        if(ops[i][0] == '+')
        {
            push(&tmp_stack, peek(&tmp_stack, tmp_stack.top) + peek(&tmp_stack, tmp_stack.top-1) );
        }
        else if(ops[i][0] == 'D')
        {
            push(&tmp_stack, peek(&tmp_stack, tmp_stack.top) * 2);
        }
        else if(ops[i][0] == 'C')
        {
            pop(&tmp_stack);
        }
        else
        {
            char sign = ops[i][0];
            int val = 0;
            if(sign == '-')
            {
                int j=1;
                while(ops[i][j] != '\0')
                {
                    val = (val*10) + (ops[i][j] - '0');
                    j++;
                }
                
                val *= -1;
            }
            else
            {
                int j=0;
                while(ops[i][j] != '\0')
                {
                    val = (val*10) + (ops[i][j] - '0');
                    j++;
                }
                
            }
            push(&tmp_stack, val);
        }
        
        i++;
    }
    
    int count = 0;
    
    while(!isStackEmpty(&tmp_stack))
    {
        count += pop(&tmp_stack);
    }
    return count;
}