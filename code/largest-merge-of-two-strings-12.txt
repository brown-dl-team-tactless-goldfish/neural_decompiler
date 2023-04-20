class Solution {
public:
    string largestMerge(string word1, string word2) {
        int s1 = word1.size(), s2 = word2.size();
        if (s1 == 0) {return word2;}
        if (s2 == 0) {return word1;}
        
        int i = 0, j = 0;
        string ans;
        while (i < s1 && j < s2) {
            if (word1[i] < word2[j]) {
                ans += word2[j];
                j++;
            }
            else if (word1[i] > word2[j]) {
                ans += word1[i];
                i++;
            }
            else {
                int ii = i, jj = j;
                while (ii < s1 && jj < s2 && word1[ii] == word2[jj]) {
                    ii++; jj++;
                }
                if (ii == s1) {ans += word2[j++];}
                else if (jj == s2) {ans += word1[i++];}
                else if (word1[ii] > word2[jj]) {ans += word1[i++];}
                else if (word1[ii] < word2[jj]) {ans += word2[j++];}
            }
        }
        while (i < s1) {ans += word1[i++];}
        while (j < s2) {ans += word2[j++];}
        return ans;
    }
};