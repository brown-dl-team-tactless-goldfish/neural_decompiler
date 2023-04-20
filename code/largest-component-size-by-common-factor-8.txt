class UnionFind {
    public:
    vector<int> par, sz;
    UnionFind(int n) : par(n), sz(n,1) {
        iota(begin(par), end(par), 0);
    }
    int find(int x) {
        if(par[x] == x) return x;
        return par[x] = find(par[x]);
    }
    bool Union(int x, int y) {
        int xp = find(x), yp = find(y);
        if(xp == yp) return false;
        if(sz[xp] > sz[yp]) par[yp] = par[xp], sz[xp] += sz[yp];
        else par[xp] = par[yp], sz[yp] += sz[xp];
        return true;
    }
};
class Solution {
public:
    int largestComponentSize(vector<int>& nums) {
        int n = size(nums), ans = 1;
        auto spf = sieve(*max_element(begin(nums), end(nums))+1);
        UnionFind uf(n + 1);
        unordered_map<int, int> mp;                      // stores {p : 1st found index i such that nums[i] % p == 0}
        for(int i = 0; i < n; i++)                       // prime factorize nums[i]
            for(auto p : getPrimes(nums[i], spf))
                if(mp.count(p)) uf.Union(i, mp[p]);
                else mp[p] = i;
        
        return *max_element(begin(uf.sz), end(uf.sz));
    }
    
    vector<int> sieve(int M) {
        vector<int> spf(M+1);
        iota(begin(spf), end(spf), 0);
        for(int i = 2; i*i < M; i++) 
            if(spf[i] == i) 
                for(int j = i*i; j < M; j += i)
                    if(spf[j] == j)
                        spf[j] = i;            
        return spf;
    }

    vector<int> getPrimes(int x, vector<int>& spf) {
        vector<int> primes;
        while (x != 1) {
            int p = spf[x];
            primes.push_back(p);
            while(x % p == 0) x /= p;
        }
        return primes;
    }
};