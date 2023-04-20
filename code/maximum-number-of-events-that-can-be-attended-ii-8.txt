class Solution {
public:
    
    // state - index, left
    // transition
    // 1. skip the current interval
    // 2. choose the current interval, now go to next valid interval i.e whose start>current end
    // Time ans Spce - O(n*k) where n is the size of events and k is the number of events allowed to take
    
    vector<vector<int>> events;
    int n;
    vector<vector<int>> dp;
    
    int rec(int level,int left){
        if(left == 0){
            return 0;
        }
        if(level == n){
            return 0;
        }
        if(dp[level][left] != -1) return dp[level][left];
        
        int ans = rec(level+1,left);
        
        // transition using binary search
        vector<int> temp = {events[level][1]+1,0,0};
        int validIdx = lower_bound(events.begin(),events.end(),temp)-events.begin();
        
        // naive transition
        // int validIdx = level;
        // while(validIdx<n && events[validIdx][0]<=events[level][1]) validIdx++;
        
        ans = max(ans,events[level][2]+rec(validIdx,left-1));
        return dp[level][left] = ans;
    }
    
    int maxValue(vector<vector<int>>& _events, int k) {
        events = _events;
        n = events.size();
        sort(events.begin(),events.end());
        dp.assign(n,vector<int>(k+1,-1));
        return rec(0,k);
    }
};