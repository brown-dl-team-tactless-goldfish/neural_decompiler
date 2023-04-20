class Solution {
public:
    
    int minChanges(vector<int>& v, int k) {
        int n = v.size();
        
        // freq[i][x] = frequency of the number x at position i where i in [0, k - 1]
        vector<vector<int> > freq(k, vector<int>(1024, 0));
        /* dp[i][j] = minimum total number of elements we need to change from index 0 to i so that
           the xor of the subarray from index 0 to i is equal to j */
        vector<vector<int> > dp(k, vector<int>(1024, n + 1));
        // numsAtPosition[i] = set of unique numbers at position i where i in [0, k - 1]
        unordered_set<int> numsAtPosition[k];
                
        for(int i = 0; i < n; i++) {
            int position = i % k;
            freq[position][v[i]]++;
            numsAtPosition[position].insert(v[i]);
        }
        
        int bestUptoLast = 0;
        
        for(int i = 0; i < k; i++) { // this loop runs k times
            
            // how many i indices exist in the array
            int cntOfPos = n / k + (((n % k) > i) ? 1 : 0);
            
            // will track best value at i
            int bestAti = n + 1;
            
            // find the best way to make the xor sum equal to j from index 0 to i
            for(int j = 0; j < 1024; j++) { // this loop runs 1024 times
                if(i == 0) {
                    dp[i][j] = cntOfPos - freq[i][j];
                }
                else {
                    
                    // iterate over all numbers that occur at index i
                    for(auto x : numsAtPosition[i]) { // this loop runs n/k times
                        dp[i][j] = min(dp[i][j], dp[i - 1][j ^ x] + cntOfPos - freq[i][x]);
                    }
                    
                    // this will do for all the numbers that don't occur at index i
                    // we are changing all the numbers at index i with an arbitrary number that gives best result
                    dp[i][j] = min(dp[i][j], bestUptoLast + cntOfPos);
                }
                bestAti = min(bestAti, dp[i][j]);
            }
            bestUptoLast = bestAti;
        }
        
        return dp[k - 1][0];
    }
};