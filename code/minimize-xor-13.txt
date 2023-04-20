class Solution {
public:
    
    
    long long binpow(long long a, long long b) {
    if (b == 0)
        return 1;
    long long res = binpow(a, b / 2);
    if (b % 2)
        return res * res * a;
    else
        return res * res;
    }
    
    int minimizeXor(int num1, int num2) {
        int n1 = num1;
        int n2 = num2;
        
        int cnt_set_bits_num2 = 0;
        while(n2 > 0){
            cnt_set_bits_num2 += n2 % 2;
            n2 /= 2;
        }
        
        vector<int> temp;
        while(n1 > 0){
            int flag = n1 % 2;
            temp.push_back(flag);
            n1 /= 2;
        }
                

        vector<int> ans(32,0);
        int n = temp.size();
        
        for(int i=n-1 ; i>=0 ; --i){
            if(temp[i] == 1){
                if(cnt_set_bits_num2 > 0){
                    --cnt_set_bits_num2;
                    ans[i] = 1;
                }
            }
        }
        
       
        for(int i=0 ; i<30 ; ++i){
            if(cnt_set_bits_num2 == 0) break;
            if(ans[i] == 0){
                cnt_set_bits_num2--;
                ans[i] = 1;
            }
        }
        
    
        long long res = 0;
        for(int i=0 ; i<32 ; ++i){
            if(ans[i] == 1) res += binpow(2,i);   
        }
        return int(res);
        
    }
};