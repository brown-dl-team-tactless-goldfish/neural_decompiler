class Solution {
private:
    // Check if an area is empty according to prefix sum
    bool areaEmpty(vector<vector<int>> &ps, int r, int c, int h, int w) {        
        return (ps[r][c] - ps[r - h][c] - ps[r][c - w] + ps[r - h][c - w] == 0);
    }
    
public:
    bool possibleToStamp(vector<vector<int>>& grid, int sH, int sW) {
        
        int rSize = grid.size();
        int cSize = grid[0].size();
        
        // Part 1: 2d prefix sum for slots that area that is occupied
        vector<vector<int>> slotPs (rSize + 1, vector<int>(cSize + 1, 0));
        for (int r = 0; r < rSize; r++) {
            for (int c = 0; c < cSize; c++) {
                slotPs[r + 1][c + 1] = slotPs[r + 1][c] + grid[r][c];
            }
        }
        
        for (int c = 0; c < cSize; c++) {
            for (int r = 0; r < rSize; r++) {
                slotPs[r + 1][c + 1] = slotPs[r][c + 1] + slotPs[r + 1][c + 1];
            }
        }
        
        // Part 2: Edge case handling
        if (slotPs[rSize][cSize] == rSize * cSize) return true;
        if (sH > rSize || sW > cSize) return false;
        
        // Part 3: slots in which we can place a stamp (mark the bottom right of the stamp)
        vector<vector<int>> stampPs(rSize + 1, vector<int>(cSize + 1, 0));
        for (int r = sH; r <= rSize; r++) {
            for (int c = sW; c <= cSize; c++) {
                if (grid[r - 1][c - 1] == 1) continue;
                stampPs[r][c] = (int)areaEmpty(slotPs, r, c, sH, sW);
            }
        }
        
        // Part 4: 2d prefix sum for slots in which we can place a stamp
        for (int r = 0; r < rSize; r++) {
            for (int c = 0; c < cSize; c++) {
                stampPs[r + 1][c + 1] = stampPs[r + 1][c] + stampPs[r + 1][c + 1];
            }
        }
        
        for (int c = 0; c < cSize; c++) {
            for (int r = 0; r < rSize; r++) {
                stampPs[r + 1][c + 1] = stampPs[r][c + 1] + stampPs[r + 1][c + 1];
            }
        }
        
        // Part 5: scan adjacent area to see if there is a stamp covering the empty slot
        for (int r = 1; r <= rSize; r++) {
            for (int c = 1; c <= cSize; c++) {
                if (grid[r - 1][c - 1] == 1) continue;
                int scanRMax = min(rSize, r + sH - 1), scanCMax = min(cSize, c + sW - 1);
                if (areaEmpty(stampPs, scanRMax, scanCMax, scanRMax - r + 1, scanCMax - c + 1)) {
                    return false;
                }
            }
        }
        return true;
    }
};