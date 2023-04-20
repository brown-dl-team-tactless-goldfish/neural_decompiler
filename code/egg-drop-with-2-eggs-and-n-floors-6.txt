class Solution {
public:
    int twoEggDrop(int n) {
        int sq=sqrt(2*n);
        while(sq*(sq+1)>=2*n){
            sq--;
        }
        return sq+1;
    }
};