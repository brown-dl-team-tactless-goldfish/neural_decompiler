class Solution {
public:
    int halveArray(vector<int>& nums) {
        double sum = 0;
	    priority_queue<double> p;
        for(auto x : nums) {
		     sum += x;
             p.push(x);
		}
        double ans = sum;
        int cnt = 0;
        while(sum > ans/2.0){
            cnt++;
            double top = p.top();
            p.pop();
            sum -= top/2.0;
            top = top/2.0;
            p.push(top);
        }
        return cnt;
    }
};