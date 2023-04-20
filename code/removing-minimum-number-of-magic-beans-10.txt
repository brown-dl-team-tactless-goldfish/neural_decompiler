class Solution {
public:
    long long minimumRemoval(vector<int>& beans) {
        sort(beans.begin(), beans.end());
        long long ans = LONG_LONG_MAX, ps = 0, n = beans.size(), ts = accumulate(beans.begin(), beans.end(), 0ll);

        for(int i=0; i<n; i++) {
            ans = min(ans, ps + ts - beans[i] * (n - i));
            ps += beans[i];
            ts -= beans[i];
        }
        return ans;
    }
};