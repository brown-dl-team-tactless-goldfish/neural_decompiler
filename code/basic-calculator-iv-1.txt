class Solution {
public:
    const map<pair<int, string>, int> evaluate(queue<map<pair<int, string>, int>>& es, queue<char>& os) {
        deque<map<pair<int, string>, int>> qe;
        deque<char> qo;
        
        if (es.size() == os.size()) {
            qe.push_back({{{0, ""}, 0}});
        } else {
            qe.push_back(es.front());
            es.pop();
        }
        
        const auto sorted = [](const pair<int, string>& k1, const pair<int, string>& k2) {
            map<string, int> cnts;
            string t;
            for (const char& c: k1.second) {
                if (c == '*') {
                    cnts[t]++;
                    t.clear();
                } else {
                    t += c;
                }
            }
            cnts[t]++;
            t.clear();
            for (const char& c: k2.second) {
                if (c == '*') {
                    cnts[t]++;
                    t.clear();
                } else {
                    t += c;
                }
            }
            cnts[t]++;
            t.clear();
            for (const auto&[k, v]: cnts)
                for (int i = 0; i < v; ++i)
                    if (!k.empty())
                        t += k + '*';
            
            if (!t.empty()) t.pop_back();
            return make_pair(k1.first + k2.first, t);
        };
        
        while (!es.empty()) {
            if (os.front() == '*') {
                map<pair<int, string>, int> p;
                for (const auto& [k1, v1]: qe.back())
                    for (const auto& [k2, v2]: es.front())
                        p[sorted(k1, k2)] += v1 * v2;
                        
                qe.pop_back();
                qe.push_back(p);
            } else {
                qo.push_back(os.front());
                qe.push_back(es.front());
            }
            es.pop();
            os.pop();
        }
        
        while (!qo.empty()) {
            auto e = qe.front();
            qe.pop_front();
            for (const auto& [k, v]: qe.front())
                qo.front() == '+' ? e[k] += v : e[k] -= v;
            qe.pop_front();
            qo.pop_front();
            qe.push_front(e);
        }
        
        return qe.front();
    }
    
    vector<string> basicCalculatorIV(string expression, vector<string>& evalvars, vector<int>& evalints) {
        expression += '!';
        unordered_map<string, int> known;
        int n(evalvars.size());
        for (int i = 0; i < n; ++i)
            known[evalvars[i]] = evalints[i];
        
        stack<queue<map<pair<int, string>, int>>> operands;
        stack<queue<char>> operators;
        string t;
        map<pair<int, string>, int> res;
        operands.push({});
        operators.push({});
        
        const auto is_num = [](const string& s) {
            for (const char& c: s)
                if (!isdigit(c))
                    return false;
            return true;
        };
        
        for (const char& c: expression) {
            if (c == ' ') continue;
            if (c == '(') {
                operands.push({});
                operators.push({});
            } else if (isalnum(c)) {
                t += c;
            } else {        
                if (!t.empty()) {
                    if (is_num(t)) {
                        operands.top().push({{{0, ""}, stoi(t)}});
                    } else if (known.count(t)) {
                        operands.top().push({{{0, ""}, known[t]}});
                    } else {
                        operands.top().push({{{-1, t}, 1}});
                    }
                }
                
                t.clear();
                if (c == ')' || c == '!') {
                    res = evaluate(operands.top(), operators.top());
                    operands.pop();
                    operators.pop();
                    if (c == '!') break;
                    operands.top().push(res);
                } else {
                    operators.top().push(c);
                }
            }
        }
        
        vector<string> ans(res.size());
        int i(0);
        for (const auto&[k, v]: res)
            if (v) ans[i++] = to_string(v) + (k.second.empty() ? "" : "*" + k.second);
            
        ans.resize(i);
        return ans;
    }
};