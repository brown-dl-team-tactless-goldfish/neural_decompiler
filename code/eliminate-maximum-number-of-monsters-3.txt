class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        vector<double> time;
        int n = dist.size();
        for(int i = 0; i < n; i++)
        {
            time.push_back((double)dist[i]/speed[i]);
        }
        sort(time.begin(), time.end());
        int currtime = 0, ans = 0;
        for(int i = 0; i < n; i++)
        {
            if(currtime < time[i])
            {
                ans++;
                currtime++;
            }
            else
                break;
        }
        return ans;
    }
};