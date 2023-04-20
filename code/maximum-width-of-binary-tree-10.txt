public class Solution {
    public int WidthOfBinaryTree(TreeNode root) {
        int res = 0;
        Queue<(TreeNode, int)> q = new Queue<(TreeNode, int)>();
        
        q.Enqueue((root, 1));
        
        while (q.Count > 0)
        {
            int cnt = q.Count,
                s = q.Peek().Item2,
                e = 0;
            
            while (cnt > 0)
            {
                (TreeNode, int) cur = q.Dequeue();
                
                if (cnt == 1)
                {
                    e = cur.Item2;
                }
                
                if (cur.Item1.left != null)
                {
                    q.Enqueue((cur.Item1.left, cur.Item2 * 2));
                }
                
                if (cur.Item1.right != null)
                {
                    q.Enqueue((cur.Item1.right, cur.Item2 * 2 + 1));
                }
                
                cnt--;
            }
            
            res = Math.Max(res, e - s + 1);
        }
        
        return res;
    }
}