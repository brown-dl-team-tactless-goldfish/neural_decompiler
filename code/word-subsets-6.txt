public class Solution {
    public IList<string> WordSubsets(string[] A, string[] B) {
        if (A == null || A.Length == 0 || B == null || B.Length == 0)
            return new List<string>();
        
        IList<string> res = new List<string>();
        int[] arrB = new int[26];
        
        foreach (var str in B)
        {
            int[] temp = new int[26];
            
            foreach (var c in str)
                temp[c - 'a'] += 1;
                
            for (int i = 0; i < 26; i++)
                if (arrB[i] < temp[i])
                    arrB[i] = temp[i];
        }
        
        foreach (var str in A)
        {
            int[] temp = new int[26];
            bool mismatch = false;
            
            foreach (var c in str)
                temp[c - 'a'] += 1;
            
            for (int i = 0; i < 26; i++)
                if (temp[i] < arrB[i])
                {
                    mismatch = true;
                    break;
                }
            
            if (!mismatch)
                res.Add(str);
        }
        
        return res;
    }
}