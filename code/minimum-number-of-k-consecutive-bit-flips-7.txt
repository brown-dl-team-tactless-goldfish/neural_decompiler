class Solution {
public:
    int minKBitFlips(vector<int>& A, int K) {
        int ans = 0;
        int size = A.size();
        queue<int> record;
        for(int i = 0; i < size; i++)
        {
            int pivot = record.size() % 2 == 0 ? A[i] : 1 - A[i];
            if(pivot == 0)
            {
                ans++;
                record.push(i + K - 1);
            }
            if(!record.empty() && i == record.front()) record.pop();
        }
        return record.empty() ? ans : -1;
    }
};