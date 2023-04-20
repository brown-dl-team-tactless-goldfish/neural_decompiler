class Solution {
private:
    static const int N = 1000005;
    int mod = 1000000007;

    int c[N];

    int lowbit(int x){ return x & (-x); }

    void add(int k, int val){
        for(; k < N; k += lowbit(k)) c[k] += val;
    }

    int query(int k){
        int res = 0;
        for(; k; k -= lowbit(k)) res += c[k];
        return res;
    }

    template <typename A, typename B, typename C>
    inline A fpow(A x, B p, C lyd){
        A ans = 1;
        for(; p; p >>= 1, x = 1LL * x * x % lyd)if(p & 1)ans = 1LL * x * ans % lyd;
        return ans;
    }

public:
    int numSubseq(vector<int>& nums, int target) {

        sort(nums.begin(), nums.end());
        __int128 res = 0;
        for(int i = 0; i < nums.size(); i ++){
            bool good = false;
            int sub = target - nums[i];
            if(sub < 0) continue;
            int cnt = query(sub);
            int y = 0;
            if(query(nums[i]) - query(sub) > 0){
                y = query(nums[i]) - query(sub);
                good = true;
            }
            if(nums[i] * 2 <= target) res = (res + 1) % mod;
            if(good){
                __int128 a = (fpow(2, cnt, mod) - 1) % mod;
                __int128 b = (fpow(2, y, mod)) % mod;
                __int128 c = (a * b) % mod;
                res = (res + c) % mod;
            }
            else{
                res = (res % mod + ((fpow(2, cnt, mod) - 1) % mod)) % mod;
            }
            add(nums[i], 1);
        }
        return (int)res;
    }
};