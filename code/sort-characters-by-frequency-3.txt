int compareIntArray(const void *pa, const void *pb) {
    const int *a = *(const int **)pa;
    const int *b = *(const int **)pb;

    // descending order
    if (a[1] == b[1]) {
        return b[0] - a[0];
    } else {
        return b[1] - a[1];
    }
}

char *frequencySort(char *s) {
    int i, j;

    // s consists of uppercase and lowercase English letters and digits.
#define HASHTABLE_SIZE (128)
    // malloc hash table
    int **pHashTable = (int **)malloc(HASHTABLE_SIZE * sizeof(int *));
    if (pHashTable == NULL) {
        perror("malloc");
        return s;
    }
    for (i = 0; i < HASHTABLE_SIZE; ++i) {
        pHashTable[i] = (int *)malloc(2 * sizeof(int));
        if (pHashTable[i] == NULL) {
            perror("malloc");
            for (j = 0; j < i; ++j) {
                free(pHashTable[j]);
                pHashTable[j] = NULL;
            }
            free(pHashTable);
            pHashTable = NULL;
            return s;
        }
        pHashTable[i][0] = i;
        pHashTable[i][1] = 0;
    }

    // use hash table to record the frequency of the characters
    int len = strlen(s);
    for (i = 0; i < len; ++i) {
        ++pHashTable[(int)s[i]][1];
    }

    // sort the number of character appearance
    qsort(pHashTable, HASHTABLE_SIZE, sizeof(pHashTable[0]), compareIntArray);

    // update return string based on the frequency of the characters
    int count = 0;
    for (i = 0; i < HASHTABLE_SIZE; ++i) {
        if (pHashTable[i][1] == 0) {
            break;
        }

        for (j = 0; j < pHashTable[i][1]; ++j) {
            s[count] = pHashTable[i][0];
            ++count;
        }
    }

    // free hash table
    for (i = 0; i < HASHTABLE_SIZE; ++i) {
        free(pHashTable[i]);
        pHashTable[i] = NULL;
    }
    free(pHashTable);
    pHashTable = NULL;

    return s;
}