class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int n=time.size();
        int ans=0;
        unordered_map<int,int> mp;
        for(int i=0;i<n;i++)
        {
            int rem1=time[i]%60;
            int rem2=(60-rem1)%60;
            ans+=mp[rem2];
            mp[rem1]++;
        }
        return ans;
    }
};