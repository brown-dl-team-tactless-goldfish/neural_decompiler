class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& tt) {
        int a=0,b=0,c=0;
        for(auto &x: triplets)  
            if( x[0] <= tt[0] && x[1] <= tt[1] && x[2] <= tt[2]) 
            {  a= max(a,x[0]); b= max(b,x[1]);  c= max(c,x[2]); }
        return  (a==tt[0] && b==tt[1] && c==tt[2]) ? true :false;   
    }
};
