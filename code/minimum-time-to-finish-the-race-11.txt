class Solution {
    int best[1001];
private:
    int recur(int n,int changeTime,int maxLaps,vector<int>&dp)
    {
        if(n==0)
            return -changeTime;
        
        if(dp[n]!=-1)
            return dp[n];
        long long int mini=INT_MAX;
        for(int laps=1;laps<=min(n,maxLaps);laps++)
        {
           long long  time=best[laps]+changeTime+recur(n-laps,changeTime,maxLaps,dp);
            mini=min(mini,time);
        }
        return dp[n]= mini;
    }
public:
    int minimumFinishTime(vector<vector<int>>& tires, int changeTime, int numLaps) {
        
        int i,j;
        for(i=0;i<=1000;i++)
            best[i]=INT_MAX;
        vector<int>dp(numLaps+100,-1);
        
        int maxLaps=0;
        for(auto i:tires)
        {
            int fi=i[0];
            int ri=i[1];
            int time=fi;
            long long int currLapTime=time;
           
            for(int lap=1;lap<=numLaps and currLapTime<changeTime+fi;lap++)
            {
                if(time<best[lap])
                    best[lap]=time;
                currLapTime*=ri;
                
                time+=currLapTime;
                
                maxLaps=max(maxLaps,lap);
                
            }
           
            
        }
        // for(j=1;j<=2;j++)
        //     cout<<best[j]<<" ";
        
        return recur(numLaps,changeTime,maxLaps,dp);
        
        
    }
};