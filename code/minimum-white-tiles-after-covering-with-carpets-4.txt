class Solution {
    int n;
    vector<int> suffix;
    vector<vector<int>> memo;
public:
    
    int doit(string& floor, int carp, int len, int ind) {
        if (ind >= n)   return 0;
        if (carp == 0)  return suffix[ind]; // if no carpets are left then all the white tiles from current index to the last will be visible
        if (memo[carp][ind] != -1)  return memo[carp][ind];
        int a = doit(floor, carp-1, len, ind+len); // carpet is used
        int b = doit(floor, carp, len, ind+1) + (floor[ind] == '1'); // carpet is not used
        return memo[carp][ind] = min(a, b);
    }
        
    int minimumWhiteTiles(string floor, int carp, int len) {
        
        n = size(floor);
        suffix.resize(n+1, 0);
        memo.resize(carp+1, vector<int>(n+1, -1));
        suffix[n-1] = (floor[n-1] == '1');
        for (int i=n-2; ~i; i--)
            suffix[i] = suffix[i+1] + (floor[i] == '1');
        
        return doit(floor, carp, len, 0);
    }
};