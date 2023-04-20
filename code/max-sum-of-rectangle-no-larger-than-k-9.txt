class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int maxS) {
        int maxA = INT32_MIN, r = matrix.size(), c = matrix[0].size();
        for(int i = 0; i < c; ++i) {
            vector<int> sum(r, 0);
            if(maxA == maxS) return maxA; // Stop if we can reach maxS
            for(int j = i; j < c; ++j) {
                for(int k = 0; k < r; ++k) sum[k] += matrix[k][j];
                
                //First try Kadane's Algo and see if maxSum is less than maxS. 
                int curMax = INT32_MIN, curSum = 0;
                for(int k = 0; k < r; ++k) {
                    curSum += sum[k];
                    curMax = max(curMax, curSum);
                    if(curSum < 0) curSum = 0;
                }
                if(curMax <= maxS) {maxA = max(maxA, curMax); continue;}
                
                // Only apply slow method when there maxSum that is greater than maxS.
                int csum = 0;
                set<int> s({csum});
                for(int k = 0; k < r; ++k) {
                    csum += sum[k];
                    auto it = s.lower_bound(csum - maxS);
                    if(it != s.end()) maxA = max(maxA, csum - *it);
                    s.insert(csum);
                }
            }
        }
        return maxA;
    }
};

auto gucciGang = []() {std::ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);return 0;}();