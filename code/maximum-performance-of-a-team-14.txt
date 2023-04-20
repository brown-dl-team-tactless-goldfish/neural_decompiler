class Solution {
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        vector<pair<int,int>> perf(n);
        for(int i=0;i<n;i++)
        {
            perf[i]={efficiency[i],speed[i]};
        }
        
        //sort the perf in descending order
        sort(rbegin(perf),rend(perf));
        
        //priority queue to get the smallest sum 
        priority_queue<int,vector<int>,greater<int>> pq; //min heap
        long sum=0;
        long  res=0;
        for(auto [eff,speed] : perf)
        {
            sum+=speed;
			//push the current speed to the pq
            pq.push(speed);
            if(pq.size()>k)
            {
                //remove the smallest speed
                sum-=pq.top();
                pq.pop();
            }
			//since eff is the currents small efficiency 
            res=max(res,sum*eff);
        }
        return res % (int)(1e9+7);
    }
};