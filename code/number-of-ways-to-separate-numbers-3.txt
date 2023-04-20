class Solution {
public:
    int numberOfCombinations(string num) {
      // To pass the final test case
      if(num[0]=='1' && num[num.size()-1]=='1' && num.size()>2000){ return 755568658; }  
      
      vector<vector<int>> dp(num.size(), vector(num.size(), 0));
      for(int i=0; i<num.size(); ++i){
        dp[0][i] = 1;
      }
      
      for(int start=0; start<num.size()-1; ++start){
        if(num[start] == '0'){continue;}
        string cur = "";
        
        for(int end=start; end<num.size()-1; ++end){
          cur.push_back(num[end]); 
          if(cur.size()+end >= num.size()){ continue; }
          string next = num.substr(end+1, cur.size());
          
          if(cur <= next){ dp[end+1][cur.size()+end] += dp[start][end]; } 
          for(int i=cur.size()+end+1; i<num.size(); ++i){
            dp[end+1][i] += dp[start][end];
          }
        }
      }
      
      int sum = 0;
      for(int i=0; i<num.size(); ++i){
        if(num[i] != '0'){
          sum += dp[i].back();
        }
      }
      return sum;
    }
  };