class Solution {
public:
   int findClosestNumber(vector<int>& nums) 
    {
        int a = INT_MAX;
        int b = INT_MIN;
        for(int i:nums)
        {
            if(i>0)
                a = min(a,i);
            else if(0>i)
                b = max(b,i);
            else
                return 0;
        }
        if(b == INT_MIN)
            return a;
        else if(a == INT_MAX)
            return b;
        else if(abs(b) < a)
            return b;
        else
            return a;
    }
};