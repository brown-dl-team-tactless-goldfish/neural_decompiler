class Solution {
public:
   int minFlips(string s) {
        int n=s.size();
        vector<vector<int> > cnt(2, vector<int>(2, 0));
        
        for(int i=0; i<n; i++){
            cnt[s[i]-'0'][i%2]++;
        }
        int ans=cnt[1][0]+cnt[0][1]; 
        ans=min(ans, cnt[0][0]+cnt[1][1]); 
        for(int i=0; i<n; i++){
            cnt[s[i]-'0'][i%2]--;
            cnt[s[i]-'0'][(n+i)%2]++;
            ans=min(ans, cnt[1][0]+cnt[0][1]);
            ans=min(ans, cnt[0][0]+cnt[1][1]);
        }
        return ans;
    }

};