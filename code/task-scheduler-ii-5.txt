class Solution {
public:
    long long taskSchedulerII(vector<int>& tasks, int space) {
        long long n = tasks.size(), day = 0;
        unordered_map<int, long long> um;
        for(int i = 0; i < n; i++)
        {
            if(!um.count(tasks[i]))
                um[tasks[i]] = day + space + 1;
            else
            {
                if(um[tasks[i]] > day)
                {
                    day = um[tasks[i]];   
                }
                um[tasks[i]] = day + space + 1;
            }
            day++;
        }
        return day;
    }
};