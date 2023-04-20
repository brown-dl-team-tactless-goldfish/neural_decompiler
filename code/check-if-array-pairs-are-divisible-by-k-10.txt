class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        
        int n = arr.size();
        unordered_map<int, int>mp;
        
        for (int i = 0; i < n; i++)
			/* Add k to ensure this works for negative numbers */
            mp[(k + arr[i] % k) % k]++;
        
        for (int i = 0; i < n; i++) {
            int r = (k + arr[i] % k) % k;
            if (r == 0) {
			    /* If remainder is 0, then there must be even number of such array elements */
                if (mp[r] % 2 != 0)
                    return false;
            } else if (mp[r] != mp[k-r]) {
			    /* number of elements with remainder r must be same as number of elements with remainder k-r */ 
                return false;
            }
        }
        
        return true;
    }
};