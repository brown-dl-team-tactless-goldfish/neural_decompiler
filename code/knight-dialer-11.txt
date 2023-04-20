class Solution {
public:
    int knightDialer(int n) {
        int mod = pow(10, 9) + 7;
        vector<vector<int>> v = {{4,6}, {6,8}, {7,9}, {4,8}, {3,9,0}, {}, {1,7,0}, {2,6}, {1,3}, {2,4}};
        
        vector<long> count(10, 1), curr_count(10, 0);
        
        for (int i = 0; i < n-1; i++) {
            fill(curr_count.begin(), curr_count.end(), 0);
            
            for (int j = 0; j < 10; j++) {
                
                for (auto next : v[j]) {
                    curr_count[next] += count[j] % mod;
                }
                
            }
            
            count = curr_count;
        }

        long total = 0;
        for (auto c : count) total += c % mod;
        return total % mod;
    }
};