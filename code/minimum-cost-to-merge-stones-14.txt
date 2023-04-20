class Solution {
public:
    int F[31][31][31],prefix[31];
    int memoization(int x,int y,int z,vector<int> & stones, int k)
    {
        int mi=1e9,a,b,f1,f2;
        if(y-x+1==z) return 0;
        if(y-x+1==k&&z==1)
        {
            if(x==0) a=prefix[y];
            else a=prefix[y]-prefix[x-1];
            return a;
        }
        if(y-x+1<z) return -1;
        if(F[x][y][z]!=0) return F[x][y][z];
        if(z==1)
        {
            for(int i=x;i<=y-1;i++)
            {
                if(x==0) a=prefix[i];
                else a=prefix[i]-prefix[x-1];
                b=prefix[y]-prefix[i];
                for(int j=1;j<=k-1;j++)
                {
                    f1=memoization(x,i,j,stones,k);
                    f2=memoization(i+1,y,k-j,stones,k);
                    if(f1==-1||f2==-1) continue;
                    mi=min(mi,a+b+f1+f2);
                }
            }
        }
        else
        {
            for(int i=x;i<=y-1;i++)
            {
                for(int j=1;j<=z-1;j++)
                {
                    f1=memoization(x,i,j,stones,k);
                    f2=memoization(i+1,y,z-j,stones,k);
                    if(f1==-1||f2==-1) continue;
                    mi=min(mi,f1+f2);
                }
            }
        }
        if(mi==1e9) mi=-1;
        return F[x][y][z]=mi;
    }
    int mergeStones(vector<int>& stones, int k) {
        if(stones.size()==1) return 0;
        if(stones.size()<k||(stones.size()-k)%(k-1)!=0) return -1;
        prefix[0]=stones[0];
        for(int i=1;i<=stones.size()-1;i++)
            prefix[i]=prefix[i-1]+stones[i];
        return memoization(0,stones.size()-1,1,stones,k);
    }
};