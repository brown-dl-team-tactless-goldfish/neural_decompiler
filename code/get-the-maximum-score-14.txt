class Solution {
public:
    int maxSum(vector<int>& A, vector<int>& B) {
        int i = 0, j = 0, n = A.size(), m = B.size();
        long a = 0, b = 0, mod = 1e9 + 7;
        while (i < n || j < m) {
            if (i < n && (j == m || A[i] < B[j])) {
                a += A[i++];
            } else if (j < m && (i == n || A[i] > B[j])) {
                b += B[j++];
            } else {
                a = b = max(a, b) + A[i];
                i++, j++;
            }
        }
        return max(a, b) % mod;
    }
};