class Solution {
public:
    vector<int> productQueries(int n, vector<vector<int>>& q) {
       
        vector<int> pow;
        long long mod = 1e9+7;
        
        //if bit is set insert in the power array
        for(int i =0;i<32;i++)
        {
            if(n&(1<<i))
                pow.push_back(1<<i);
        }
        vector<int> ans;
        
        //solving for the query
        for(int i =0;i<q.size();i++)
        {
            long long temp=1;
            for(int j =q[i][0];j<=q[i][1];j++)
            {
                temp=((temp%mod)*pow[j])%mod;
            }
            ans.push_back(temp);
        }
        return ans;
    }
};