int factorial(int num)
{
    if(num==1){return 1;}
    else return num * factorial(num - 1);
}

void perm(int **arr,int *ind,int numsSize,int *nums,int *visited,int *res,int size,int k)
{
    if(k==numsSize){
        if(*ind==size){return;}
        int *temp = malloc(sizeof(int) * numsSize);
        memcpy(temp,res,sizeof(int) * numsSize);
        arr[(*ind)++] = temp;
    }
    else{
        for(int i=0;i<numsSize;i++){
            if(visited[i] == 0){
                res[k] = nums[i];
                visited[i] = 1;
                perm(arr,ind,numsSize,nums,visited,res,size,k+1);
                visited[i] = 0;
            }
        }
    }
}


int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    int size = factorial(numsSize);
	int ind = 0;
	
    int **arr = malloc(sizeof(int*) * size);
    int *visited = (int*)calloc(numsSize,sizeof(int));
    int *res = (int*)calloc(numsSize,sizeof(int));
	
    perm(arr,&ind,numsSize,nums,visited,res,size,0);
    
    int *ret = malloc(sizeof(int) * size);
    for(int i=0;i<size;i++){ret[i]=numsSize;}
    
    free(visited);
    free(res);
    
	*returnSize = size;
    *returnColumnSizes = ret;
    return arr;
}