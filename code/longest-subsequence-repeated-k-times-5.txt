class Solution {
public:
    int count_oc(string sub, string s){ //pointers approach
        if(sub.length() == 0) return s.length(); //dummy case when sub = ""
        int ind = 0;  //current pointer in sub
        int cntr = 0; //number of times it appears as substring
        for(int i = 0; i < s.length(); i++) {
            if(sub[ind] == s[i]){ //if it matches, then increment our index
                ind++; 
                if(ind == (int)sub.length()) ind = 0, cntr++; //reset our pointer
            } 
        }
        return cntr;
    }
    string best; //best string we've seen so far
    void rec(string sub, string s, int k) {
        if(count_oc(sub, s) < k) return; //if it doesn't work, appending something still won't make it work
        if(sub.length() >= best.length() && sub > best) best = sub; //we've found something better!
        for(char c = 'a'; c <= 'z'; c++) rec(sub + c, s, k); //we can try appending and seeing if it works
    }
    string longestSubsequenceRepeatedK(string s, int k) {
        rec("", s, k);
        return best;
    }
};