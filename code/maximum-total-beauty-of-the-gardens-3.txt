class Solution {
public:
    using ll = long long;
    ll maximumBeauty(vector<int>& F, ll newFlowers, int target, int full, int partial) {
        ll res = 0;
        sort(begin(F), end(F));
        vector<ll> preSum(F.size()+1, 0);
        for(int i = 0; i < F.size(); i++) preSum[i+1] = preSum[i]+F[i];
        for(int i = F.size()-1; i >= -1; i--) {
            if(i >= 0 && F[i] >= target) continue;
            int l = -1, h = i;
            while(l < h) {
                ll m = l + (h-l+1)/2, v_sum = preSum[m+1], t_sum = F[m]*(m+1), diff = t_sum - v_sum;
                if(diff > newFlowers) h = m-1;
                else l = m;
            }
            ll min_v = i == -1 ? 0 : min(target-1ll, (preSum[l+1]+(ll)newFlowers)/(l+1));
            res = max(res, min_v*partial+((ll)F.size()-i-1)*full);
            if(i != -1 && target-F[i] > newFlowers) break;
            if(i != -1) newFlowers -= max(0, target-F[i]);
        }
        return res;
    }
};