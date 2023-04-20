class Solution {
public:
    
    void helper(vector<int> &ans, int k, bool takePositive){
        if(k == 0)
            return;
        takePositive ? ans.push_back(ans[ans.size()-1] + k) : ans.push_back(ans[ans.size()-1] - k);
        helper(ans, k-1, !takePositive);
    }
    
    vector<int> constructArray(int n, int k) {
        vector<int> ans;
        ans.push_back(1);
        helper(ans,k,true);
        int c = n - ans.size();
        int a = ans[1]+1;
        while(c--)
            ans.push_back(a++);
        
        return ans;
    }
};