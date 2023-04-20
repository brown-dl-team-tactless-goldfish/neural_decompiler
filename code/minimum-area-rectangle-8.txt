class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        int ans = INT_MAX;
        unordered_map<int, unordered_set<int>> mymap;
        
        for (auto p : points) {
            mymap[p[0]].insert(p[1]);
        }
        
        /*
            A ----------------------------D
            |(x1, y1)             (x2, y1)|
            |                             |
            |(x1, y2)             (x2, y2)|  
            C ----------------------------B
        */
        
        for (int i = 0; i < points.size(); i++) {
            for (int j = i+1; j < points.size(); j++) {
                int x1 = points[i][0];  // A
                int y1 = points[i][1];  // A
                int x2 = points[j][0];  // B
                int y2 = points[j][1];  //B
                
                if ((x1 != x2) && (y2 != y1)) { // diagonal
                    if (mymap[x1].find(y2) != mymap[x1].end() && mymap[x2].find(y1) != mymap[x2].end()) { // C & D
                        ans = min(ans, (abs(x1-x2) *abs(y1-y2)));
                    }
                }
            }
        }

        return ((ans == INT_MAX) ? 0: ans);
    }
};