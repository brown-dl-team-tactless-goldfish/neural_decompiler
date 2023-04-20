class Solution {
public:
    const long long inf = 1e15;
    long long solve(int i,int j,vector<int>& robots, vector<vector<int>>& F,vector<vector<long long>> &dp)
    {
        if(i == robots.size())
        {
            return 0;
        }
        if(j == F.size())
        {
            return 1000000000000;
        }

        if(dp[i][j] != inf) return dp[i][j];

        long long ans = 1000000000000;

        long long d = 0;

        int k = i;

        for(int taken = 1;taken <= F[j][1];taken++)
        {
            
            d += labs(robots[k] - F[j][0]);

            ans = min(ans, d + solve(k+1,j+1,robots,F,dp));
            k++;
            
            if(k == robots.size()) break;
        }
        
        // Not taking current factory
        ans = min(ans,solve(i,j+1,robots,F,dp));
        


        return dp[i][j] = ans;
    }
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        
        vector<vector<long long>> dp(robot.size(),vector<long long>(factory.size(), inf));
      
        sort(factory.begin(),factory.end());

        sort(robot.begin(),robot.end());



        return solve(0,0,robot,factory,dp);


    }
};