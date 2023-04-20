class Solution {
public:

    string smallestSubsequence(string s, int k, char letter, int rep) {
        int n = s.length();
        
        //cnt[i] store the count of letter in suffix [i, n-1]
        vector<int> cnt(n); 
        cnt[n-1] = (s[n-1]==letter);
        for(int i=n-2; i>=0; --i) cnt[i] = cnt[i+1] + (s[i]==letter);
        
        
        //for each character, store its indexe(s
        
        vector<deque<int>> ind(26);
        for(int i=0; i<n; ++i) ind[s[i]-'a'].push_back(i);
        
        
        int x = rep, lastInd=-1;
        string ans = "";
        for(int j=0; j<k; ++j){
            for(int ch=0; ch<26; ++ch){
                auto &dq = ind[ch];
                
                //remove invalid indexes
                while(dq.size() && dq.front() <= lastInd) dq.pop_front();
                if(!dq.size()) continue;
                
                //check if current index satisfies the conditions 
                auto index = dq.front();
                if(ans.length() + n-index >= k && cnt[index] >= x && (x-(ch+'a'==letter)+j+1 <= k)){
                    ans += ch+'a';
                    if(ch+'a'==letter) x--;   
                    lastInd = index;  
                    dq.pop_front();
                    break;
                }

            }
        }
        
        return ans;
    }




};