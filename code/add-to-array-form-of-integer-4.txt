//#define LOG_DEBUG

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void reverseArray(int* A, int ASize);
int* addToArrayForm(int* A, int ASize, int K, int* returnSize);
    
int* addToArrayForm(int* A, int ASize, int K, int* returnSize) {
    //check the max size of return array
    int KSize = 0;
    for (int i = K; i > 0; i /= 10) KSize++;
    
    int rSize = (KSize > ASize) ? (KSize+1) : (ASize+1);

    int *tmp = calloc(rSize, sizeof(int));
#ifdef LOG_DEBUG
    printf("rSize = %d \n", rSize);
#endif
    
    //save values into temp array
    int idx = 0;
    for (int i = ASize-1; (i >= 0) || (K > 0); i--) {
        K += (i >= 0) ? A[i] : 0;
        tmp[idx] = K % 10;
        idx++;
        K /= 10;
    }

#ifdef LOG_DEBUG
    for (int i = 0; i < rSize; i++) {
        printf("%d ", tmp[i]);
    }
    printf("\n");
#endif
    
    //save the temp array to ret
    int *ret;
    if (tmp[rSize-1] == 0) {
        ret = calloc(rSize-1, sizeof(int));
        *returnSize = rSize-1;
        int j = 0;
        for (int i = rSize-2; i >= 0; i--) {
            ret[j++] = tmp[i];
        }
        free(tmp);
        tmp = NULL;
    } else {
        ret = tmp;
        *returnSize = rSize;
        reverseArray(ret, rSize);
    }
    
    return ret;
}

void reverseArray(int* A, int ASize) {
    int l = 0, r = ASize-1;
    
    while (l <= r) {
        int tmp = A[l];
        A[l] = A[r];
        A[r] = tmp;
        l++;
        r--;
    }
}

