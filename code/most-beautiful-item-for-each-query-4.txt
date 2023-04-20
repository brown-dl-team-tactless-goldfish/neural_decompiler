class Solution {
    int BinarySearch(vector<vector<int>>& items, int q, vector<int> &Beauty)
    {
        int start = 0, end = items.size()-1;
        int val = 0;
        while(start <= end)
        {
            int mid = start + (end-start)/2;
            if(q >= items[mid][0])
            {
                val = Beauty[mid];
                start = mid+1;
            }
            else
                end = mid-1;
        }
        return val;
    }
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) 
    {
        int n = items.size();
        sort(items.begin(), items.end());
        vector<int> ans, mxBeauty(n);
        mxBeauty[0] = items[0][1];
        for(int i = 1; i < n; i++)
        {
            mxBeauty[i] = max(mxBeauty[i-1],items[i][1]);
        }
        for(int &q : queries)
        {
            ans.push_back(BinarySearch(items, q, mxBeauty));
        }
        return ans;
    }
};