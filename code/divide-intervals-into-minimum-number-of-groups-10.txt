class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {

        int line[1000005] = {};
        int maxEle = -1;

        for(auto &e : intervals) {
            int start = e[0], end = e[1];
            line[start] += 1;
            line[end + 1] -= 1;
        }

        for(int i = 1; i < 1000001; i++) {
            line[i] += line[i - 1];
            maxEle = max(maxEle, line[i]);
        }

        return maxEle;
    }
};