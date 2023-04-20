public class Solution {
    private List<int>[] g = null;
    private int[] informTime = null;
    
    public int NumOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        g = new List<int>[n];
        this.informTime = informTime;
        
        for (int i = 0; i < n; i++)
            if (manager[i] != -1)
            {
                if (g[manager[i]] == null)
                    g[manager[i]] = new List<int>();
                    
                g[manager[i]].Add(i);
            }
        
        return DFS(headID, 0);
    }
    
    private int DFS(int emp, int time)
    {
        int cur = 0;
        
        if (g[emp] != null)
            foreach (var sub in g[emp])
                cur = Math.Max(cur, DFS(sub, informTime[emp]));
        
        return cur + time;
    }
}