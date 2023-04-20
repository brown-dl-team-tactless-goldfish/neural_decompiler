class Solution {
public:
    int countLatticePoints(vector<vector<int>>& v) { // v is vector of circles.
        int n = v.size();
        int ans = 0;
        for(int x=0;x<=200;x++){
            for(int y=0;y<=200;y++){
                for(int i=0;i<n;i++){
                    int a=v[i][0],b=v[i][1],r=v[i][2];
                    if((a-x)*(a-x) + (b-y)*(b-y) <= r*r){
                        ans++;
                        break;
                    }
                }
            }
        }
        return ans;
    }
};