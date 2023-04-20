class Solution {
public:
    vector<int> topologicalSort(vector<vector<int>> &graph, vector<int> &inDegree) {
        queue<int> q;
        for(int i=1; i<graph.size(); i++) {
            if(inDegree[i] == 0)
                q.push(i);
        }
        vector<int> v;
        while(!q.empty()) {
            int a = q.front();
            q.pop();
            v.push_back(a);
            for(int g: graph[a]) {
                if(--inDegree[g] == 0)
                    q.push(g);
            }
        }
        return v;
    }
    
    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        vector<int> rowMat, colMat, rowInDegree(k+1, 0), colInDegree(k+1, 0);
        vector<vector<int>> graph(k+1), res(k, vector<int>(k, 0));
        for(auto row: rowConditions) {
            graph[row[0]].push_back(row[1]);
            rowInDegree[row[1]]++;
        }
        rowMat = topologicalSort(graph, rowInDegree);
        graph = vector<vector<int>>(k+1);
        for(auto col: colConditions) {
            graph[col[0]].push_back(col[1]);
            colInDegree[col[1]]++;
        }
        colMat = topologicalSort(graph, colInDegree);
        if(rowMat.size() != k || colMat.size() != k) {
            return {};
        }
        for(int i=1; i<=k; i++) {
            int r,c;
            for(int j=0; j<k; j++) {
                if(rowMat[j] == i) {
                    r = j;
                    break;
                }
            }
            for(int j=0; j<k; j++) {
                if(colMat[j] == i) {
                    c = j;
                    break;
                }
            }
            res[r][c] = i;
        }
        return res;
    }
};