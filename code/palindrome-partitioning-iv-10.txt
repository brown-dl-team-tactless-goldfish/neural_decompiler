class Solution {
private:
    vector<vector<int>>mem;
    vector<vector<int>>palindrome;
    bool isPalindrome(string& s, int i, int j) {
		if (i >= j){
            return true;
        } else if (palindrome[i][j] != -1) {
            return palindrome[i][j];
        } else if (s[i] == s[j]) {
            return palindrome[i][j] = isPalindrome(s, i + 1, j - 1);
        } else {
            return palindrome[i][j] = false;
        }
	}
    bool solve(string &s,int i,int k){
        if(i>=s.size()){
            if(k==0){
                return true;
            } else {
                return false;
            }
        } else if(mem[i][k]!=-1){
            return mem[i][k];
        } else if(k==1){
            return mem[i][k]=isPalindrome(s,i,s.size()-1);
        } else if(k==0){
            return false;
        } else {
            for(int it=i;it<s.size();it++){
                if(s[it]==s[i] and isPalindrome(s,i,it)){
                    if(solve(s,it+1,k-1)){
                        return mem[i][k]=true;
                    }
                }
            }
            return mem[i][k]=false;        
        }
    }
public:
    bool checkPartitioning(string &s) {
        mem=vector<vector<int>>(s.size(),vector<int>(4,-1));
        palindrome=vector<vector<int>>(s.size(),vector<int>(s.size(),-1));
        return solve(s,0,3);
    }
};