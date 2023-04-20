class Solution {
public:
    long long findScore(vector<int>& nums) {
        long long ans=0;
        vector<bool> vis(nums.size(),false);
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
        for(int i=0;i<nums.size();i++){
            pq.push({nums[i],i});
        }
        while(pq.size()){
            auto x = pq.top();
            pq.pop();
            if(!vis[x.second]){
                ans += x.first;
                vis[x.second] = true;
                if(x.second>0 && !vis[x.second-1]){
                    vis[x.second-1] = true;
                }
                if(x.second+1<nums.size() && !vis[x.second+1]){
                    vis[x.second+1] = true;
                }
            }
        }
        return ans;
    }
};