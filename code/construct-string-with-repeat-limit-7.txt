#define deb(x) cout << #x << " = " << x << endl
class Solution {
public:
    string repeatLimitedString(string s, int rL) {
        map<char,int> m ;
        for (int i =0;i<26;i++)m[i+'a']=0;
        for (int i = 0 ;i <s.length();i++)
            m[s[i]]++;
        string res = "";
        priority_queue <pair<int,int>>pq ;
        for(int i =0 ;i<26;i++) if(m[i+'a'])pq.push({i+'a',m[i+'a']});
        while(!pq.empty()){
            char c = pq.top().first;
            int x = pq.top().second;
            pq.pop();
            int leftOvers = x-rL;
            // deb(c);
            // deb(x);
            if(leftOvers<=0){
                if(res.length()){
                    if(res[res.length()-1]==c) continue;
                }
                while(x){
                    res+=c;
                    x--;
                }
            }else{
                while(x!=leftOvers){
                    res+=c;
                    x--;
                }
                if(pq.empty()) return res;
                char ctemp = pq.top().first;
                int xtemp = pq.top().second;
                pq.pop();
                res+=ctemp;
                xtemp--;
                pq.push({c,leftOvers});
                if(xtemp) pq.push({ctemp,xtemp});
            }
        }
        return res;
    }
};