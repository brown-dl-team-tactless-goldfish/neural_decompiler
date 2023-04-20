public class Solution {
    public char SlowestKey(int[] releaseTimes, string keysPressed) {
        if (releaseTimes == null || releaseTimes.Length == 0 || keysPressed == null || keysPressed == string.Empty)
            return '\0';
        
        char res = keysPressed[0];
        int max = releaseTimes[0];
        
        for (int i = 1; i < releaseTimes.Length; i++)
            if (releaseTimes[i] - releaseTimes[i - 1] > max || (releaseTimes[i] - releaseTimes[i - 1] == max && keysPressed[i] > res))
            {
                res = keysPressed[i];
                max = releaseTimes[i] - releaseTimes[i - 1];
            }
        
        return res;
    }
}