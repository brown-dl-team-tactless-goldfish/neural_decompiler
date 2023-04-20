#define long long long

class Solution {
public:
    string subStrHash(string str, int power, int mod, int k, int hashValue) {
        long hash = 0;
        long power_k = 1;
        
        for(int i = 1; i < k; i++)
            power_k = (power * power_k) % mod;
        
        int n = str.length();
        int j = n-1, inx = 0;
        for(int i = n-1; i >= 0; i--) {
            int val = str[i] - 'a' + 1;
            hash = (power*hash + val) % mod;
            if(j-i+1 == k) {
                if(hash == hashValue) 
                    inx = i;
                val = str[j] - 'a' + 1;
                hash = (hash - (power_k*val)) % mod;
                hash = (hash + mod) % mod;
                j -= 1;
            }
        }
        
        return str.substr(inx, k);
    }
};