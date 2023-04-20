class Solution {
public:
    vector<double> getCollisionTimes(vector<vector<int>>& cars) {
        int numcars = cars.size();
        stack<int> st;
        
        vector<double> result(numcars, 0.0);
        
        result[numcars-1] = -1.00000;
        st.push(numcars-1);

        double distance, time;
        for (int i = numcars-2; i>=0; i--) {
            time = -1;
            while (!st.empty()) {
                auto curcar = st.top();
                if (cars[curcar][1] >= cars[i][1]) {
                    st.pop();
                    continue;
                }
                distance = (cars[curcar][0]-cars[i][0]) * 1.0;
                double timetaken = distance/ (cars[i][1]-cars[curcar][1]);
                if (result[curcar] == -1) {
                    time = timetaken;
                    break;
                } else if (result[curcar] > timetaken) {
                    time = timetaken;
                    break;
                } else {
                    st.pop();
                    continue;
                }
            }
            result[i] = time;
            st.push(i);
        }
        return result;
    }
};