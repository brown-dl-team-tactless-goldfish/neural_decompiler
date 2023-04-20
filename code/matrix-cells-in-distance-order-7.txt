class Solution {
public:
    vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        vector<vector<int>> ans;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                ans.push_back({r, c});
            }
        }

        sort(ans.begin(), ans.end(), DistFromCenterSorter(rCenter, cCenter));
        return ans;
    }

private:
    struct DistFromCenterSorter {
        int rCenter;
        int cCenter;
        DistFromCenterSorter(int rCenter, int cCenter) {
            this->rCenter = rCenter;
            this->cCenter = cCenter;
        }

        bool operator()(const vector<int>& cell1, const vector<int>& cell2) {
            return distFromCenter(cell1) < distFromCenter(cell2);
        }

        int distFromCenter(const vector<int>& cell) {
            return abs(cell[0] - this->rCenter) + abs(cell[1] - this->cCenter);
        }
    };
};