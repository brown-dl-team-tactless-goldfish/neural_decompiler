public class Solution 
{
    public int ProfitableSchemes(int G, int P, int[] group, int[] profit) 
    {
        int r = G, c = P, result = 0, mod = 1_000_000_007;
        var dp = new int[r + 1, c + 1];
        dp[0, 0] = 1;
        for(int k = 0; k < profit.Length; k++)
        {
            var dpTemp = (int[,]) dp.Clone();
            for(int i = 0; i <= r; i++)
            {
                for(int j = 0; j <= c; j++)
                {
                    int ni = i + group[k], nj = Math.Min(j + profit[k], P);
                    if(ni <= r)
                        dpTemp[ni, nj] =  (dpTemp[ni, nj] + dp[i, j]) % mod;
                }
            }
            
            dp = dpTemp;
        }
        
        for(int i = 0; i <= r; i++)
                result = (result + dp[i, P]) % mod;
        
        return result;
    }
}