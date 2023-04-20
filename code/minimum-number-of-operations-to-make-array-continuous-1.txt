// OJ: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
// Author: github.com/lzl124631x
// Time: O(NlogN)
// Space: O(1)
class Solution {
public:
    int minOperations(vector<int>& A) {
        int N = A.size(), i = 0, j = 0;
        sort(begin(A), end(A));
        A.erase(unique(begin(A), end(A)), end(A)); // only keep unique elements
        for (int M = A.size(); j < M; ++j) {
            if (A[i] + N <= A[j]) ++i;
        }
        return N - j + i;
    }
};