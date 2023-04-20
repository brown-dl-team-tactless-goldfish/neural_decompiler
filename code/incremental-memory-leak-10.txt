class Solution {
public:
    vector<int> memLeak(int memory1, int memory2) {
        int i=1;
        int c=1;
        while(max(memory1,memory2)>=i)
        {
            if(memory1>=memory2)
            {
                memory1-=i;
            }
            else
            {
                memory2-=i;
            }
            c++;
            i++;
        }
        return {c,memory1,memory2};
    }
};