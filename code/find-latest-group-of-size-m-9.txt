class Solution {
public:
    
    // classical application of Union Find
    
    int parent[100005];
    int sz[100005];
    int m;
    int idx = -2;
    int i;
    multiset<int> st;
    void makeset(int v){
        parent[v] = v;
        sz[v] = 1;
        st.insert(1);
    }

    int find(int v){
        if(parent[v] == v) return v;
        return parent[v] = find(parent[v]);
    }
    
    void Union(int a,int b){
       
        a = find(a);
        b = find(b);
        if(a == b) return;
        int x = sz[a];
        int y = sz[b];
        if(st.find(x) != st.end())st.erase(st.find(x));
        if(st.find(y) != st.end())st.erase(st.find(y));
        st.insert(x+y);
        if(sz[a]>sz[b]) swap(a,b);
        sz[b]+=sz[a];
        parent[a] = b;
        
    }
    
    int findLatestStep(vector<int>& arr, int _m) {
        m = _m;
        int n = arr.size();
        for(i=0;i<n;i++){
            makeset(arr[i]);
            if(arr[i]!=1){
               if(sz[arr[i]-1]!=0) Union(arr[i],arr[i]-1);   
            }
            if(arr[i]!=n){
                if(sz[arr[i]+1]!=0) Union(find(arr[i]),find(arr[i]+1));   
            }
            if(st.find(m) != st.end()) idx = i;
        }
        
        return idx+1;
    }
};