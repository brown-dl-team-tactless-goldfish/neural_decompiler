class Solution {
public:
    int reverseDigits(int num)
{
    int rev_num = 0;
    while (num > 0) {
        rev_num = rev_num * 10 + num % 10;
        num = num / 10;
    }
    return rev_num;
}
    bool sumOfNumberAndReverse(int num) {
        if(num == 0) return true;
        else
        {
        for(int i=0;i<num;i++)
        {
            if(i + reverseDigits(i) == num)
            {
                return true;
            }
        }
        return false;
        }
    }
};