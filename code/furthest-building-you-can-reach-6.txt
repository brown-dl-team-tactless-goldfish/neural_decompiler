public class Solution
{
    public int FurthestBuilding(int[] heights, int bricks, int ladders)
    {
        int sum = 0;
        var pq = new SortedSet<(int Height,int Index)>();
        for(int i = 1; i < heights.Length; i++)
        {
            if(heights[i] <= heights[i-1]) continue;
            pq.Add((heights[i] - heights[i-1],i));
            if(pq.Count > ladders)
            {
                sum += pq.Min.Height;
                pq.Remove(pq.Min);
            }
            if(sum > bricks)
                return i - 1;
        }

        return heights.Length - 1;
    }
}