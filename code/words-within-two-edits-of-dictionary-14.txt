class Solution {
private:
    int fun(string &a, string &b){
        int k = 0;
        for(int i=0; i<a.size(); i++){
            if(a[i]!=b[i])  k++;
        }
        return k;
    }
public:
    vector<string> twoEditWords(vector<string>& q, vector<string>& d) {
        int n = q.size(), m = d.size();
        vector<string> ans;
        for(int i=0; i<n; i++){
            string a = q[i];
            for(int j=0; j<m; j++){
                string b = d[j];
                int check = fun(a, b);
                if(check<=2){
                    ans.push_back(a);
                    break;
                }
            }
        }
        return ans;
    }
};