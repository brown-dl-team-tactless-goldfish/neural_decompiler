class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
        int sum = 0;
        for (int x : stones) {
            sum += x;
        }
        int r = sum;
        for (int i = stones.size() - 2; i; --i) {
            sum -= stones[i + 1];
            r = max(r, sum - r);
        }
        return r;
    }
};