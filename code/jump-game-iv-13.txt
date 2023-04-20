class Solution {
public:
     int minJumps(vector<int>& arr) {
        unordered_map<int,vector<int>>mp;  
        for(int i=0;i<arr.size();i++)
        {
            mp[arr[i]].push_back(i);
        }
        vector<bool>vis(arr.size(),false);   
        
        int ans=INT_MAX;
        
        queue<pair<pair<int,int>,int>>q;  
        
        q.push({{arr[0],0},0});
        
        while(!q.empty())
        {
            int idx=q.front().second;
            int c=q.front().first.second;
            int ele=q.front().first.first;
            
            if(vis[idx]==false)
            {
                vis[idx]=true;
            }
            
            if(idx==arr.size()-1)
            {
                ans=min(ans,c);
            }
            
            q.pop();
            
            if(idx>0 and vis[idx-1]==false)
            {
                q.push({{arr[idx-1],c+1},idx-1});
                vis[idx-1]=true;
            }
            
            if(idx<arr.size()-1 and vis[idx+1]==false)
            {
                q.push({{arr[idx+1],c+1},idx+1});
                vis[idx+1]=true;
            }
            
            for(int j=0;j<mp[ele].size();j++)
            {
                if(mp[ele][j]!=idx and vis[mp[ele][j]]==false)
                {
                    q.push({{ele,c+1},mp[ele][j]});
                    vis[mp[ele][j]]=true;
                }
            }
            mp[ele].clear();
        }
        return ans;
    }
};