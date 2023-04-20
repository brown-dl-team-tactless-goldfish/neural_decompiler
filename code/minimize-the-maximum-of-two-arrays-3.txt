class Solution {
public:

    int minimizeSet(int d1, int d2, int uqC1, int uqC2) {
        long int low=1,high=INT_MAX;
        int ans=INT_MAX;
        long long int lcm=((long long)d1*d2)/__gcd(d1,d2);
        while(low<=high){
             int  mid=low+(high-low)/2;
             int notd1= mid -mid/d1;// not divisble by d1
             int notd2= mid- mid/d2;// not divisible by d2
             int notboth= mid-mid/lcm;// not divisble by both
           if(notd1>=uqC1 and notd2>=uqC2 and notboth>=(uqC1+uqC2)){
               ans=mid;
               high=mid-1;
           }
           else low=mid+1;
        }
       
        return ans;
    }
};