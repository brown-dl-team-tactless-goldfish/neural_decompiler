class Solution {
public:
    int getMaxRepetitions(string s1, int n1, string s2, int n2) {
        if (n1 == 0 || n2 == 0) return 0;
        int res = 0, turn = 0;
        int i = 0, j = 0;
        while (turn < n1) {
        	while (i < s1.size() && s2[j] != s1[i]) ++i;
        	if (i == s1.size()) {
        		if (++turn == n1 || j == 0) break;
        		i = 0;
        	} else {
        		++i;
        		if (++j == s2.size()) {
        		    ++res;
        		    j = 0;
        	    }
        	}
        }
        return res * (n1 / turn) / n2;
    }
};