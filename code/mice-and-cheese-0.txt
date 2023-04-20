class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        int n = reward1.size();
        vector<pair<int,int>> t;
      for(int i=0;i<n;++i){
          t.push_back({reward1[i],reward2[i]});
      }
      sort(t.begin(),t.end(),[](auto &p1, auto &p2){
          return p1.first - p1.second > p2.first - p2.second;
      });
      int ans = 0;
      for(int i=0;i<n;i++){
          if(i<k)
            ans+=t[i].first;
          else
            ans+=t[i].second;
      }
      return ans;
    }  
};