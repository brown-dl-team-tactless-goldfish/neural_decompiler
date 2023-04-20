public class Solution {
    public bool CanTransform(string start, string end) {
        var sb = new StringBuilder();
        
        foreach(var c in start){
            if(c == 'X') continue;
            sb.Append(c);
        }
        var s = sb.ToString();
        
        sb.Clear();
        foreach(var c in end){
            if(c =='X') continue;
            sb.Append(c);
        }
        var e = sb.ToString();
        
        if(s != e) return false;
        
        var j = 0;
        for(var i = 0; i < start.Length; ++i){
            if(start[i] == 'X') continue;
            while(end[j] == 'X')
                j++;    
            if(start[i] == 'L' && i < j)
                return false;
            
            if(start[i] == 'R' && i > j)
                return false;
            j++;
        }
        return true;
    }
}