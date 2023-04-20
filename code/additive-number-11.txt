class Solution {
public:
    
    bool helper(long long int term1, long long int term2, string s, bool found)
    {
        if(s.length() == 0 && found)  return true;
        
        string term3 = to_string(term1 + term2);
        
        long long idx = min(s.length(), term3.length());
        
        if(s.substr(0,idx) == term3)
            return helper(term2,stol(term3),s.substr(idx),true);
        return false;
    }
    
    bool isAdditiveNumber(string num)
    {
        if(num.size() <= 2) return false;
        
        for(int i = 1; i < num.length() - 1; i++)
        {
            long long int term1 = stol(num.substr(0,i));
            
            if(to_string(term1) != num.substr(0,i)) break;
            
            for(int j = i + 1; j < num.length(); j++)
            {
                long long int term2 = stol(num.substr(i,j - i));
                
                if(to_string(term2) != num.substr(i,j - i)) break; 
            
                bool found = helper(term1,term2,num.substr(j),false);
            
                if(found) return true;
            }
        }
        return false;
    }
};