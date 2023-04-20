class Solution {
public:
    int numberOfUniqueGoodSubsequences(string binary) {
        long long int a = 0, b = 0, c = 0, d = 0,mod = 1e9+7;
        /*strart end end a -> 0..0, b -> 0...1, c -> 1....0, d -> 1.....1*/
        for(auto &i: binary){
            if(i=='0'){
                a = 1;
                c = (c+d)%mod;
            }else{
                d = (c+d+1)%mod;
            }
        }
        return (a+b+c+d)%mod;
    }
};