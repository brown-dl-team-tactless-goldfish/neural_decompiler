class Solution {
public:
    int superpalindromesInRange(string L, string R) {
        int res = 0;
        long  l = stol(L);
        long  r = stol(R);
        back_tracking("", res, l, r);
        for(char c = '0'; c <= '9'; c++){
            back_tracking(string(1,c), res, l, r);
        }
        return res;
    }
    void back_tracking(string cur, int& res, long & l, long & r){
        if(cur.size() > 9) return;
        
        if(!cur.empty() && cur[0] != '0'){
            long cur_num = stol(cur);
            long pow_2_cur = cur_num * cur_num;
            if(pow_2_cur > r) return;
            if(pow_2_cur >= l && is_palindrome(to_string(pow_2_cur))) res++; 
        }
        for(char c = '0'; c <= '9'; c++)
            back_tracking( string(1,c) + cur + string(1,c), res, l, r);
    }
    bool is_palindrome(string s){
        int l = 0, r = s.size()-1;
        while(l < r){
            if(s[l] != s[r]) return false;
            l++; r--;
        }
        return true;
    }
};