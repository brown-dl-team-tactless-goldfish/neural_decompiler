class Solution {
public:
    void solve(vector<int> &nums,int i,int n,vector<int> &v,int sum)
    {
        if(i==n)
        {
            v.push_back(sum);
            return;
        }
        solve(nums,i+1,n,v,sum+nums[i]);
        solve(nums,i+1,n,v,sum);
    }
    int findSmaller(vector<int> &v,int x)
    {
        int low=0;
        int high=v.size()-1;
        int ans=0;
        int mid;
        while(low<=high)
        {
            mid=low+(high-low)/2;
            if(v[mid]<=x)
            {
                ans=mid;
                low=mid+1;
            }
            else
            {
                high=mid-1;
            }
        }
        return v[ans];
    }
    int findGreater(vector<int> &v,int x)
    {
        int idx=lower_bound(v.begin(),v.end(),x)-v.begin();
        if(idx==v.size())
        return v[idx-1];
        return v[idx];
    }
    int minAbsDifference(vector<int>& nums, int goal) {
      int n=nums.size();
      vector<int> num1,num2;
      for(int i=0;i<n/2;i++)
      {
          num1.push_back(nums[i]);
          //cout<<nums[i]<<" ";
      }
      cout<<endl;
      for(int i=n/2;i<n;i++)
      {
          num2.push_back(nums[i]);
          //cout<<nums[i]<<" ";
      }
      cout<<endl;
      vector<int> sum1,sum2;
      solve(num1,0,num1.size(),sum1,0);
      solve(num2,0,num2.size(),sum2,0);
      sort(sum2.begin(),sum2.end());
      int ans=INT_MAX;
      for(auto x:sum1)
      {
          int to_find=goal-x;
          int x1=findSmaller(sum2,to_find);
          int x2=findGreater(sum2,to_find);
          ans=min(ans,abs(x1+x-goal));
          ans=min(ans,abs(x2+x-goal));
          if(ans==0)
          return 0;
      }
      return ans;
    }
};