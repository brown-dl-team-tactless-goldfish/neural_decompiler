class Solution {
public:
    int longestDecomposition(string text) {
        if (text=="") return 0;
        int len;
        for (int i=text.length()-1; i>(text.length()-1)/2; i--){
            len = text.length()-i;
            if (check(text, i)){
                return 2 + longestDecomposition(text.substr(len, text.length()-2*len));
            } 
        }
        return 1;
    }
    
    bool check(string text, int s){
        for (int i=s; i<text.length(); i++){
            if (text[i]!=text[i-s]) return false;
        }
        return true;
    }
};