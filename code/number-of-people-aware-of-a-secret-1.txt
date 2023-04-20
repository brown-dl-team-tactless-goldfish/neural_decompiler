class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        long long mod = 1e9 + 7, know = 0, wait = 1;
        queue<pair<long long, long long>> delayq, forgetq;
        delayq.push({delay + 1, 1});
        forgetq.push({forget + 1, 1});
        for(int i = delay + 1; i <= n; i++) {
            if(!forgetq.empty() and forgetq.front().first == i) {
                auto [_, c] =  forgetq.front(); forgetq.pop();
                know = (know - c + mod) % mod;
            }
            if(!delayq.empty() and delayq.front().first == i) {
                auto [_, c] = delayq.front(); delayq.pop();
                wait = (wait - c + mod) % mod;
                know = (know + c) % mod;
            }
            if(know) {
                delayq.push({i + delay, know});
                forgetq.push({i + forget, know});
                wait = (wait + know) % mod;
            }
        }
        return (know + wait) % mod;
    }
};