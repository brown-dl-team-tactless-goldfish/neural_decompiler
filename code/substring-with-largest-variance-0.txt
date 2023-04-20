class Solution {
public:
    int largestVariance(string s) {
        int n = s.size();
        int res = 0;
    
        for (char p = 'a'; p <= 'z'; p++) {
            for (char q = 'a'; q <= 'z'; q++) {
                if (p == q) continue;
                
                int pCount = 0; 
                int qCount = 0; 
                
                
                bool canExtendprevQ = false;
                
                for (auto c : s) {
                    if (c == p) pCount++;
                    if (c == q) qCount++;
                    
                    if (qCount > 0) {
                        res = max(res, pCount - qCount);
                    }
                    else if (qCount == 0 && canExtendprevQ) {
                        res = max(res, pCount - 1);
                    }
                    
                    if (qCount > pCount) {
                        qCount = pCount = 0;
                        
                        canExtendprevQ = true;
                    }
                }
            }
        }
        return res;
    }
};