class Solution {
public:
    int minimumDeviation(vector<int>& arr) {
        int n = arr.size();
        int maxi = INT_MIN;
        int mini = INT_MAX;
        for(int i = 0; i < n; i++)
        {
            if(arr[i] % 2 != 0)
            {
                arr[i] = 2 * arr[i];
            }
            maxi = max(maxi, arr[i]);
            mini = min(mini, arr[i]);
        }
        priority_queue<int> pq;
        for(int i = 0; i < n; i++)
        {
            pq.push(arr[i]);
        }
        int min_deviation = maxi - mini;
        int top = 0; 
        while(pq.top() % 2 == 0)
        {
            top = pq.top();
            pq.pop();
            min_deviation = min(min_deviation, top - mini);
            mini = min(mini, top / 2);
            pq.push(top / 2);
        }
        top = pq.top();
        min_deviation = min(min_deviation, top - mini);
        return min_deviation;
    }
};