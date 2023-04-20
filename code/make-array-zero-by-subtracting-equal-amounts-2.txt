int minimumOperations(int* nums, int numsSize){
int x=9999999,count=0;
while(x)
{ 
    x=9999999;
    int p=0;
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]<x&&nums[i]>0)
        {
            x=nums[i];
            p=1;
        }
    }
    if(p==0)
        {
            return count;
        }
    for(int j=0;j<numsSize;j++)
    {
        if(nums[j]>0)
        {
            nums[j]=nums[j]-x;
        }
    }
    count++;
}
return 0;
}