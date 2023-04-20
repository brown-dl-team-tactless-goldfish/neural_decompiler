class Solution {
    struct cmp {
        bool operator()(vector<string> x, vector<string> y) {   // sort terms by degree
            if (x.size() == y.size()) return x < y;
            else return x.size() > y.size();
        }
    };
    
    map<vector<string>, int, cmp> helper(string& expr,  unordered_map<string, int>& eval) {
        map<vector<string>, int, cmp> local = {{{}, 1}}, global;
        string sub = "";
        for (int i = 0, sign = 1, n = expr.size(); i <= n; ++i) {
            if (i < n && expr[i] == ' ') continue;  // skip space
            if (i < n && isalnum(expr[i])) sub += expr[i];  // number and alphabet, add to sub expression
            else if (i < n && expr[i] == '(') { // parenthesis
                i ++;
                for (int p = 1; ; ++i) {    // get the sub expression in parenthesis
                    if (expr[i] == '(') p ++;
                    else if (expr[i] == ')') p --;
                    if (p == 0) break;
                    sub += expr[i];
                }
            }
            else {  // '+', '-', '*' or i == n
                if (sub.size() == n) {  // the whole expression is a number or variable
                    if (eval.count(sub)) return {{{}, eval[sub]}};  // variable is found in eval list 
                    if (isdigit(sub[0])) return {{{}, stoi(sub)}};  // number
                    return {{{sub}, 1}};    // variable
                }
                map<vector<string>, int, cmp> mult, submp = helper(sub, eval);
                for (auto l : local) {  // multiply local with sub
                    for (auto r : submp) {
                        auto k = l.first;
                        k.insert(k.end(), r.first.begin(), r.first.end());
                        sort(k.begin(), k.end());
                        mult[k] += l.second * r.second;
                    }
                }
                local = move(mult);
                if (i == n || expr[i] != '*') {  // '+' or '-'
                    for (auto& t : local)   // add local to global
                        global[t.first] += sign * t.second;
                    sign = i < n && expr[i] == '-' ? -1 : 1;
                    local = {{{}, 1}};  // reset local
                }
                sub = "";   // reset sub
            }
        }
        return global;
    }
    
public:
    vector<string> basicCalculatorIV(string expression, vector<string>& evalvars, vector<int>& evalints) {
        unordered_map<string, int> eval;
        for (int i = 0; i < evalvars.size(); ++i)
            eval[evalvars[i]] = evalints[i];
        vector<string> res;
        auto resmp = helper(expression, eval);
        for (auto param : resmp) {
            if (param.second == 0) continue;    // skip zero coefficient
            res.push_back(to_string(param.second));
            for (auto p : param.first) res.back() += "*" + p;
        }
        return res;
    }
};