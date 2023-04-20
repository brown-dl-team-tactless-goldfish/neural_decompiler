class Solution {
public:
    long long maxProduct(string s) {
        int n = s.size(), center = 0, right = 0; 
        vector<int> hlen(n, 0), prefix(n, 0), suffix(n, 0); 
        for (int i = 0; i < n; ++i) {
            if (i < right) hlen[i] = min(right - i, hlen[2*center - i]); 
            while (0 <= i-1-hlen[i] && i+1+hlen[i] < n && s[i-1-hlen[i]] == s[i+1+hlen[i]]) ++hlen[i]; 
            if (right < i + hlen[i]) {
                center = i; 
                right = i + hlen[i]; 
            }
        }
        
        for (int i = 0; i < n; ++i) {
            prefix[i+hlen[i]] = max(prefix[i+hlen[i]], 2*hlen[i] + 1); 
            suffix[i-hlen[i]] = max(suffix[i-hlen[i]], 2*hlen[i] + 1); 
        }
        
        for (int i = 1; i < n; ++i) {
            prefix[n-1-i] = max(prefix[n-1-i], prefix[n-i]-2); 
            suffix[i] = max(suffix[i], suffix[i-1]-2); 
        }
        
        for (int i = 1; i < n; ++i) {
            prefix[i] = max(prefix[i-1], prefix[i]); 
            suffix[n-1-i] = max(suffix[n-1-i], suffix[n-i]); 
        }
        
        long long ans = 0ll; 
        for (int i = 1; i < n; ++i) ans = max(ans, (long long) prefix[i-1] * suffix[i]); 
        return ans; 
    }
};