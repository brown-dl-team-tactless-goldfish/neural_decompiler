template <typename T>
ostream& operator <<(ostream& out, const vector<T>& a) {
  out << "["; bool first = true;
  for (auto v : a) { out << (first ? "" : ", "); out << v; first = 0;} 
  out << "]";
  return out;
}
const int N = 1010;
int f[N];
int g[N];
class Solution {
public:
    vector<int> movesToStamp(string t, string s) {
        vector<int> res;
        queue<int> q;
        memset(f, 0, sizeof(f));
        memset(g, 0, sizeof(g));
        int m = t.size();
        //forward
        for(int i = 0; i < s.size(); i++) {
            for(int j = 0; j < t.size(); j++) {
                if(i + j < s.size() && t[j] == s[i + j]) {
                    f[i]++;
                } else {
                    break;
                }
            }
        }
        //backwoard
        for(int i = s.size() - 1; i >= 0; i--) {
            int cnt = 0;
            for(int j = t.size() - 1; j >= 0; j--) {
                if(i - cnt >= 0 && t[j] == s[i - cnt]) {
                    g[i]++;
                } else {
                    break;
                }
                cnt++;
            }
        }
 
        for(int i = 0; i < s.size(); i++) {
            if(f[i] == t.size()) {
                q.push(i);
                res.push_back(i);
                i = i + (t.size() - 1);
            }
        }
        
        while(q.size() > 0) {
            int sz = q.size();
            for(int i = 0; i < sz; i++) {
                int idx = q.front(); q.pop();
                for(int j = idx; j <= idx + t.size() - 1; j++) {
                    s[j] = '?';
                }
            }
            
            if(finish(s)) {
                break;
            }
            
                      
            vector<int> prefix(s.size());
            int sum = 0;
            for(int j = 0; j < s.size(); j++) {
                sum += (s[j] == '?');
                prefix[j] = sum;
            }
            
            bool forward = false;
            for(int j = 0; j < s.size(); j++) {
                if(s[j] == '?') continue;
                if(j + t.size() - 1 < s.size() && f[j] > 0) {
                    int to = j + f[j];
                    if(cal(prefix, to, j + t.size() - 1) == (t.size() - f[j])) {
                        q.push(j);
                        res.push_back(j);
                        j += (t.size() - 1);
                        forward = true;
                    }
                }
            }
            if(!forward) {
                for(int j = s.size() - 1; j >= 0; j--) {
                    if(s[j] == '?') continue;
                    if(j - m + 1 >= 0 && g[j] > 0) {
                        int to = j - g[j];
                        if(cal(prefix, j - m + 1, to) == (m - g[j])) {
                            q.push(j - m + 1);
                            res.push_back(j - t.size() + 1);
                            j -= (m + 1);
                        }
                    }
                }
            }
        }
        
        
        for(int i = 0; i < s.size(); i++) {
            if(i + t.size() - 1 < s.size()) {
                if(match(s, t, i)) {
                    for(int j = 0; j < t.size(); j++) {
                        s[i + j] = '?';
                    }
                    res.push_back(i);
                }
            }
        }
        
        if(!finish(s)) {
            return {};
        }
        
        reverse(res.begin(), res.end());
        return res;
    }
    
    bool match(string& s, string& t, int idx) {
        for(int i = 0; i < t.size(); i++) {
            if(s[i + idx] == t[i] || s[i + idx] == '?') {
                
            } else {
                return false;
            }
        }
        return true;
    }
    
    bool finish(string& s) {
        int cnt = 0;
        for(char c : s) cnt += (c == '?');
        return cnt == s.size();
    }
    
    int cal(vector<int>& pre, int l, int r) {
        if(l == 0) return pre[r];
        return pre[r] - pre[l - 1];
    }
    
};