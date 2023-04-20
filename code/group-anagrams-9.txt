typedef struct {
    char *string;
    char *sorted;
} Unit;

int compareChar(const void *a, const void *b) {
    return (*(char*)a - *(char*)b);
}

int compareUnitPtr(const void *a, const void *b) {
    Unit **u1Ptr = (Unit **) a;
    char *u1Sorted = (*u1Ptr)->sorted;
    Unit **u2Ptr = (Unit **) b;
    char *u2Sorted = (*u2Ptr)->sorted;
    int i;
    for (i = 0; i < strlen(u1Sorted); i++) {
        if (u1Sorted[i] != u2Sorted[i]) {
            return u1Sorted[i] - u2Sorted[i];
        }
    }
    return (int) u1Sorted[i] - (int) u2Sorted[i];
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char *** groupAnagrams(char ** strs, int strsSize, int* returnSize, int** returnColumnSizes){
    if (strsSize == 0) {
        return NULL;
    }
    // fill up an array with Unit pointers
    Unit *units[strsSize];
    for (int i = 0; i < strsSize; i++) {
        units[i] = (Unit *) malloc(sizeof(Unit));
        units[i]->string = (char *) malloc(sizeof(char) * (strlen(strs[i]) + 1));
        strcpy(units[i]->string, strs[i]);
        units[i]->sorted = (char *) malloc(sizeof(char) * (strlen(strs[i]) + 1));
        strcpy(units[i]->sorted, strs[i]);
        qsort(units[i]->sorted, strlen(strs[i]), sizeof(char), compareChar);
    }
	
	// sort Unit pointer array and copy each one's unsorted string into grouped
    qsort(units, strsSize, sizeof(Unit *), compareUnitPtr);
    char **grouped = (char **) malloc(sizeof(char *) * strsSize);
    for (int i = 0; i < strsSize; i++) {
        grouped[i] = (char *) malloc(sizeof(char) * (strlen(units[i]->string) + 1));
        strcpy(grouped[i], units[i]->string);
    }
    // create and fill partitionIndices
    int partitionIndices[strsSize];
    int index = 0;
    partitionIndices[0] = index;
    for (int i = 1; i < strsSize; i++) {
        if (strcmp(units[i]->sorted, units[i - 1]->sorted)) {
            index++;
        }
        partitionIndices[i] = index;
    } 
    // assign *returnSize and allocate memory for answers
    *returnSize = index + 1;
    char ***anagramGroup = (char ***) malloc(sizeof(char **) * (*returnSize));
    *returnColumnSizes = (int *) malloc(sizeof(int) * (*returnSize));
	
    // calculate *returnColumnSizes and anagramGroup
    int lengthHelper = 1;
    int colSizesIndex = 0;
    int partitionIndex = 1;
    while (partitionIndex < strsSize) {
        if (partitionIndices[partitionIndex] == partitionIndices[partitionIndex - 1]) {
            lengthHelper++;
        }
        else {
            (*returnColumnSizes)[colSizesIndex] = lengthHelper;
            lengthHelper = 1;
            colSizesIndex++;
        }
        partitionIndex++;
    }
    (*returnColumnSizes)[colSizesIndex] = lengthHelper;
    anagramGroup[0] = grouped;
    for (int i = 1; i < *returnSize; i++) {
        anagramGroup[i] = anagramGroup[i - 1] + (*returnColumnSizes)[i - 1];
    }
    // free memory allocated for Units array
    for (int i = 0; i < strsSize; i++) {
        free(units[i]->string);
        free(units[i]->sorted);
        free(units[i]);
    }
    return anagramGroup;
}