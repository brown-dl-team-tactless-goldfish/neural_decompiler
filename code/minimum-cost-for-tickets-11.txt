class Solution {
private:
    unordered_map<int,int>memo;
public:
    int helper(vector<int>& days, vector<int>& costs,int dayIndex)
    {
        if(memo[dayIndex])
        {
            return memo[dayIndex];
        }
        if(dayIndex>=days.size())
        {
            return 0;
        }
        
        int costDay=helper(days,costs,dayIndex+1)+costs[0];
            
        int start=days[dayIndex];
        int i=dayIndex;
        for(i; i<days.size() and days[i]<start+7;i++);
        
        int costWeek=helper(days,costs,i)+costs[1];
        
        i=dayIndex;
        for(i; i<days.size() and days[i]<start+30;i++);  
        int costMonth=helper(days,costs,i)+costs[2];
        
        memo[dayIndex]= min({costDay,costWeek,costMonth});
        return memo[dayIndex];
    }
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        return helper(days,costs,0);
    }
};