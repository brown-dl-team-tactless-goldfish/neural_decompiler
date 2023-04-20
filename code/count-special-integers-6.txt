class Solution {
public:
    int memo[11][2][2][2<<10];
    int helper(string &s , int &len , int idx , bool last , bool zero , int &mask){
        if(idx==len){
            return 1;
        }
        if(memo[idx][last][zero][mask]!=-1) return memo[idx][last][zero][mask];

        int till = (last ? (s[idx]-'0') : 9);

        int ans = 0;
        for(int i = 0 ; i <= till ; i++){
            if((mask&(1<<i)) == 0){
                if((i!=0) or (i==0 and !zero)) mask |= 1<<i;
                ans +=helper(s,len,idx+1,last&&(i==till),(i==0 and zero),mask);
                mask &= (~(1<<i));
            }
        }
        return memo[idx][last][zero][mask] = ans;
    }
    int countSpecialNumbers(int n) {
        string s = to_string(n);
        int len = s.length() , mask = 0;
        memset(memo,-1,sizeof(memo));
        int ans = helper(s,len,0,true,true,mask)-1;
        return ans;
    }
};