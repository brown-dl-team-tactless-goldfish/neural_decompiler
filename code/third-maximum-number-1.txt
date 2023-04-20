int thirdMax(int* nums, int numsSize){
   long m[3] = { LONG_MIN, LONG_MIN, LONG_MIN };
   int cnt = 0;

   for(int i = 0; i < numsSize; i++) {
      if(nums[i] == m[0] || nums[i] == m[1] || nums[i] == m[2])
         continue;
      if(nums[i] > m[0]) {
         m[2] = m[1];
         m[1] = m[0];
         m[0] = nums[i];
         cnt++;
      }else if(nums[i] > m[1]) {
         m[2] = m[1];
         m[1] = nums[i];
         cnt++;
      }else if(nums[i] > m[2]) {
         m[2] = nums[i];
         cnt++;
      }
   }
   if(cnt < 3) {
      return m[0];
   }else {
      return m[2];
   }
}