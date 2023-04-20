class Solution {
public:
    unordered_map<string, int> scope;
    vector<string> basicCalculatorIV(string expression, vector<string>& evalvars, vector<int>& evalints) {
        for (int i = 0; i < evalvars.size(); ++i) {
            scope[evalvars[i]] = evalints[i];
        }
        int count = 0;
        string input = removewhitespace(expression);
        auto e = exp(input, count);
        vector<string> result;
        cleanup(e, result);
        return result;
    }
    
    string removewhitespace(string& s) { 
        string withoutspace = "";
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ' ') continue;
            withoutspace += s[i];
        }      
        return withoutspace;
    }
    
    void cleanup(vector<pair<int, vector<string>>>& e, vector<string>& result) {
        auto desc = [&e](auto& a, auto& b) {
            auto av = a.second; auto bv = b.second;
            if (av.size() == bv.size()) {
                for (int i = 0; i < av.size(); ++i) {
                    if (av[i] < bv[i]) return true;
                    if (av[i] > bv[i]) return false;
                }
            } 
            return av.size() > bv.size();
        };
        
        sort(e.begin(), e.end(), desc);
        for (auto [constant, alg] : e) { 
            if (constant == 0) continue;
            string t = to_string(constant); 
            for (string& a : alg) t += "*" + a; 
            result.push_back(t);
        }        
    }
    
    vector<pair<int, vector<string>>> exp(string& s, int& i) {
        auto lhs = term(s, i);
        while (i < s.size() && (s[i] == '+' || s[i] == '-')) {
            char opt = s[i];
            ++i; 
            auto rhs = term(s, i);
            
            map<vector<string>, int> m;
            for (auto& [f, s] : lhs) m[s] += f;
            for (auto& [f, s] : rhs) m[s] += opt == '+' ? f : -1 * f;      
            
            vector<pair<int, vector<string>>> result;
            for (auto [key, value] : m) result.push_back({value, key});

            lhs = result;
        }
        
        return lhs;
    }
    
    vector<pair<int, vector<string>>> term(string& s, int& i) {
        auto lhs = factor(s, i);
        while (i < s.size() && s[i] == '*') {
            ++i; 
            auto rhs = factor(s, i);
            
            map<vector<string>, int> m;
            for (auto& a : lhs) {
                for (auto& b : rhs) {
                    vector<string> algebra = a.second;
                    for (string& str : b.second) algebra.push_back(str);
                    sort(algebra.begin(), algebra.end());
                    
                    m[algebra] += a.first * b.first;
                }
            }
            
            vector<pair<int, vector<string>>> result;
            for (auto [key, value] : m) result.push_back({value, key});
            
            lhs = result;
        }
        return lhs;
    }
    
    vector<pair<int, vector<string>>> factor(string& s, int& i) { 
        if (s[i] == '(') { 
            ++i; 
            auto expression = exp(s, i);
            i++; 
            return expression;
        }
        
        if (isdigit(s[i])) { 
            int digit = 0;
            while (isdigit(s[i])) digit = (digit * 10) + (s[i++] - '0');
            return {{digit, {}}};
        }
        
        string variable = ""; 
        while (islower(s[i])) variable += s[i++];
        
        if (scope.find(variable) == scope.end()) { 
            return {{1, {variable}}};
        }
        return {{scope[variable], {}}};
    }
};