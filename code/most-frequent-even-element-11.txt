class Solution {
public:
    int mostFrequentEven(vector<int>& nums) {
        map <int,int> mp;
        int k;
        int maxi=INT_MIN;
        int flag=0;
        for(int i:nums) mp[i]++;
        for(auto &it:mp){
            if((it.second>maxi) &&((it.first)%2==0)){
             maxi=it.second;
            k=it.first;
            flag=1;
            }
        }
        if(flag)
            return k;
        else
            return -1;
    }
};