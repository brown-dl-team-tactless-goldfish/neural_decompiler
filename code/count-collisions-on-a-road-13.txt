class Solution {
public:
    int countCollisions(string str) {
        stack<char>st;
        int ans=0;
        for(int i=0;i<str.length();i++)
        {
            if(st.empty())
            {
                st.push(str[i]);
            }
            else
            {
                if(st.top()=='R' and str[i]=='L')
                {
                    st.top()='S';
                    ans+=2;
                }
                else if(st.top()=='S' and str[i]=='L')
                {
                    ans+=1;
                }
                else if(st.top()=='S' and str[i]=='R')
                {
                    st.push(str[i]);
                }
                else if(st.top()=='R' and str[i]=='S')
                {
                    ans+=1;
                    st.top()='S';
                }
                else if(st.top()=='L' and str[i]=='S')
                {
                    st.push(str[i]);
                }
                else
                {
                    st.push(str[i]);
                }
            }
        }
        while(!st.empty())
        {
            char ch=st.top();
            st.pop();
            if(!st.empty())
            {
                if(ch=='S' and st.top()=='R')
                {
                    ans+=1;
                    st.top()='S';
                }
                else if(ch=='L' and st.top()=='R')
                {
                    st.top()='S';
                    ans+=2;
                }
            }
        }
        return ans;
    }
};