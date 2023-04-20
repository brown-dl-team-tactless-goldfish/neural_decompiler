class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int can) {
        priority_queue<long long, vector<long long>, greater<long long>> pql, pqr;
        int n = costs.size(), s = 0, e = n - 1, cnt = 0;
        while(s < can && cnt < n) pql.push(costs[s++]), cnt++;
        while(e >= n - can && cnt < n) pqr.push(costs[e--]), cnt++;
        
        long long ans = 0, t = 0;
        while(t < k) {
            long long a = INT_MAX, b = INT_MAX;
            if(pql.size()) a = pql.top();
            if(pqr.size()) b = pqr.top();
            if(a > b) {
                ans += b;
                pqr.pop();
                if(s <= e && cnt < n) pqr.push(costs[e--]), cnt++;
            }
            else {
                ans += a;
                pql.pop();
                if(s <= e && cnt < n) pql.push(costs[s++]), cnt++;
            }
            t++;
        }
        return ans;
    }
};