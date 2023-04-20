class Solution {
public:
    int flipLights(int n, int k) {
        if(k==0)
        return 1;
        
        if(n==1)
        return 2;
        if(n==2)
        {
            if(k==1)
            {
                return 3;
            }
            else
            {
                return 4;
            }
        }
        else
        {
            if(k==1)
            {
                return 4;
            }
            else if(k==2)
            {
                return 7;
            }
            else
            {
                return 8;
            }
        }
        return 0;
    }
};