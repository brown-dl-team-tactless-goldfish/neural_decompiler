class Solution
{
public:
    string lcs(string &s1, string &s2)
    {
        int n1 = s1.length();
        int n2 = s2.length();
        vector<vector<string>> dp(n1 + 1, vector<string>(n2 + 1, ""));
        for (int i = 0; i < n1; i++)
        {
            for (int j = 0; j < n2; j++)
            {
                if (s1[i] == s2[j])
                    dp[i + 1][j + 1] = dp[i][j] + s1[i];
                else
                    dp[i + 1][j + 1] = (dp[i + 1][j].length() > dp[i][j + 1].length()) ? dp[i + 1][j] : dp[i][j + 1];
            }
        }
        return dp[n1][n2];
    }
    string shortestCommonSupersequence(string str1, string str2)
    {
        string k = lcs(str1, str2);
        string ans = "";
        int i = 0, j = 0;
        for (char c : k)
        {
            while (str1[i] != c) // add all non-common characters of str1
                ans += str1[i++];
            while (str2[j] != c) // add all non-common characters of str2
                ans += str2[j++];
            ans += c; // add the common character
            i++;
            j++;
        }
        return ans + str1.substr(i) + str2.substr(j);
    }
};