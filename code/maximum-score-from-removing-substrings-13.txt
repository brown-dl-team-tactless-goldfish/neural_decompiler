class Solution {
public:
    string solve(string& str,string pat,int points,int& total_points)
    {
        stack<char>S;
        for(char a : str)
        {
            if(S.empty())
                S.push(a);
            else
            {
                if(S.top() == pat[0] and a == pat[1])
                {
                    total_points += points;
                    S.pop();
                }
                else
                    S.push(a);
            }
        }
        string remaining_str = "";
        while(!S.empty())
        {
            remaining_str += S.top();
            S.pop();
        }
        reverse(remaining_str.begin(),remaining_str.end());
        return remaining_str;
            
            
    }
    int maximumGain(string s, int x, int y) {
        
        int total_points1 = 0;
        int total_points2 = 0;
        if(x > y)
        {
            string s1 = solve(s,"ab",x,total_points1);
            s1 = solve(s1,"ba",y,total_points1);
        }
        else
        {
            s = solve(s,"ba",y,total_points2);
            s = solve(s,"ab",x,total_points2);
        }
        
        return max(total_points1,total_points2);
        
        
    }
};