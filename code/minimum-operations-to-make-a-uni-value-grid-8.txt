class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int> v;
        for(auto g:grid)
        {
            for(auto x:g)
            {
                v.push_back(x);
            }
        }
        sort(v.begin(),v.end());
        int n=v.size();
        int value=v[n/2];
        int ans=0;
        for(int i=0;i<n;i++)
        {
            if(abs(value-v[i])%x!=0)
            {
                return -1;
            }
            else
            {
                ans+=abs(value-v[i])/x;
            }
        }
        return ans;
    }
};