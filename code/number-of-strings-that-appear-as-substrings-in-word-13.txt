class Solution {
public:
    int numOfStrings(vector<string>& arr, string word) {
        int count=0;
        for(int i=0;i<arr.size();i++)
        {
            if(word.find(arr[i])==-1)
            {
                continue;
            }
            else
            {
                count++;
            }
        }
        return count;
    }
};