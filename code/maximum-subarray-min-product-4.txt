class Solution {
public:
   
    int maxSumMinProduct(vector<int>& a) {
        int n = a.size();
        int right[n],left[n];
        for(int i = 0 ; i < n ; i++)
        {
            right[i]= n;
            left[i] = -1;
        }
        stack<long long >s;
        //next smaller to right
        for(int i=0;i<n;i++)
        {
            while(s.size() > 0 && a[s.top()] > a[i])
            {
                right[s.top()] = i ;
                s.pop();
            }
            s.push(i);
        }
        //nrxt smaller to left 
        stack<long long >r;
         for(int i=n-1;i>=0;i--)
        {
            while(r.size() > 0 && a[r.top()] > a[i])
            {
                left[r.top()] = i ; 
                r.pop();
            }
            r.push(i);
        }
       
         int mod = 1e9 + 7 ; 
        vector<long long >pre(n+1,0);
        pre[1] = a[0];
        for(int i =1 ; i < n ; i++)
            pre[i+1] = (long long )(pre[i] + a[i]) ;
        
        
        long long ans = 0 ; 
        for(int i = 0 ; i < n ; i++)
        {
            int l = left[i]; int r = right[i]; 
         
            long long  sum= 0 ; 
            if(l==-1)
                sum = pre[r];
            else
             sum = ((long long )pre[r]-(long long )pre[l+1]);
           
            long long int  pro = (long long )(long long )(sum*(long long)a[i]);
            ans = (long long )max(ans,pro);
            
        }
        return ans%mod;
    }
};