class Solution {
public:
    long long minCost(vector<int>& b1, vector<int>& b2) {
       
        unordered_map<int,int>cnt1,cnt2;
        int mn = b1[0]; // mn will store the minimum of all the values.
        
        // count occurence of each cost in each basket
        for(int&x:b1)cnt1[x]++, mn = min(mn,x);
        for(int&x:b2)cnt2[x]++, mn = min(mn,x);
        
        // to_swap stores the values that needs to be swapped.
        vector<int>to_swap;
        for(auto u:cnt1){
            int value = u.first;
            int occ1 = u.second;
            int occ2 = cnt2[value];
            int dif = abs(occ1-occ2);
            if(dif%2){
                return -1;
            }
            dif/=2;
            for(int i=0;i<dif;i++)to_swap.push_back(value);
            // we clear the occurences as later we will check unique values of basket2.
            cnt1[value] = 0;
            cnt2[value] = 0;
        }
        for(auto&u:cnt2){
            int value = u.first;
            int occ = u.second;
            if(occ%2) return -1;
            occ/=2;
            for(int i=0;i<occ;i++)to_swap.push_back(value);
        }
        sort(to_swap.begin(),to_swap.end());
        long long ans = 0;
        for(int i=0;i<to_swap.size()/2;i++)ans+=min(2ll*mn,1ll*to_swap[i]);
        return ans;
    }
};