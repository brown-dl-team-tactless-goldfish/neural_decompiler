class Solution {
public:
    int directbuy(vector<int>& price, vector<int>& needs)
    {
        int sum = 0;
        for(int i=0;i<price.size();i++) sum += price[i]*needs[i];
        return sum;
    }
    
    int solve(vector<int>& price, vector<vector<int>>& special, vector<int>& needs, int pos)
    {
        int n = needs.size();
        int ans = directbuy(price,needs);
        for(int i=pos;i<special.size();i++)
        {
            vector<int> temp;
            for(int j=0;j<n;j++)
            {
                if(special[i][j]>needs[j])
                {
                    temp.clear();
                    break;
                }
                temp.push_back(needs[j]-special[i][j]);
            }
            if(temp.size()>0) ans = min(ans, special[i][n] + solve(price,special,temp,i));
        }
        return ans;
    }
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        return solve(price,special,needs,0);
    }
};