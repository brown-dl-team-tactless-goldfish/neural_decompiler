class Solution {
public:
    int kadane(vector<int> &arr)
    {
      int sum = 0, maxsum = 0;
      for(int it : arr)
      {
          sum = max(sum, 0) + it;
          maxsum = max(sum, maxsum);
      }
      return maxsum;
    }
    
    int kConcatenationMaxSum(vector<int>& arr, int k) {
     const int mod = 1e9 + 7;
     if( k == 1)
     return kadane(arr);
     int n = arr.size();
     int sum = 0;
     for(int it : arr)
     {
         sum = (sum + it)%mod;
     }
     arr.reserve(2 * n);
     for (int i = 0; i < n; ++i)
         arr.push_back(arr[i]);
     int ans = kadane(arr);
     if(sum <= 0)
     return ans;
     ans = (ans + long(k-2)*sum)%mod;
     return ans;
    }
};