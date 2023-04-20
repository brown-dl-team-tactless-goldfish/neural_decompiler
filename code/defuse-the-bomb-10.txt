class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        if(k == 0){
            for(int i = 0 ; i < code.size() ; i++){
                code[i] = 0;
            }
            return code;
        }
        if(k > 0){
            vector<int> forward(n,0);
            int sum = 0;
            for(int i = 0 ; i < k ; i++){
                sum += code[i];
            }
            int j = k - 1;
            for(int i = code.size() - 1 ; i >= 0 ; i--, j--){
                if(j < 0){
                    j = n - 1;
                }
                forward[i] = sum;
                sum -= code[j];
                sum += code[i];
            }
            return forward;
        }
        else
        {
            k = abs(k);
            vector<int> backword(n ,0);
            int c = 0;
            int sum = 0;
            for(int i = n - 1 ; c < k && i >= 0; c++ , i--){
                sum += code[i];
            }
            int j = n - k;
            for(int i = 0 ; i < n ; i++ , j++){
                if(j > n - 1){
                    j = 0;
                }
                backword[i] = sum;
                sum -= code[j];
                sum += code[i];
            }
            return backword;
        }
    }
};