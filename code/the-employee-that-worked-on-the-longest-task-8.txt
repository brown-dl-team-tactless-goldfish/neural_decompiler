class Solution 
{
public:
    int hardestWorker(int n, vector<vector<int>>& logs) 
    {
        int id=INT_MAX, maxi=INT_MIN, last=0;
        
        for(int i=0; i<logs.size(); i++)
        {
            if((logs[i][1] - last) > maxi || ((logs[i][1] - last)==maxi && id > logs[i][0]))
            {
                maxi = (logs[i][1] - last);
                id = logs[i][0];
            } 
            last = logs[i][1];
        }
        return id;
    }
};