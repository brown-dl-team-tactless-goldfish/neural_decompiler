class Solution {
public:
    bool find(vector<int>&t,vector<int>&w,int mid,int pill,int s)
    {
        multiset<int>st(w.begin(),w.end());
        for(int i=mid-1;i>=0;i--)
        {
            auto it=st.lower_bound(t[i]);
            if(it==st.end())
            {
                it=st.lower_bound(t[i]-s);
                pill--;
                if(it==st.end()||pill<0)
                {
                  return false;
                }
            }
            st.erase(it);
        }
        return true;
    }
    int maxTaskAssign(vector<int>& t, vector<int>& w, int pill,int s) 
    {
        sort(t.begin(),t.end());
        sort(w.begin(),w.end());
        int n=t.size();
        int m=w.size();
        int l=0;
        int ans=l;
        int r=min(n,m);
        while(l<=r)
        {
            int mid=(l+r)/2;
            if(find(t,w,mid,pill,s))
            {
                ans=mid;
                l=mid+1;
            }
            else
            {
                r=mid-1;
            }
        }
        return ans;
    }
};