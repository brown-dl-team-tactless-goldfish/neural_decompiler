class Solution {
public:
    int bestRotation(vector<int>& A) {
        const int N = A.size();
        // vector to accumulate intervals
		// For a position k, the accumulated score is the sum of tmp[0] + ... + tmp[k]
        vector<int> tmp(N+1, 0); 
        
        for (int i(0); i < N; ++i) {
            if (A[i] <= i) {
                // if A[i] <= i, K in [0,i-A[i]] or [i+1, N-1] to get 1 point
                tmp[0] += 1;
                tmp[i-A[i]+1] -= 1;
                tmp[i+1] += 1;
                tmp[N] -= 1;
            }
            else {
                // if A[i] > i, K in [i+1, N-A[i]+i] to get 1 point 
                tmp[i+1] += 1;
                tmp[N-A[i]+i+1] -= 1;
            }
        }
        
        // count to get maximum
        int maxc = INT_MIN;
        int maxK = -1;
        int cur = 0;
        for (int i(0); i < N; ++i) {
            cur += tmp[i];
            if (cur > maxc) {
                maxc = cur;
                maxK = i;
            }
        }
        return maxK;
    }
};