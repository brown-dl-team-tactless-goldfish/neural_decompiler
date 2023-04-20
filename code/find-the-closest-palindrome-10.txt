class Solution {
public:
    string nearestPalindromic(string s) 
    {
        long long no=stoll(s);
        int n=s.size();
        set<long long >st;
        st.insert(pow(10,n)+1);
        st.insert(pow(10,n-1)-1);
        int mid=(n+1)/2;
        long long prefix=stoll(s.substr(0,mid));
        for(int i=-1;i<=1;i++)
        {
            string str=to_string(prefix+i);
            string new_str="";
            if(n&1)
            {
                new_str=str.substr(0,str.size()-1);
            }
            else
            {
                new_str=str;
            }
            reverse(str.begin(),str.end());
            new_str+=str;
            long long x=stoll(new_str);
            st.insert(x);
        }
        st.erase(no);
        long long ans=0;
        long long diff=LONG_LONG_MAX;
        for(auto it:st)
        {
          
            if(abs(it-no)<diff)
            {
                diff=abs(it-no);
                ans=it;
            }
        }
        return to_string(ans);
    }
};