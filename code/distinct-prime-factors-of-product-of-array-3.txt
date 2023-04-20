class Solution {
public:
    vector<int> helper(int n){
      int c = 2;
      vector<int> res;
      while(n > 1){
        if(n % c == 0){
          res.emplace_back(c);
          n /= c;
        } else c++;
      }
      return res;
    }
    
    int distinctPrimeFactors(vector<int>& v) {
      unordered_set<int> s;
      for(auto &i: v){
        auto temp = helper(i);
        for(auto &e: temp) s.insert(e);
      }
      return s.size();
    }
};