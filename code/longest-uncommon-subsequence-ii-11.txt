class Solution {
public:
    bool check(string a,string b){
        int A = a.size();
        int B = b.size();
        while(A > 0 && B > 0)
        {
            int i = a.size() - A ;
            int j = b.size() - B ;
            if(a[i] == b[j])
            {
                A-- ;
            }
            B-- ;
        }
        return A==0;
    }
    int findLUSlength(vector<string>& strs) {
        int maxLen = -1 ;
        for(int i = 0 ; i < strs.size() ; ++i)
        {
            int currLen = strs[i].length() ;
            bool flag = true ;
            for(int j = 0 ; j < strs.size() ; ++j)
            {
                if(i != j && check(strs[i], strs[j]))
                {
                    flag = false ;
                    break ;
                }
            }
            if(flag)
            {
                maxLen = max(maxLen , currLen);
            }
        }
        return maxLen;
    }
};