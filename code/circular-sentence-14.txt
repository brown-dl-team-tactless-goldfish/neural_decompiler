class Solution {
public:
    bool isCircularSentence(string s) 
    {
        int n = s.size();
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == ' ')
            {
			   //if there is space char at "i" => s[i - 1] will be last char of prevWord, s[i + 1] will be first char fo nextWord
                if (s[i - 1] != s[i + 1]) return false;
            }
        }
        return (s[0] == s[n - 1]);
    }
};