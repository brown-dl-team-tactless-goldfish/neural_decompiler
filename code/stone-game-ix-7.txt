#define ALICE true
#define BOB false

class Solution {
public:
    bool stoneGameIX(vector<int>& stones) {
        vector<int> a(3, 0);
        for (auto &x : stones)
            a[x % 3]++;
        bool flip = (a[0] % 2 > 0);
        if (!a[1])
            return (a[2] < 3 ? BOB : flip);
        if (!a[2])
            return (a[1] < 3 ? BOB : flip);
        if (abs(a[1] - a[2]) > 2)
            return ALICE;
        return !flip;
    }
};