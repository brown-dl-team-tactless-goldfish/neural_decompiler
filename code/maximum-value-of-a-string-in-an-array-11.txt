class Solution {
public:
    bool ischar(string s )
    {
        for(char c : s )
        {
            if( c >'9' || c < '0') return false;
        }
        return true;
    }
    
    int maximumValue(vector<string>& strs) {
        int ans = 0 ;
        for( int i =0 ; i < strs.size() ; ++i )
        {
            int len = strs[i].size();
            if( ischar(strs[i])){ len = stoi(strs[i]);}
            ans = max(ans,len);
        }
      return ans;   
    }
};