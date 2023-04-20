class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        unordered_map<int, int> map;
        int n = digits.size();
        vector<int> ans;
        for(int i = 0; i < n; i++)
        {
            map[digits[i]]++;
        }
        for(int i = 1; i < 10; i++)
        {
            if(map[i] == 0) continue;
            
            --map[i];
            for(int j = 0; j < 10; j++)
            {
                if(map[j] == 0) continue;
                
                --map[j];
                for(int k = 0; k < 10; k=k+2)
                {
                    if(map[k] == 0) continue;
                    
                    ans.push_back(i*100 + j*10 + k);
                }
                ++map[j];
            }
            ++map[i];
        }
        return ans;   
    }
};