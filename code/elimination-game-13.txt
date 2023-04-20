class Solution {
public:
    int lastRemaining(int n) {
        int ans=1,step=1;
        int rem=n;
        bool left=1;
        while(rem>1)
        {
            if(left or rem&1)
                ans+=step;
            rem/=2;
            step*=2;
            left=1-left;
        }
    return ans;
    }
};