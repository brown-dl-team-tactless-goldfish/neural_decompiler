class Solution {
public:
    int totalSteps(vector<int>& A) {
        int n = A.size(), res = 0;
        vector<int> stack, dp(n);
        for (int i = n - 1; i >= 0; --i) {
            while (!stack.empty() && A[i] > A[stack.back()]) {
                dp[i] = max(++dp[i], dp[stack.back()]);
                stack.pop_back();
                res = max(res, dp[i]);
            }
            stack.push_back(i);
        }
        return res;
    }
};