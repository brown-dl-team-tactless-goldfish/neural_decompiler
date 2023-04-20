class Solution {
public:
    int countHillValley(vector<int>& nums) {
          int ans = 0;
          int i = 1;
          while(i < nums.size() - 1){
              int ele = nums[i];
              int j = i -1;
              bool flag1 = true, flag2 = true;
              while(nums[j] == ele){
                  j--;
                  if(j < 0) {flag1 = false; break;}
              }
              
              int k = i + 1;
               while(nums[k] == ele){
                  k++;
                  if(k >= nums.size()) {flag2 = false; break;}
              }
              
              if(flag1 && flag2){
                  if(ele > nums[j] && ele > nums[k]) ans++;
                  else if(ele < nums[j] && ele < nums[k]) ans++;
              }
               // skippings the duplicates 
                while(nums[i] == ele) i++;
          }
        return ans;
    }
};