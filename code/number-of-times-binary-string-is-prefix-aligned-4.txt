class Solution {
public:
    int numTimesAllBlue(vector<int>& flips) 
    {
        int count=0;
        int max_val=0;
        int n=flips.size();
        for(int i=0;i<n;i++)
        {
            max_val=max(max_val,flips[i]-1);
            if(i==max_val)
            {
                count++;
            }
        }
        return count;
    }
};