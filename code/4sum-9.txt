class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n=nums.size();
        vector<vector<int>> ans;
        sort(nums.begin(),nums.end());
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                int sum=target-nums[i]-nums[j];
                int left=j+1;
                int right=n-1;
                while(left<right)
                {
                    int find=nums[left]+nums[right];
                    if(find==sum)
                    {
                        vector<int> v(4);
                        v[0]=nums[i];
                        v[1]=nums[j];
                        v[2]=nums[left];
                        v[3]=nums[right];
                        ans.push_back(v);
                        left++;
                        right--;
                        while(left<right && nums[left]==v[2])
                        {
                            ++left;
                        }
                        while(left<right && nums[right]==v[3])
                        {
                            --right;
                        }
                        while(j+1<n && nums[j+1]==nums[j]) j++;
                        while(i+1<n && nums[i+1]==nums[i]) i++;
                    }
                    else if(find<sum)
                    {
                        left++;
                    }
                    else
                    {
                        right--;
                    }
                }
            }
        }
        return ans;
    }
};