

bool isValid(char * s){
    char *stack = malloc(strlen(s));
    assert(stack);
    int top = 0;
    int i;
    char c, e;
	bool ret = false;
    
    for (i = 0; i < strlen(s); i++) {
        c = s[i];
        if (c == ')') {
            if (top == 0)
                goto out;
            e = stack[--top];
            if (e != '(')
                goto out;
        } else if (c == '}') {
            if (top == 0)
                goto out;
            e = stack[--top];
            if (e != '{')
                goto out;
        } else if (c == ']') {
            if (top == 0)
                goto out;
            e = stack[--top];
            if (e != '[')
                goto out;
        } else {
            stack[top++] = c;
        }
    }

    ret = top == 0;
out:
    free(stack);
    return ret;
}