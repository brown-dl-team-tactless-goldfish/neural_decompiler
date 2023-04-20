class Solution {
public:
    int minOperations(int n) {
        int ops = 0;
        unsigned stack = n;
        
        while(stack > 0) {
            if(stack & 1) {
                ops++;
                stack >>= 1;
                
                if(!(stack & 1)) continue;
                while(stack & 1) stack >>= 1;
                stack |= 1;
            }
            else stack >>= 1;
        }
        
        return ops;
    }
};