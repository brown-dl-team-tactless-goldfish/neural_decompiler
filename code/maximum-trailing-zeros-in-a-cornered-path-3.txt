#define ll long long int
class Solution {
public:
    int maxTrailingZeros(vector<vector<int>>& grid) {
        int n=grid.size();
        int m=grid[0].size();
        vector<vector<pair<ll,ll>>> v(n,vector<pair<ll,ll>>(m,{0,0})),ltr,utd,rtl,dtu;
        
        for(ll i=0;i<n;i++)
        {
            for(ll j=0;j<m;j++)
            {
                ll z=grid[i][j],c1=0,c2=0;
                while(z%2==0)
                {
                    z/=2;
                    c1++;
                }
                while(z%5==0)
                {
                    z/=5;
                    c2++;
                }
                v[i][j].first=c1;
                v[i][j].second=c2;
            }
        }
        ltr=utd=rtl=dtu=v;
        for(ll i=0;i<n;i++)
        {
            for(ll j=1;j<m;j++)
            {
                ltr[i][j].first+=ltr[i][j-1].first;
                ltr[i][j].second+=ltr[i][j-1].second;
            }
        }
        for(ll i=0;i<n;i++)
        {
            for(ll j=m-2;j>=0;j--)
            {
                rtl[i][j].first+=rtl[i][j+1].first;
                rtl[i][j].second+=rtl[i][j+1].second;
            }
        }
        for(ll j=0;j<m;j++)
        {
            for(ll i=1;i<n;i++)
            {
                utd[i][j].first+=utd[i-1][j].first;
                utd[i][j].second+=utd[i-1][j].second;
            }
        }
        for(ll j=0;j<m;j++)
        {
            for(ll i=n-2;i>=0;i--)
            {
                dtu[i][j].first+=dtu[i+1][j].first;
                dtu[i][j].second+=dtu[i+1][j].second;
            }
        }
        ll ans=0;
        for(ll i=0;i<n;i++)
        {
            for(ll j=0;j<m;j++)
            {
                ll c1,c2,c3,c4;
                ll x1,x2,x3,x4;
                ll a,b;
                a=v[i][j].first;
                b=v[i][j].second;       
                
                c1=ltr[i][j].first;
                c2=rtl[i][j].first;
                
                c3=utd[i][j].first;
                c4=dtu[i][j].first;
                
                x1=ltr[i][j].second;
                x2=rtl[i][j].second;
                
                x3=utd[i][j].second;
                x4=dtu[i][j].second;
                
                ans=max(ans,min(c3+c1-a,x3+x1-b));
                ans=max(ans,min(c3+c2-a,x3+x2-b));
                ans=max(ans,min(c4+c1-a,x4+x1-b));
                ans=max(ans,min(c4+c2-a,x4+x2-b));
            }
        }
        return ans;
    }
};