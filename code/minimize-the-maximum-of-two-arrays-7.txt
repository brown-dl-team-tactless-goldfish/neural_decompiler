#define ll long long int

class Solution {
public:
    int minimizeSet(int d1, int d2, int uc1, int uc2) {
        
        ll s = 1, e = INT_MAX;
        ll LCM = (1LL * d1 * d2) / (__gcd(d1, d2));
        
        while(s < e)
        {
            // total number of elements (1 to x)
            ll x = (s+e)/2;
            
            // elements divisible by both d1 and d2
            ll a = x / LCM;
            
            /* elements divisible by only d1 i.e.
            
               (elements divisible by d1) - (elements divisible by both d1 and d2) */
            ll b = x / d1 - a;
            
            /* elements divisible by only d2 i.e.
            
               (elements divisible by d2) - (elements divisible by both d1 and d2)*/
            ll c = x / d2 - a;
            
            /* elements not divisible by d1 and d2 i.e.
            
               (total number of elements) - 
               (elements divisible by both d1 and d2) - 
               (elements divisible by only d1) - 
               (elements divisible by only d2)
             */
            ll d = x - a - b - c;
            
            // if elements divisible by d2 is less than unique count of arr 1, then we need to take elements from d.
            if(c < uc1)
                d -= (uc1 - c);
            
            // if elements divisible by d1 is less than unique count of arr 2, then we need to take elements from d.
            if(b < uc2)
                d -= (uc2 - b);
            
            // if d has more elements left, then it is a possible answer lets go tot the left side.
            if(d >= 0)
                e = x;
            else // lets go to right side.
                s = x+1;
        }
        
        return s;
    }
};