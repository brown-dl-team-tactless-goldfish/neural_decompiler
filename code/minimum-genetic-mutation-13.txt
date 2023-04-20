public class Solution {
    public int MinMutation(string start, string end, string[] bank) {
        Queue<string> q = new ();
        HashSet<string> used = new ();

        q.Enqueue(start);
        used.Add(start);
        
        int t = 0;
        bool reachedEnd = false;
        while (q.Count > 0 && !reachedEnd) {
            int iterationCount = q.Count;
            
            for (int i = 0; i < iterationCount && !reachedEnd; i++) {
                string c = q.Dequeue();
                
                for (int j = 0; j < bank.Length && !reachedEnd; j++) {
                    if (used.Contains(bank[j])) continue;
                    
                    int diffs = 0;
                    for (int k = 0; k < 8 && diffs <= 1; k++) {
                        if (c[k] != bank[j][k]) diffs++;
                    }
                    
                    if (diffs == 1) {
                        if (bank[j] == end) reachedEnd = true;
                        else {
                            q.Enqueue(bank[j]);
                            used.Add(bank[j]);
                        }
                    }
                }
            }
            
            t++;
        }
        
        if (!reachedEnd) return -1;
        return t;
    }
}