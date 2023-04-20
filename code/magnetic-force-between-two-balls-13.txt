class Solution {
public:

    bool pass(vector<int> &v , int dis , int balls){
        int c = 1 ;
        int pre = v[0] ;
        for(int i = 1 ; i < v.size() ; i++){
            if(v[i] - pre >= dis){
                c++;
                pre = v[i];
            }
        }
        return c >= balls ;
    }

    int maxDistance(vector<int>& position, int m) {
        sort(position.begin() , position.end()) ;
        int l = 1 ;
        int n = position.size() ;
        int r = position[n-1] ;
        while(r-l > 1){
            int md = l + (r-l)/2 ;
            if(pass(position , md , m))
                l = md ;
            else 
                r = md - 1 ;
        }
        int ans = -1;
        if(pass(position , r , m)) ans = r ;
        else ans = l ;
        return ans ;
    }
};