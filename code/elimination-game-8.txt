class Solution {
public:
    int lastRemaining(int n) {
        bool left = true;
        int head = 1, step = 1, rem = n;
        while(rem>1) {
            if(left || rem%2==1) {
                head = head + step;
            }   
            rem = rem/2;
            step = step*2;
            left = !left;
        }
        return head;
    }
};
