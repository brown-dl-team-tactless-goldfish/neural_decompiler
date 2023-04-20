public class Solution {
    private int res = 0;
    
    public int MaxLength(IList<string> arr) {
        if (arr == null || arr.Count == 0)
            return 0;
        
        Backtrack(arr, 0, 0, new HashSet<char>());
        
        return res;
    }
    
    private void Backtrack(IList<string> arr, int i, int curLen, HashSet<char> set)
    {
        if (i == arr.Count)
        {
            res = Math.Max(res, curLen);
            return;
        }
            
        for (int j = i; j < arr.Count; j++)
        {
            bool inPrev = false,
                 inCur = false;            
            HashSet<char> curSet = new HashSet<char>();
            
            foreach (var c in arr[j])
            {
                if (set.Contains(c))
                    inPrev = true;
                
                if (curSet.Contains(c))
                    inCur = true;
                
                curSet.Add(c);
            }
            
            if (inPrev || inCur)
            {
                if (inPrev)
                    res = Math.Max(res, curLen);
                
                continue;
            }
            
            foreach (var c in arr[j])
                set.Add(c);
            
            Backtrack(arr, j + 1, curLen + arr[j].Length, set);
            
            foreach (var c in arr[j])
                set.Remove(c);
        }
    }
}