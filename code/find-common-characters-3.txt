class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        vector<string> res;
        vector<vector<int>> temp;
        int i,j;
        for(i=0;i<A.size();i++) {
            vector<int> level (26,0);
            for(j=0;j<A[i].size();j++) {
                level[A[i][j]-'a']++;
            }
            temp.push_back(level);
        }
        for(i=0;i<26;i++) {
            int min = INT_MAX;
            
            for(j=0;j<temp.size();j++) {
                 
                if(temp[j][i] < min) min = temp[j][i];
            }
            while(min) {
                string p;
               p+= i+'a';
                res.push_back(p);
                min--;
            } 
            
        }
        return res;
    }
};