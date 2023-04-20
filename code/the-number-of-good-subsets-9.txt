class Solution {
public:
    vector<int> prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    int MASK[31], MOD = 1e9 + 7, seen[31];
    long long memo[31][1050]; 
    long long solve1(int last, int mask) {
        long long &ret = memo[last][mask];
        if (ret != -1) return ret;
        ret = 1;
        for (int i = last + 1; i < 31; i++) if (seen[i] > 0 && MASK[i] > 0 && (MASK[i]&mask) == 0) {
            long long cnt = seen[i];
            ret += (cnt*solve1(i, mask | MASK[i])) % MOD;
            ret %= MOD;
        }
        return ret % MOD;
    }
    int numberOfGoodSubsets(vector<int>& nums) {
        memset(seen, 0, sizeof(seen));
        memset(memo, -1, sizeof(memo));
        for (int n : nums) seen[n]++;
        for (int i = 1 ; i < 31; i++) {
            int mask = 0, n = i;
            for (int j = 0; j < prime.size(); j++) if (n % prime[j] == 0) {
                int cnt = 0;
                while (n % prime[j] == 0) n /= prime[j], cnt++;
                if (cnt > 1) {
                    mask = 0;
                    break;
                }
                mask |= (1<<j);
            }
            MASK[i] = mask;
        }
        long long ans = 0, one_cnt = 0;
        for (int i = 0; i < nums.size(); i++) if (MASK[nums[i]] > 0 ) {
            ans += solve1(nums[i], MASK[nums[i]]);
            ans %= MOD;
        } else if (nums[i] == 1) one_cnt++;
      while (one_cnt-- > 0) {
            ans += ans;
            ans %= MOD;
        } 
        return ans;
    }
};