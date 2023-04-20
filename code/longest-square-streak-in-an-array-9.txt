class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        set<long long> st(nums.begin(),nums.end());
        long long  ans=-1;
        for(auto it : nums){
            if(st.find((long long)it*it)!=st.end()){
                long long  cnt=2,val=(long long)it*it;
                while(st.find(val*val)!=st.end()){
                    cnt += 1;
                    val = val*val;
                }
                if(ans<cnt) ans = cnt;
            }
        }
        return ans;
    }
};