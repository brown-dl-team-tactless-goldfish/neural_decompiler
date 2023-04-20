struct word {
    char sorted[256];
    char s[256];
    UT_hash_handle hh;
};

int comp(const void *aa, const void *bb)
{
    char a, b;
    a = *(char *)aa;
    b = *(char *)bb;
    
    if (a < b)
        return -1;
    else if (a > b)
        return 1;
    else
        return 0;
}

char *sort_string(char *s)
{
    char *rs = malloc(strlen(s)+1);
    assert(rs);
    strcpy(rs, s);
    qsort((void *)rs, strlen(rs), 1, comp);
    return rs;
}

int word_sort(struct word *a, struct word *b) {
    return strcmp(a->sorted,b->sorted);
}


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char *** groupAnagrams(char ** strs, int strsSize, int* returnSize, int** returnColumnSizes){
    struct word *w, *tmp;
    int i;
    struct word *words = NULL;
    
    for (i = 0; i < strsSize; i++) {
        char *sorted = sort_string(strs[i]);
        w = (struct word *)malloc(sizeof *w);
        strncpy(w->sorted, sorted, 256);
        strncpy(w->s, strs[i], 256);
        HASH_ADD_STR( words, sorted, w );
        free(sorted);
    }
    
    char ***ret = malloc(strsSize * sizeof(char *));
    int *retcolsizes = malloc(strsSize * sizeof(int));
    *returnColumnSizes = retcolsizes;
    assert(*returnColumnSizes);
    assert(ret);
    
    *returnSize = -1;
    char *anagram = NULL;
    
    /* XXX: what we would like is something like (python):
     *      return dic.values();
     * I know its C, but there has to be a better way.
     */
    HASH_SORT(words, word_sort);
    HASH_ITER(hh, words, w, tmp) {
        if (anagram != NULL && strcmp(w->sorted, anagram) == 0) {
            ret[*returnSize][retcolsizes[*returnSize]] = w->s; // was malloc'ed
            retcolsizes[*returnSize] += 1;
        } else {
            *returnSize += 1;
            ret[*returnSize] = malloc(strsSize * sizeof(char *));
            assert(ret[*returnSize]);
            retcolsizes[*returnSize] = 0;
            ret[*returnSize][retcolsizes[*returnSize]] = w->s; // was malloc'ed
            retcolsizes[*returnSize] += 1;
            anagram = w->sorted;
        }
    }
    
    /* XXX: we are leaking a bunch of memory for the struct word's*/
    *returnSize += 1;
    return ret;
}