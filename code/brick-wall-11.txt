class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int,int> map;
        int n=wall.size();
        for(int i=0;i<n;i++){
            int sum=0;
            for(int j=0;j<wall[i].size()-1;j++){
                sum+=wall[i][j];
                map[sum]++;
            }
        }
        int maxi=0;
        for(auto m: map){
            if(m.second>maxi)
                maxi=m.second;
        }
        return n-maxi;
    }
};