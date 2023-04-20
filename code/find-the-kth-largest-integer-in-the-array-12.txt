using System.Collections.Generic;
using System.Numerics;

public class Solution
{
    public string KthLargestNumber(string[] nums, int k)
    {
        var queue = new PriorityQueue<string, BigInteger>();        
        
        for (int i = 0; i < nums.Length; i++)
        {
            queue.Enqueue(nums[i], BigInteger.Parse(nums[i]));

            if (queue.Count > k)
            {
                queue.Dequeue();
            }
        }

        return queue.Peek();
    }
}