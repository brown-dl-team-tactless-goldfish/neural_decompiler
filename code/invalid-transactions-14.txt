class Solution {
public:
    vector<string> invalidTransactions(vector<string>& t) {
        
        vector<string>name,city,res;
        vector<int>time,amt;
        
        for(int i=0;i<t.size();i++)
        {
            vector<string>x;
            
            string temp="";
            for(int j=0;j<t[i].size();j++)
            {
                if(t[i][j]!=',')
                     temp+=t[i][j];
                else
                 {
                    x.push_back(temp);
                    temp="";
                }
            }
             x.push_back(temp);
            
            name.push_back(x[0]);
            city.push_back(x[3]);
            time.push_back(stoi(x[1]));
            amt.push_back(stoi(x[2]));
        }
        
        unordered_set<int>ans;
        
        for(int i=0;i<t.size();i++)
        {
            
       
            if(amt[i]>1000)
                 ans.insert(i);
            for(int j=0;j<t.size();j++)
            {
                if(i!=j&&abs(time[i]-time[j])<=60&&city[i]!=city[j]&&name[i]==name[j])
                {
                    ans.insert(i);
                    ans.insert(j);
                }
            }
        }
        
        
        for(auto x:ans)
            res.push_back(t[x]);
        
        return res;
    }
};