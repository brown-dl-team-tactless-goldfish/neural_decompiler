class Solution {
public:
    int dp[9][9][9][9][140];
    int dx[4] = {0,1,0,-1};
    int dy[4] = {1,0,-1,0};
    
    bool solve(vector<string>& grid, int catJump, int mouseJump, int catR, int catC, int mouseR, int mouseC, int moves){        
        int r = grid.size(), c = grid[0].size();
        if(moves >= 128) return false;
        if(mouseR==catR && mouseC==catC) return false;
        if(grid[catR][catC] == 'F') return false;
        if(grid[mouseR][mouseC] == 'F') return true;
        
        if(dp[catR][catC][mouseR][mouseC][moves] != -1) 
            return dp[catR][catC][mouseR][mouseC][moves];
        
        if(moves%2 == 0){
            for(int i=0; i<4; ++i){
                for(int j=0; j<=mouseJump; ++j){
                    int x = mouseR+j*dx[i], y = mouseC+j*dy[i];
                    if(x>=0 && x<r && y>=0 && y<c && grid[x][y]!='#'){
                        if(solve(grid, catJump, mouseJump, catR, catC, x, y, moves+1) == true) 
                            return dp[catR][catC][mouseR][mouseC][moves] = true;
                    }else break;
                }
            }
            return dp[catR][catC][mouseR][mouseC][moves] = false;
        }else{
            for(int i=0; i<4; ++i){
                for(int j=0; j<=catJump; ++j){
                    int x = catR+dx[i]*j, y = catC+dy[i]*j;
                    if(x>=0 && x<r && y>=0 && y<c && grid[x][y]!='#'){
                        if(solve(grid, catJump, mouseJump, x, y, mouseR, mouseC, moves+1) == false) 
                            return dp[catR][catC][mouseR][mouseC][moves] = false; 
                    }else break;
                }
            }
            return dp[catR][catC][mouseR][mouseC][moves] = true;
        }
    }
    
    bool canMouseWin(vector<string>& grid, int catJump, int mouseJump) {
       memset(dp,-1,sizeof(dp));
        int r = grid.size(), c =grid[0].size();
        int catR, catC, mouseR, mouseC;
        for(int i=0; i<r; ++i){
            for(int j=0; j<c; ++j){
                if(grid[i][j] == 'C'){
                    catR = i, catC = j;
                }
                else if(grid[i][j] == 'M'){
                    mouseR = i, mouseC = j;
                }
            }
        }
        
        return solve(grid, catJump, mouseJump, catR, catC, mouseR, mouseC, 0);
    }
};