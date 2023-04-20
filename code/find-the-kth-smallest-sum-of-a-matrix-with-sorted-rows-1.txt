class Solution {
public:
    int n,m;
    vector<int>find(vector<int>&nums1,vector<int>&nums2,int k)
    {
        priority_queue<vector<int>,vector<vector<int>>,greater<vector<int>>>pq;
        for(int i=0;i<min((int)nums1.size(),k);i++)
        {
            pq.push({nums1[i]+nums2[0],i,0});
        }
        vector<int>ans;
        while(pq.size()&&k--)
        {
            auto temp=pq.top();
            pq.pop();
            int sum=temp[0];
            int x=temp[1];
            int y=temp[2];
            ans.push_back(sum);
            if(y+1<nums2.size())
            {
                pq.push({nums1[x]+nums2[y+1],x,y+1});
            }
        }
        return ans;
    }
    int kthSmallest(vector<vector<int>>& mat, int k) 
    {
        m=mat[0].size();
        n=mat.size();
        if(n==1)
        {
            return mat[0][k-1];
        }
        vector<int>ans=find(mat[0],mat[1],k);
        for(int i=2;i<n;i++)
        {
            ans=find(ans,mat[i],k);
        }
        return ans[k-1];
    }
};