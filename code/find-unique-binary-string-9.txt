class Solution {
public:
    bool generate(string& result, int n, unordered_set<string>& st) {
        if(n <= 0) {
            return !st.count(result) ? true : false;
        }
        
        result[n-1] = '0'; //check with '0' and explore further
        if(generate(result, n-1, st))
            return true;
        
        result[n-1] = '1'; //check with '1' and explore further
        return generate(result, n-1, st);
    }
    string findDifferentBinaryString(vector<string>& nums) {
        unordered_set<string> st(begin(nums), end(nums));
        int n = nums[0].length();
        string result(n, ' ');
        
        generate(result, n, st);
        
        return result;
    }
};