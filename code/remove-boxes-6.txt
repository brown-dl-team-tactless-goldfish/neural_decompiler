class Solution {
public:  
  int n;
  vector<vector<vector<int>>> dp;
  
  int helper(vector<int> &boxes, int i, int j, int s){
    if(i > j) return 0;
        
    if(i == j) return (s+1)*(s+1);
        
    if(dp[i][j][s] != -1) return dp[i][j][s];
        
    int tmp_max = (s+1)*(s+1) + helper(boxes,i+1,j,0); 
        
    for(int k = i+1; k <= j; k++) 
      if(boxes[k] == boxes[i]) 
        tmp_max = max(tmp_max,helper (boxes, i+1, k-1, 0) + helper(boxes, k, j, s+1));
            
    return dp[i][j][s] = tmp_max;
  }
  
  int removeBoxes(vector<int>& boxes){
    n = boxes.size(); 
    dp.resize(n, vector<vector<int>>(n, vector<int>(n , -1)));
        
    return helper(boxes , 0, n - 1, 0);
  }  
};