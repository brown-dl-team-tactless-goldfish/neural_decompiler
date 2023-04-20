public class Solution 
{
    public int MaxJump(int[] stones) 
    {
        if (stones.Length == 2)
            return stones[1] - stones[0];
        int max = int.MinValue;
        for (int i = 0; i < stones.Length - 2; i++)
        {
            max = Math.Max(max, stones[i + 2] - stones[i]);
        }
        return max;
    }
}