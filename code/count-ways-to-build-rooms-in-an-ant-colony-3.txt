class Solution {
public:
    const long long MOD = 1000000007;
    vector<vector<int>> adj;
    vector<int> parent;
    vector<int> sub;
    int subTreeSize(int x){
        if(sub[x] != -1){
            return sub[x];
        }
        int cntr = 1;
        for(int y: adj[x]){
            if(y == parent[x]) continue;
            cntr += subTreeSize(y);
        }
        sub[x] = cntr;
        return cntr;
    }
    long long prod(long long x, long long y){
        return (x * y) % MOD;
    }
    long long binpow(long long a, long long b) {
        long long res = 1;
        while (b > 0) {
            if (b & 1){
                res = prod(res, a);
            }
            a = prod(a, a);
            b >>= 1;
        }
        return res;
    }
    long long inv(long long x){
        return binpow(x, MOD - 2);
    }
    int waysToBuildRooms(vector<int>& prevRoom) {
        sub.resize(prevRoom.size());
        parent = prevRoom;
        adj.resize(prevRoom.size());
        for(int i = 0; i < prevRoom.size(); i++){
            sub[i] = -1;
            if(prevRoom[i] == -1) continue;
            adj[prevRoom[i]].push_back(i);
            adj[i].push_back(prevRoom[i]);
        }
        subTreeSize(0);
        long long x = 1;
        for(int i = 0; i < adj.size(); i++){
            x = prod(x, inv(sub[i]));
        }
        for(int i = 0; i < adj.size(); i++){
            x = prod(x, i + 1);
        }
        return x;
    }
};