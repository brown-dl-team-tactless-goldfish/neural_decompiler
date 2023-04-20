class Solution {
public:
    vector<int>prefix;
    vector<vector<vector<int>>>dp;
    int stoneGameII(vector<int>& piles) 
    {   
        dp.resize(piles.size(),vector<vector<int>>(3,vector<int>(202,-1)));
        
        for(int i=0;i<piles.size();i++)
        {
            if(prefix.size()==0)
            {
               prefix.push_back(piles[i]);
            }
            else
            {
                prefix.push_back(piles[i]+prefix[prefix.size()-1]);
            }
        }
        
        int idx=0;
        int turn=1;     //for keeping the track of the player bw the alice and bob alice->1 bob->2
        int m=1;
        
        return fun(piles,idx,turn,m);
    }
    int fun(vector<int>&piles,int idx,int turn,int m)
    {
       
        if(idx>=piles.size())
        {
            return 0;
        }
        if(dp[idx][turn][m]!=-1)
        {
            return dp[idx][turn][m];
        }
        //if the alice has the turn 
        if(turn==1)
        {
            int ans=INT_MIN;
            int sum=0;
            
            for(int i=0;i<(2*m);i++)
            {
                if(idx+i<(piles.size()))
                {
                    sum=sum+piles[idx+i];
                    
                    int totalsum=prefix[prefix.size()-1]-prefix[idx+i];
                    int x=fun(piles,idx+i+1,2,max(m,i+1));   //this will give the ans of the max bob       
                     
                    ans=max(ans,sum+(totalsum-x));
                }
            }
            return dp[idx][turn][m]=ans;
        }
        else if(turn==2)   //if the bob has the turn
        {
           int ans=INT_MIN;
           int sum=0;
           
            for(int i=0;i<(2*m) ;i++)
            {
                if(idx+i<(piles.size()))
                {
                    sum=sum+piles[idx+i];
                    
                    int totalsum=prefix[prefix.size()-1]-prefix[idx+i];
                    int x=fun(piles,idx+i+1,1,max(m,i+1));   //this will give the ans of the max bob       
                    
                    ans=max(ans,sum+(totalsum-x));
                }
            }
            return dp[idx][turn][m]=ans;
        }
        return -1;
    }
};