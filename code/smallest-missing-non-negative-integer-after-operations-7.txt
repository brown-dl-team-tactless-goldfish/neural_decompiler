class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        int mx = INT_MAX/value * value;
        for(auto & i : nums){ // i forgot how to take negative modulo the right way, quick hack/fix
            long long t = i;
            t += mx;
            t %= value;
            i = t;
        }
        map<int, int> freq;
        for(auto & i : nums) freq[i%value]++;
        for(int i = 0; i <= 100001; i++){
            freq[i%value]--;
            if(freq[i%value] == -1) return i;
        }
        return -1;
    }
};