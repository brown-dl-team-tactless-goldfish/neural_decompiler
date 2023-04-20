void backtrack(int *nums,int numsSize,int target,int index,int pos,int *res){
    if(pos==numsSize) return;
    for(int i=pos;i<numsSize;i++){
        int temp=index|nums[i];
        if(temp==target) (*res)++;
        backtrack(nums,numsSize,target,temp,i+1,res);
    }
}

int countMaxOrSubsets(int* nums, int numsSize){
    int max=0;
    for(int i=0;i<numsSize;i++){
        max|=nums[i];
    }
    int res=0;
    for(int i=0;i<numsSize;i++){
        if(nums[i]==max) res++;
        backtrack(nums,numsSize,max,nums[i],i+1,&res);
    }
    return res;
}