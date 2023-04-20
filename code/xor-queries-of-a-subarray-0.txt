/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* xorQueries(int* arr, int arrSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize){
    *returnSize=queriesSize;
    int *res=(int*)malloc(sizeof(int)*queriesSize);
    for(int i=1;i<arrSize;i++){
        arr[i]^=arr[i-1];
    }
    for(int i=0;i<queriesSize;i++){
        if(queries[i][0]==0) res[i]=arr[queries[i][1]];
        // else if(queries[i][0]==queries[i][1]) res[i]=arr[queries[i][1]]^arr[queries[i][1]-1];
        else res[i]=arr[queries[i][1]]^arr[queries[i][0]-1];
    }
    return res;
}