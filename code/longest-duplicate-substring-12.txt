class SA {
public:
    vector<int> p;
    vector<int> cnt;
    vector<vector<int>> c;
    vector<int> logs;
    const int alphabet = 256;
    int n;
    string s;
    SA(string s) {
        int i;
        this->n = (int) s.size();
        this->s = s;
        p = vector<int>(n, 0);
        cnt = vector<int>(max(alphabet, n), 0);
        logs = vector<int>(n + 5, 0);
        for (i = 2; i <= n; ++i) {
            logs[i] = logs[i/2] + 1;
        }
        
        c = vector<vector<int>>(logs[n] + 2, vector<int>(n+1, 0));
    }

    void sort_cyclic_shifts() {
        int h, i;
        for (i = 0; i < n; i++)
            cnt[(int) s[i]]++;
        for (i = 1; i < alphabet; i++)
            cnt[i] += cnt[i-1];
        for (i = 0; i < n; i++)
            p[--cnt[(int) s[i]]] = i;
        c[0][p[0]] = 0;
        int classes = 1;
        for (i = 1; i < n; i++) {
            if (s[p[i]] != s[p[i-1]])
                classes++;
            c[0][p[i]] = classes - 1;
        }

        vector<int> pn(n), cn(n);
        for (h = 0; (1 << h) < n; ++h) {
            for (i = 0; i < n; i++) {
                pn[i] = p[i] - (1 << h);
                if (pn[i] < 0)
                    pn[i] += n;
            }
            fill(cnt.begin(), cnt.begin() + classes, 0);
            for (i = 0; i < n; i++)
                cnt[c[h][pn[i]]]++;
            for (i = 1; i < classes; i++)
                cnt[i] += cnt[i-1];
            for (i = n-1; i >= 0; i--)
                p[--cnt[c[h][pn[i]]]] = pn[i];
            cn[p[0]] = 0;
            classes = 1;
            for (i = 1; i < n; i++) {
                pair<int, int> cur = {c[h][p[i]], c[h][(p[i] + (1 << h)) % n]};
                pair<int, int> prev = {c[h][p[i-1]], c[h][(p[i-1] + (1 << h)) % n]};
                if (cur != prev)
                    ++classes;
                cn[p[i]] = classes - 1;
            }
            
            for (i = 0 ; i < n; ++i) {
                c[h+1][i] = cn[i];
            }
            
        }
    }

    void generate() {
        int i;
        sort_cyclic_shifts();
        for (i = 0 ; i < (int) s.size() - 1; ++i) {
            p[i] = p[i+1];
        }
    }

    int lcp(int i, int j) {
        int ans = 0, k;
        for (k = logs[n]; k >= 0; k--) {
            if (c[k][i] == c[k][j]) {
                ans += 1 << k;
                i += 1 << k;
                j += 1 << k;
            }
        }
        return ans;
    }
};

class Solution {
public:
    string longestDupSubstring(string S) {
        int pos = -1, i, n = S.length();
        int ans = 0;
        string ret;
        S += '$';
        SA sa = SA(S);
        sa.generate();
        for (i = 0 ; i < n - 1; ++i) {
            int len = sa.lcp(sa.p[i], sa.p[i+1]);
            if (ans < len) {
                ans = len;
                pos = sa.p[i];
            }
        }
        
        for (i = pos; i < pos + ans; ++i) {
            ret += S[i];
        }
        
        return ret;
    }
};