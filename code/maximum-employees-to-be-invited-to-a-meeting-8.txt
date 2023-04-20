class Solution {
public:
    int maximumInvitations(vector<int>& favorite) {
        g = move(favorite);
        n = g.size();
        isPair.resize(n);
        greverse.resize(n);
        findPair();
        vector<int> result(n, 0), visited(n, 0);
        for(int i=0;i<n;i++) {
            if(g[g[i]] != i) greverse[g[i]].push_back(i);
        }
        for(int i=0;i<n;i++)
            if(isPair[i]) result[i] = depth(i, visited);

        int maxCircle = 0;
        for(int i=0;i<n;i++)
            findCircle(i, visited, maxCircle);

        int pairSum = 0;
        for(int i=0;i<n;i++){
            if(!isPair[i]) continue;
            int j = g[i];
            pairSum +=  result[i] + result[j];
        }
        return max(maxCircle, pairSum/2) ;
    }

    void findPair(){
        for(int i=0;i<g.size();i++){
            if(g[g[i]] == i) {
                isPair[i] = isPair[g[i]] = true;
            }
        }
    }

    int depth(int i, vector<int>& visited){
        visited[i] = true;
        int res = 0;
        for(auto j:greverse[i]){
            res = max(res, depth(j, visited));
        }
        return 1+res;
    }

    void findCircle(int i, vector<int>& visited, int& res){
        if(visited[i]) return;
        unordered_map<int,int> visiting;
        while(visiting[i] < 2){
            if(visited[i]) break;
            visiting[i]++;
            i = g[i];
        }

        int count = 0;
        for(auto [x, n] : visiting){
            visited[x] = true;
            if(n>1) count++;
        }
        res = max(res, count);
    }


    int n;
    vector<int> g;
    vector<vector<int>> greverse;
    vector<bool> isPair;
};