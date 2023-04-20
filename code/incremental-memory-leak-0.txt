class Solution {
public:
    vector<int> memLeak(int val1, int val2) {
        
        int second = 1;

        while(true)
        {
            if(val1 == val2 and (val1 >= second))
            {
                val1 = val1 - second;
                second++;
            }
            else if(val1 > val2 and (val1 >= second))
            {
                val1 = val1 - second;
                second++;
            }
            else if(val2 > val1 and (val2 >= second))
            {
                  val2 = val2 - second;
                  second++;
            }
            else
            {
                break;
            }
        }
        return {second,val1,val2};
    }
};