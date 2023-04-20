class Solution {
public:
    string getWord(const string& expr, int& i) {
        string res;
        while ('a' <= expr[i] && expr[i] <= 'z')
            res.push_back(expr[i++]);
        return res;
    }

    unordered_set<string> dfs(const string& expr, int& i) {
        unordered_set<string> res;

        unordered_set<string> S;
        while (i < int(expr.length()) && expr[i] != '}') {
            if (expr[i] == ',') {
			    // union
                for (auto& it : S)
                    res.insert(it);
                S.clear();
                i++;
            }
            unordered_set<string> t;
            if (expr[i] == '{') {
                i++;
                t = dfs(expr, i);
                i++;
            } else {
                t.insert(getWord(expr, i));
            }

            if (S.empty())
                S = t;
            else {
			    // cartesian product
                unordered_set<string> S2;
                for (auto& it1 : S) {
                    for (auto& it2 : t)
                        S2.insert(it1 + it2);
                }
                swap(S, S2);
            }
        }
        // union
        for (auto& it : S)
            res.insert(it);

        return res;
    }

    vector<string> braceExpansionII(string expression) {
        int i = 0;
        unordered_set<string> S = dfs(expression, i);

        vector<string> res;
        for (auto& it : S)
            res.push_back(it);
        sort(res.begin(), res.end());

        return res;
    }
};