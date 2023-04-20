class Solution {
public:
    int hIndex(vector<int>& citations) {
        int size = citations.size();
        int low = 0, high = size;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (size - mid <= citations[mid])
                high = mid;
            else
                low = mid + 1;
        }
        return size - high;
    }
};