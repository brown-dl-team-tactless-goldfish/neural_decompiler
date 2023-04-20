class LockingTree {
public:
    vector<int> parent, locked;
    vector<vector<int>> child;
    
    LockingTree(vector<int>& p) {
        int n = p.size();
        child.resize(n);
        locked.resize(n, -1);
        parent = p;
        for(int i = 1 ; i < n; i++)
            child[p[i]].push_back(i);
    }
    
    bool isLockedChild(int& a){
        if(a == -1) return false;
        if(locked[a] != -1) return true;
        for(auto& c: child[a])
            if(isLockedChild(c)) return true;
        return false;
    }
    
    bool isLockedParent(int& a){
        if(a == -1) return false;
        if(locked[a] != -1) return true;
        return isLockedParent(parent[a]);
    }
    
    bool checkNode(int& num){
        return isLockedChild(num) && !isLockedParent(num);
    }
    
    bool lock(int num, int user) {
        if(locked[num] != -1)
            return false;
        locked[num] = user;
        return true;
    }
    
    bool unlock(int num, int user) {
        if(locked[num] == -1 || locked[num] != user)
            return false;
        locked[num] = -1;
        return true;
    }
    
    bool upgrade(int num, int user) {
        if(!checkNode(num)) return false;
        queue<int> q;
        q.push(num);
        while(!q.empty()){
            int sz = q.size();
            while(sz--){
                int node = q.front();
                q.pop();
                if(node == -1) continue;
                locked[node] = -1;
                for(auto& c: child[node])
                    q.push(c);
            }
        }
        locked[num] = user;
        return true;
    }
};