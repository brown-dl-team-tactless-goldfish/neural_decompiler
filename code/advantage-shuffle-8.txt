public class Solution 
{
    public int[] AdvantageCount(int[] A, int[] B) 
    {
        List<int> result = new List<int>(), list = new List<int>(A);
        list.Sort();
        for(int i = 0; i < B.Length; i++)
        {
            var index = list.BinarySearch(B[i] + 1);
            if(index < 0) index = ~index;
            if(index == list.Count) index = 0;
            result.Add(list[index]);
            list.RemoveAt(index);
        }
        return result.ToArray();
    }
}