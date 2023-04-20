public class Solution {
    public bool IsRobotBounded(string instructions) {
        
        if(instructions == null || instructions.Length == 0)
            return true;
        
        int[,] dirs = new int[,]{{0,1}, {1,0}, {0,-1}, {-1,0}}; // north, east, sourth, west
        int i = 0, x = 0, y = 0;
        foreach(var c in instructions)
        {
            if(c == 'G')
            {
                x += dirs[i,0];
                y += dirs[i,1];
            }
            else if(c == 'L')
                i = (i + 3) % 4; // (i - 1 + 4) % 4, % is the remainder operator, -1 % 4 = -1
            else
                i = (i + 1) % 4;
        }
        
        return (x == 0 && y == 0) || i != 0;
    }
}