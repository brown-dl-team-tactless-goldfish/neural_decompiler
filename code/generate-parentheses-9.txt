

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void swap(char *right, char *left)
{
    char t = *right;
    *right = *left;
    *left = t;
}

void dfs(char *base, int size, char ***arr, int *rs, int idx ,int openCount, int closedCount, int n)
{
    if(openCount == closedCount && closedCount == n)
    {
        //found valid sequence
        (*rs)++;
        (*arr) = realloc(*arr, sizeof(char*)*((*rs)));
        (*arr)[(*rs)-1] = calloc(1, sizeof(char)*(size+1));
        for(int i = 0;i<=size;i++)
        {
            (*arr)[(*rs)-1][i] = base[i];
        }
        return;
       
    }
    else
    {
            if(openCount < n)
            {
                base[idx] = '(';
                dfs(base, size, arr, rs, idx+1 , openCount+1, closedCount, n);
                base[idx] = '\0';
            }
            if(openCount >closedCount)
            {
                base[idx] = ')';
                dfs(base, size, arr, rs, idx+1, openCount, closedCount+1, n);
                base[idx] = '\0';
            }
    }
}

char ** generateParenthesis(int n, int* returnSize){
    char **arr = calloc(1, sizeof(char*));
    char *base = calloc(20, sizeof(char));
    *returnSize = 0;
    /*for(int i = 0;i<n*2;)
    {
        base[i++] = '(';
        base[i++] = ')';
    }*/
    dfs(base, n*2, &arr, returnSize, 0, 0, 0, n);
    return arr;
}