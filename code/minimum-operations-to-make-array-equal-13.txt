class Solution {
public:
    int minOperations(int n) {
        int k = (n-1)/2, c = 0, add = 2;
        for (int i = 0; i < k; i++) {
            c += add;
            add += 2;
        }
        if (n%2 == 0) c += (k+1);
        return c;
    }
};