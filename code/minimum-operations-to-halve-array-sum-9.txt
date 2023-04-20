class Solution {
public:
    int halveArray(vector<int>& nums) {
        priority_queue<double> pq;
        long long sum = 0;
        for (int x : nums) {
            sum += x;
            pq.push(x);
        }
        
        double half = (double)sum / 2.0;
        int answer = 0;
        
        while (half > 0) {
            double max = pq.top();
            pq.pop();
            
            max /= 2.0;
            half -= max;
            
            if (max > 0) {
                pq.push(max);
            }
            
            answer++;
        }
        
        return answer;
    }
};