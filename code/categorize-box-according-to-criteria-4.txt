class Solution {
public:
    string categorizeBox(int l, int b, int h, int mass) {
        int blk = 0, hv = 0;
        if(l >= 10000 || b >= 10000 || h >= 10000 || (long long)l * b * h >= 1e9)  blk = 1;
        if(mass >= 100) hv = 1;
        
        if(blk && hv) return "Both";
        if(!blk && !hv) return "Neither";
        if(blk && !hv) return "Bulky";
        else return "Heavy";
    }
};