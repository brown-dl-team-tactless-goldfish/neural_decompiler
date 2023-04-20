class Solution {
public:
  string predictPartyVictory(string s) {
    char p;
    int c = 0;
      
    while(true){
      string t = ""; 
      
      for(auto ch: s)
        if(c == 0) p = ch, c++, t.push_back(ch);
        else if(ch == p) c++, t.push_back(ch);
             else c--;
     
      s.clear();
      int i = 0;
      while(i != t.size() && c)
        if(t[i++] == p) s.push_back(p);
        else c--;
      
      if(c > 0) return p == 'R' ? "Radiant" : "Dire";
      s += t.substr(i, t.size());
    }   
    
    return "";
  }
};