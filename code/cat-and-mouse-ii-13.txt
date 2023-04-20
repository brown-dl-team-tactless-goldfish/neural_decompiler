int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
class Solution {
public:
    int catJump, mouseJump, rows, cols, foodX, foodY, dp[71][9][9][9][9];
    vector<string>grid;
    
    bool canMouseWin(vector<string>& matrix, int cJump, int mJump) {
        grid = matrix; rows = grid.size(); cols = grid[0].size();
        int mouseX, mouseY, catX, catY;
        catJump = cJump; mouseJump = mJump;
        for(int i = 0; i < grid.size(); ++i) {
            for(int j = 0; j < grid[0].size(); ++j) {
                if(grid[i][j] == 'M') {
                    mouseX = i, mouseY = j;
                }
                if(grid[i][j] == 'C') {
                    catX = i, catY = j;
                }
                if(grid[i][j] == 'F') {
                    foodX = i, foodY = j;
                }
            }
        }
        memset(dp,-1,sizeof(dp));
        return canWin(0, mouseX, mouseY, catX, catY);
    }
    
    bool canWin(int turn, int mouseX, int mouseY, int catX, int catY) {
        if((catX == mouseX && catY == mouseY)||(catX == foodX && catY == foodY) || turn >= 70) {
            return turn%2 == 1;
        }
        if(mouseX == foodX && mouseY == foodY) {
            return turn%2 == 0;
        }
       
        if(dp[turn][mouseX][mouseY][catX][catY] != -1) {
            return dp[turn][mouseX][mouseY][catX][catY];
        }
        
        int jumps = turn%2==0? mouseJump: catJump;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j <= jumps; ++j) {
                int nMouseX = mouseX + (turn%2==0)*j*dx[i], nMouseY = mouseY + (turn%2==0)*j*dy[i], nCatX = catX + + (turn%2==1)*j*dx[i], nCatY = catY + (turn%2==1)*j*dy[i];
                if(nMouseX < 0 || nMouseY < 0 || nMouseX >= rows || nMouseY >= cols || nCatX < 0 || nCatY < 0 || nCatX >= rows || nCatY >= cols || grid[nMouseX][nMouseY] == '#' || grid[nCatX][nCatY] == '#')
                    break;
                if(!canWin(turn+1, nMouseX, nMouseY, nCatX, nCatY))
                    return dp[turn][mouseX][mouseY][catX][catY] = true;
            }
        }
        return dp[turn][mouseX][mouseY][catX][catY] = false;
    }
};