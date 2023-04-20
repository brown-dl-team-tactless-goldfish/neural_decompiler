class Solution {
    class comp{
    public:
        bool operator()(pair<int,int> a,pair<int,int> b){
			//// a/b < c/d  ==> a*d < c*b //////
			///// doing this to avoid comparing doubles //////////
            return a.first*b.second < a.second*b.first;
        }
    };
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        priority_queue<pair<int,int>,vector<pair<int,int>>,comp> pq;
        
        for(int i=0;i<arr.size();i++)
        {
            for(int j=i+1;j<arr.size();j++)
            {
                pq.push({arr[i],arr[j]});
                if(pq.size()>k)
                    pq.pop();
            }
        }
        
        pair<int,int> ans=pq.top();
        
        return {ans.first,ans.second};
    }
};