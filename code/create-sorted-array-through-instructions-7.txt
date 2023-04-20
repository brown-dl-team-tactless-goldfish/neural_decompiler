struct BIT{
    vector<long long> nums;
    BIT(int size) : nums(size){}
    long long lowbit(long long x) { return x & -x; }
    void update(long long x, long long cnt){
        while (x < nums.size()) {
            nums[x] += cnt;
            x += lowbit(x);
        }
    }
    
    long long query(int x) {
        long long sum = 0;
        if(x == 0) return 0;
        while(x > 0) {
            sum += nums[x];
            x -= lowbit(x);
        }
        return sum;
    }
};

class Solution {
public:
    int createSortedArray(vector<int>& instructions) {
        long long ans = 0, M = 1e9 + 7;
        BIT bit(1e5 + 10);
        for(auto n : instructions) {
            ans += min(bit.query(n - 1), bit.query(1e5) - bit.query(n));
            bit.update(n, 1);
        }
        return ans % M;
    }
};