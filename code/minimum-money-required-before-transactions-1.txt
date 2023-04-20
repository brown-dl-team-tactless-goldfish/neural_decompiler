class Solution {
public:
    long long minimumMoney(vector<vector<int>>& transactions) {
        long long res = 0;
        for(auto ele: transactions){
            res  = max(res,min(ele[0],ele[1])*1LL);
        };
        for(auto ele:transactions){
            res+=max(ele[0]-ele[1],0);
        };
        return res;
    }
};