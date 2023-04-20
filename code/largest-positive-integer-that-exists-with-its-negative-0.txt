int findMaxK(int* nums, int numsSize){
  int i,j,c=0,max=0;
  int arr[10000],k=0;
  for(i=0;i<numsSize;i++){
      for(j=i+1;j<numsSize;j++){
          if(nums[i]==-nums[j]){
              if(nums[j]>0)
             arr[k++]=nums[j];
             else
             arr[k++]=nums[j]*(-1);
          }
      }
  }
  for(i=0;i<k;i++){
      if(max<arr[i]){
          max=arr[i];
          c=1;
      }
  }
  if(c==1)
  return max;
  else
  return -1;
}