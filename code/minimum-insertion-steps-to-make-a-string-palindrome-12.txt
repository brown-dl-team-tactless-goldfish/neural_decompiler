public class Solution
{
    public int MinInsertions(string s)
    {
        if(string.IsNullOrEmpty(s)) return 0;
        int n = s.Length;
        var memo = new int[n, n];
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                memo[i, j] = -1;
        return MinInsertions(s, 0, s.Length - 1, memo);
    }
    
    public int MinInsertions(string s, int start, int end, int[,] memo)
    {
        if(start >= end) return 0;
        if(memo[start, end] != -1) return memo[start, end];
        
        if(s[start] == s[end])
            memo[start, end] = MinInsertions(s, start + 1, end - 1, memo);
        else
            memo[start, end] = 1 + Math.Min(MinInsertions(s, start + 1, end, memo), 
                               MinInsertions(s, start, end - 1, memo));
        return memo[start, end];
    }
}