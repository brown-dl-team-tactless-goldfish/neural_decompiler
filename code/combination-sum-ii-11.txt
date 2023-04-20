

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int comp(const void *a, const void *b)
{
    return (*(int *)a)-(*(int*)b);
}

void pickOrNotPick(int *candidates, int size, int curr, int target, int***res, int *helper, int helperTop, int *rs, int **rcs)
{
    if(target == 0)
    {
        (*rs)++;
        (*res) = realloc((*res), sizeof(int*) * (*rs));
        (*res)[(*rs)-1] = calloc((helperTop)+1, sizeof(int) );
        *rcs = realloc(*rcs, sizeof(int) *(*rs));
        (*rcs)[(*rs)-1] = (helperTop)+1;
        for(int i = 0;i<=helperTop;i++)
        {
            (*res)[(*rs)-1][i] = helper[i];
        }
        return;
    }
    else if(target <0 || curr > size)
    {
        //no way we can now reach the target.
        return;
    }
    else if(target > 0 && curr < size)
    {
        //assume a pick, and increment curr, as it cannot be repicked
        helper[(helperTop)+1]= candidates[curr];
        
        
        pickOrNotPick(candidates, size, curr+1, target-candidates[curr], res, helper, helperTop+1, rs, rcs);
        //assume a skip, for that pop out the pushed elem and call function.
        //skip dups
        while( curr+1<size && candidates[curr] == candidates[curr+1])
        {
            curr++;
        }
        pickOrNotPick(candidates, size, curr+1, target, res, helper, helperTop, rs, rcs);
    }
    return;
}


int** combinationSum2(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes){
    qsort(candidates, candidatesSize, sizeof(int), comp);
    *returnSize = 0;
    int **res = calloc(1, sizeof(int*));
    *returnColumnSizes = calloc(1, sizeof(int));
    int* helper = calloc(candidatesSize, sizeof(int));
    pickOrNotPick(candidates, candidatesSize ,0,target, &res, helper, -1, returnSize, returnColumnSizes);
    return res;

}