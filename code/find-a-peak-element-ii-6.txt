class Solution {
public:
    
    vector<int> findPeakGrid(vector<vector<int>>& grid) {
        int r = grid.size() , c = grid[0].size() ;
        
        //traverse in each row and apply binary seach
        for(int i = 0 ; i < r ; ++i ){
            int lo = 0 , hi = c - 1 ;
            while(lo <= hi){
                int mid = lo + (hi-lo) / 2 ;
                
                int U = i - 1 >= 0 ? grid[i-1][mid] : INT_MIN ;
                int D = i + 1 < r ? grid[i + 1][mid] : INT_MIN ;
                int L = mid - 1 >= 0 ? grid[i][mid - 1] : INT_MIN ;
                int R = mid + 1 < c ? grid[i][mid + 1] : INT_MIN ;
                
                if(grid[i][mid] >= U and grid[i][mid] >= R and grid[i][mid] >= D and grid[i][mid] >= L) return {i,mid} ;
                else if(L >= R) hi = mid - 1 ;
                else if(R > L) lo = mid  + 1 ;
                else break ;
            }
        }
        
        return {-1,-1} ;
    }
};