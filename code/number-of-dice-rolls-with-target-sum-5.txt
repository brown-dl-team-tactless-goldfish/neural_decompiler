public class Solution 
{
    public int NumRollsToTarget(int d, int f, int target) 
    {
        var dp = new int[target + 1];
        dp[0] = 1;
        for (int i = 1; i <= d; i++) 
        {
            var tempdp = new int[target + 1];
            for (var j = 1; j <= f; j++)
                for (var k = j; k <= target; k++)
                    tempdp[k] = (tempdp[k] + dp[k - j]) % 1_000_000_007;
            dp = tempdp;
        }
        
        return dp[target];
    }
}