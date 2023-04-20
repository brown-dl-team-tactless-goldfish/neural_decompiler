
void swap(int *arr,int left,int right)
{
    if(left == right)
        return;
    arr[left]=arr[left] + arr[right];
    arr[right]=arr[left] - arr[right];
    arr[left]=arr[left] - arr[right];
}

typedef struct {
    int *orig;
    int *arr;
    int size;
} Solution;

void printArr(int *arr, int size)
{
    for(int i = 0;i<size;i++)
    {
        printf("\n arr[%d] is %d",i,arr[i]);
    }
}

Solution* solutionCreate(int* nums, int numsSize) {
    Solution *obj = malloc(sizeof(Solution));
    obj->arr = malloc(numsSize*sizeof(int));
    obj->orig = malloc(numsSize*sizeof(int));
    obj->size = numsSize;
    memcpy(obj->orig, nums, numsSize * sizeof(int));
    memcpy(obj->arr, obj->orig, numsSize * sizeof(int));
    //printArr(obj->arr, obj->size);
    return obj;
    
}

int* solutionReset(Solution* obj, int* retSize) {
    memcpy(obj->arr, obj->orig, obj->size * sizeof(int));
    *retSize = obj->size;
    return obj->arr;
}

int* solutionShuffle(Solution* obj, int* retSize) {
    //memcpy(obj->arr, obj->orig, obj->size * sizeof(int)); //as per hint
    int random;
    for(int i = 0;i<obj->size;i++)
    {
        random = rand() % (obj->size);
        printf("random no. generated is %d",random);
        swap(obj->arr, i, random);
    }
    *retSize = obj->size;
    return obj->arr;
}

void solutionFree(Solution* obj) {
    free(obj->arr);
    free(obj->orig);
    free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(nums, numsSize);
 * int* param_1 = solutionReset(obj, retSize);
 
 * int* param_2 = solutionShuffle(obj, retSize);
 
 * solutionFree(obj);
*/