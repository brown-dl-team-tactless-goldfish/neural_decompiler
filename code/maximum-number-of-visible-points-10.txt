class Solution {
public:
    double PI = 3.141592;
    int visiblePoints(vector<vector<int>>& points, int angle, vector<int>& location) {
	    // 1 Move your location to (0, 0) and move all points.
        for (auto & p : points) {
            p[0] -= location[0];
            p[1] -= location[1];
        }
        
        vector<double> angles;
        int atLocation = 0;
        for (auto & p : points) {
            // 2 Keep count on all points already at location. 
            if (p[0] == 0 && p[1] == 0)
                atLocation++;
            else // 3 Use atan2 to convert all points into angles array.
                angles.push_back(atan2(p[1], p[0]));
        }
        
        // 4 Sort angles array ascendingly.
        sort(angles.begin(), angles.end());
        
        // 5 Copy each angle by adding 360 degree(2*PI) and append to angles array.
        int size = angles.size();
        for (int i = 0; i < size; i++) {
            angles.push_back(2 * PI + angles[i]);
        }
        
        double angleWindow = 1.0 * angle / 180 * PI;
        int res = 0;
        // 6 For each angle, see how many angles are in the visible window.
        for (int i = 0; i < angles.size() / 2; i++) {
            auto it = upper_bound(angles.begin() + i, angles.end(), angles[i] + angleWindow);  
            it--; 
            res = max(res, int(it - angles.begin()) -  i + 1);
        }
        
        return res + atLocation;
    }
};