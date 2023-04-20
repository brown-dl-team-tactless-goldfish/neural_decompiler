class Solution {
public:
    unordered_map<int, int> mp; //used for compression
    int tree[8000]; //tree[i] holds the maximum height for its corresponding range
    
    void update(int t, int low, int high, int i, int j, int h){
        if(i>j)
            return;
        if(low==high){
            tree[t]=h;
            return;
        }
        int mid=low+((high-low)/2);
        update(2*t, low, mid, i, min(mid, j), h);
        update(2*t+1, mid+1, high, max(mid+1, i), j, h);
        tree[t]=max(tree[2*t], tree[2*t+1]);
    }
    
    int query(int t, int low, int high, int i, int j){
        if(i>j)
            return -2e9;
        if(low==i && high==j)
            return tree[t];
        int mid=low+((high-low)/2);
        return max(query(2*t, low, mid, i, min(mid, j)), query(2*t+1, mid+1, high, max(mid+1, i), j));
    }
    
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        set<int> s;
        memset(tree, 0, sizeof(tree));
        for(auto it: positions){
            s.insert(it[0]);
            s.insert(it[0]+it[1]-1);
        }
        int compressed=1, n=positions.size();
        vector<int> ans(n);
        for(auto it: s)
            mp[it]=compressed++;
        for(int i=0; i<n; i++){
            int start=positions[i][0], end=positions[i][1]+start-1, h=positions[i][1];
            int curr=query(1, 1, 2*n, mp[start], mp[end]), ncurr=curr+h;
            update(1, 1, 2*n, mp[start], mp[end], ncurr);
            ans[i]=tree[1]; 
        }
        return ans;
    }
};