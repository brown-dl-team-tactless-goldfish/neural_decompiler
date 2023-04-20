class Solution {
public:
    int numPoints(vector<vector<int>>& p, int r) {
        int n = p.size();
        vector<vector<double>> dist(n, vector<double>(n));
        for (int i=0; i<n; ++i) {
            for (int j=0; j<n; ++j) {
                dist[i][j] = dist[j][i] = sqrt((p[i][0] - p[j][0]) * (p[i][0] - p[j][0]) + (p[i][1] - p[j][1]) * (p[i][1] - p[j][1]));
            }
        }
        
        int res = 1;
        for (int i=0; i<n; ++i) {
            vector<pair<double, bool>> angles;
            
            for (int j=0; j<n; ++j) {
                if (j != i && dist[i][j] <= 2 * r) {
                    double A = atan2(p[j][1] - p[i][1], p[j][0] - p[i][0]);
                    double B = acos(dist[i][j] / (2.0 * r));
                    double alpha = A-B; 
                    double beta = A+B; 
                    angles.push_back(make_pair(alpha, false)); // "false" means this point is entering
                    angles.push_back(make_pair(beta, true)); // "true" means this point is exiting
                }
            }
            
            sort(angles.begin(), angles.end());  // sort the angles
            
            int cnt = 1;
            for (auto it=angles.begin(); it!=angles.end(); ++it) 
            { 
                if ((*it).second == false) cnt++;   // if the point is entering, then increment
                else cnt--; // if it is exiting, then decrement

                res = max(res, cnt);
            } 
        }
        return res;
    }
};