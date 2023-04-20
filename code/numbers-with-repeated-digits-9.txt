class Solution {
    vector<int> getarray(int n) {
        vector<int> a;
        while(n != 0) {
            a.push_back(n%10);
            n /= 10;
        }
        reverse(a.rbegin(), a.rend());
        return a;
    }
    
    int npr(int n, int r) {
        int ans = 1;
        for(int i = 1; i <= n; i++)
            ans *= i;
        for(int i = 1; i <= n-r; i++)
            ans /= i;
        return ans;
    }
    
public:
    int numDupDigitsAtMostN(int n) {
        if(n <= 10)
            return 0;
        
        vector<int> a = getarray(n);
        int len = a.size();
        
        // the approach is too count the numbers with distinct digit

        // counting possibilities of 1 to len-1 digit number
        // 0-9, 10-99, 100-999, 1000-9999, ............        
        int ans = 0;
        for(int i = 1; i < len; i++) 
            ans += 9 * npr(10-1, i-1);
            
        // for len digit number which are less than n
        vector<bool> used(10);
        for(int i = 0; i < len; i++) {
            for(int j = i==0?1:0; j < a[i]; j++) {
                if(used[j]) continue;
                ans += npr(10-i-1, len-i-1);
            }
            if(used[a[i]]) 
                break;
            used[a[i]] = true;
        }
        
        vector<bool> dup(10);
        bool flag = false;
        for(int i = 0; i < len; i++) {
            if(dup[a[i]]) {
                flag = true;
                break;
            }
            dup[a[i]] = true;
        }
        
        if(!flag) ans += 1;
                
        return n - ans;
    }
};

