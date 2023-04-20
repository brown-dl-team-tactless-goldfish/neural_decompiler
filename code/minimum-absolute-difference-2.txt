/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int cmp(const void *a,const void*b) {
    return (*(int*)a-*(int*)b);
}
int** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int** returnColumnSizes){
    int **res = NULL;
    
    int min =INT_MAX;
    (*returnSize) = 0; // ahaha always forget to reset it it comes with random value and will fuck ur program!
    (*returnColumnSizes) = NULL; // this mother-fucker too
    qsort(arr,arrSize,sizeof(int),cmp);
    int i;
    for(i=0;i<arrSize-1;i++) {
        if(abs(arr[i]-arr[i+1])<min) min = abs(arr[i]-arr[i+1]);
    }
   
    for(i=0;i<arrSize-1;i++) {
        if(abs(arr[i]-arr[i+1]) == min) {
            res = (int**)realloc(res,++(*returnSize)*sizeof(int*));
            res[(*returnSize)-1] = (int*)malloc(2*sizeof(int));
            res[(*returnSize)-1][0] = arr[i],res[(*returnSize)-1][1] = arr[i+1];
            (*returnColumnSizes) = (int*)realloc((*returnColumnSizes),(*returnSize)*sizeof(int));
            (*returnColumnSizes)[(*returnSize)-1] = 2;
        }
    }
    
    return res;
}