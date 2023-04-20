class Solution {
public:
    string categorizeBox(int length, int width, int height, int mass) {
        long long v = (long long)length* (long long)width* (long long)height;
        int b = 0, h = 0;
        if(length >= 10000 || height >= 10000 || width >= 10000 || v >= 1000000000) b = 1;
        if(mass >= 100) h = 1;
        if(h && b) return "Both";
        if(h == 0 && b == 0) return "Neither";
        if(h) return "Heavy";
        return "Bulky";
    }
};