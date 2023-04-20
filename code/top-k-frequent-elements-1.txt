/* Qsort array, create array A with elem and freq, qsort A
 * return first k elems in A */
typedef struct node 
{
    int elem;
    int count;
}node_t;


int compareNodeList(const void *a, const void *b)
{
    node_t *x = (node_t *) a;
    node_t *y = (node_t *) b;
    return (y->count)-(x->count);
}

int compare(const void *a, const void* b)
{
    return (*(int*)a)-(*(int *)b);
}


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* topKFrequent(int* nums, int numsSize, int k, int* returnSize){
    int i = 1;
    int count = 0;
    node_t *nodeList=malloc(numsSize * sizeof(node_t));
    qsort(nums, numsSize ,sizeof(int) , compare);
    printf("\nAfter qsort array is :");
    for(int i = 0;i<numsSize;i++)
    {
        printf(" %d ",nums[i]);
    }
    int *res= malloc(k*sizeof(int));

    nodeList->elem = nums[0];
    nodeList->count = 1;
    count++;
    node_t *nodeTemp = nodeList;
    while(i<numsSize)
    {
        if(nums[i] != nums[i-1])
        {
            //res[count] = nums[i];
            nodeTemp++;
            nodeTemp->elem = nums[i];
            nodeTemp->count = 1;
            i++;
            count++; //counting number of elem is nodeList
            printf("\nNew Elem inserted %d",  nodeTemp->elem);
        }
        else
        {
            nodeTemp->count++;
            i++;
        }
        
    }
    qsort(nodeList, count ,sizeof(nodeList), compareNodeList);
    for(int i = 0;i<k;i++)
    {
        res[i]=nodeList[i].elem;
    }
    *returnSize = k;
    return res;
}