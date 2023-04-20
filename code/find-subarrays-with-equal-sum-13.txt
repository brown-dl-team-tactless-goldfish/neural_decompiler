class Solution {
public:
    bool findSubarrays(vector<int>& ar) 
    {
        int n = ar.size();        
        unordered_map<int,int>mymap;
        
        for(int i = 0 ; i + 1 < n ; i++){
            int sum  = ar[i] + ar[i + 1]; 
            if(mymap.count(sum)){
                return true;
            }
            mymap[sum]++;
        }
        return false;
        
    }
};