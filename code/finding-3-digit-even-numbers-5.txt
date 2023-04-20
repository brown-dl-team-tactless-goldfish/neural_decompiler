class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) 
    {
        vector<int>count(10,0);
        for(auto x:digits)
            count[x]++;
        vector<int>res;
        for(int i=1;i<=9;i++)
        {
            for(int j=0;j<=9;j++)
            {
                for(int k=0;k<9;k+=2)
                {
                    count[i]--;count[j]--;count[k]--;
                    if(count[i]>=0 && count[j]>=0 && count[k]>=0)
                    {
                        int x=i*100+j*10+k;
                        res.push_back(x);
                    }
                    count[i]++;count[j]++;count[k]++;
                }
            }
        }
        return res;
    }
};