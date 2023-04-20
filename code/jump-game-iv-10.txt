class Solution {
public:
    unordered_set<int>vis;
    unordered_map<int,vector<int>>mp;
    int minJumps(vector<int>& arr) 
    {
        //preprocessing
        for(int i=0;i<arr.size();i++)
        {
            mp[arr[i]].push_back(i);
        }

        queue<int>q;
        q.push(0);

        int steps=0;

        while(!q.empty())
        {
            int size=q.size();

            for(int j=0;j<size;j++)
            {
               int i = q.front();
               q.pop();

               vis.insert(i);

               if(i==arr.size()-1)
               {
                  return steps;
               }

                //i+1
               if((i+1)<arr.size() and vis.find(i+1)==vis.end())
               {
                  q.push(i+1);
                  vis.insert(i+1);
               }
               if((i-1)>=0 and vis.find(i-1)==vis.end())
               {
                  q.push(i-1);	
                  vis.insert(i-1);
               }	
               if(mp[arr[i]].size()>0)
               {
                  for(auto pos : mp[arr[i]])
                  {
                     if(vis.find(pos)==vis.end())
                     q.push(pos);
                  }  
                  mp[arr[i]].clear();
               }
               
            }
            steps++;
        }
        return steps;
    }
};