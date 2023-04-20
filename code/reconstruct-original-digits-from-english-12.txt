class Solution 
{
const int DIGS[10] = {0,2,4,6,8,5,7,3,9,1}, CHARS[10] = {25,22,20,23,6,5,18,7,8,14};
const vector<vector<int>> REMS = {{14},{14},{5,14},{18,8},{8,7},{8},{},{},{},{}};
public:
    string originalDigits(string S)
     {
        int fmap[26] = {0}, ans[10] = {0};
        for (char c : S) fmap[c - 97]++;
        for (int i = 0; i < 10; i++) 
        {
            int count = fmap[CHARS[i]];
            for (int rem : REMS[i]) fmap[rem] -= count;
            ans[DIGS[i]] = count;
        }
        string ansstr;
        for (int i = 0; i < 10; i++)
         {
            char c = (char)(i + 48);
            for (int j = ans[i]; j; j--)
                ansstr += c;
        }
        return ansstr;
    }
};