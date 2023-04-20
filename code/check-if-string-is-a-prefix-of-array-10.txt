class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) 
    {
       int sidx=0;
       for(int i=0;i<words.size();i++)
       {
          string currstr = words[i];
          int temp=0;

          while(sidx<s.length() and temp<currstr.length())
          {
              if(s[sidx]!=currstr[temp])
              {
                return false;
              }
              sidx++;
              temp++; 	
          }	
          if(sidx>=s.length() and temp>=currstr.length())
          return true;
          else if(sidx>=s.length() and temp<currstr.length())
          return false;
       }
       if(sidx >= s.length())
       return true;
        
       return false;
        
    }
};