class Solution {
public:
    int countPyramids(vector<vector<int>>& grid) {
        int n=grid.size();
        int m=grid[0].size();
        vector<vector<int>> pre(n,vector<int>(m));
        // Calculating Prefix Sum
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(j==0)
                {
                    pre[i][j]=grid[i][j];
                }
                else
                {
                    pre[i][j]=pre[i][j-1]+grid[i][j];
                }
            }
        }
        //Checking for pyramids
        int ans=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j])
                {
                    int c=1;
                    int r,c1,c2;
                    r=i;
                    c1=j;
                    c2=j;
                    while(r<n&&c1>=0&&c2<m)
                    {
                        int count;
                        if(c1<1)
                        count=pre[r][c2];
                        else
                        count=pre[r][c2]-pre[r][c1-1];
                        if(count==c)
                        {
                            if(c>1)
                            ans++;
                        }
                        else
                        break;
                        c+=2;
                        r++;
                        c1--;
                        c2++;
                    }
                }
            }
        }
        
        //Checking for inverted Pyramids
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j])
                {
                    int c=1;
                    int r,c1,c2;
                    r=i;
                    c1=j;
                    c2=j;
                    while(r>=0&&c1>=0&&c2<m)
                    {
                        int count;
                        if(c1<1)
                        count=pre[r][c2];
                        else
                        count=pre[r][c2]-pre[r][c1-1];
                        if(count==c)
                        {
                            if(c>1)
                            ans++;
                        }
                        else
                        break;
                        c+=2;
                        r--;
                        c1--;
                        c2++;
                    }
                }
            }
        }
    return ans;
    }
};