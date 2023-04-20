class Solution {
public:
    
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        int sum = 0, n = reward1.size();
        vector<pair<int,int>> arr;
        
        for(int i=0;i<n;i++)
        {
            int diff = reward1[i]-reward2[i];
            arr.push_back({diff,i}); //storing pair of difference, index
        }
        
        sort(arr.begin(),arr.end());
        reverse(arr.begin(),arr.end()); // sorted in descending order
        
        int i;
        for(i=0;i<k;i++) //add k values from reward1
        {
            auto x = arr[i];
            int index = x.second;
            sum += reward1[index];
        }
        
        for(;i<n;i++) // add remaining values from reward2
        {
            auto x = arr[i];
            int index = x.second;
            sum += reward2[index];
        }
        
        return sum;
    }
};