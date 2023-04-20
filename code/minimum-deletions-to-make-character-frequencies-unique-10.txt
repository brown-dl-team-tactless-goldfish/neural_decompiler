public class Solution {
    public int MinDeletions(string s) {
        
        if(s == null || s.Length == 0)
            return 0;
        
        // record unique frquencies 
        HashSet<int> freqSet = new HashSet<int>();
        int res = 0;
        
        // calculate frequencies
        int[] freq = new int[26];
        foreach(var c in s)
            freq[c - 'a']++;
        
        for(int i = 0; i < freq.Length; i++)
        {
            // if there is another character has the same frequence
            // we need to keep delete the current character until its frequncey is unique
            // example 1: input is {(a,3), {b,3}, {c,2}}
            // then we need to delete 2 a or 2 b
            // example 2: input is {(a,3), {b,3}, {c,2},{d,2}}
            // then we need to delete 2 a or 2 b, then delete 2 c or 2d
            while(freqSet.Contains(freq[i]) && freq[i] > 0)
            {
                freq[i]--;
                res++;
            }
            freqSet.Add(freq[i]);
        }
        
        return res;
    }
}