class Solution {
public:
    int maximumRobots(vector<int>& chargeTimes, vector<int>& runningCosts, long long budget) {
        int ans=0;
        int n=chargeTimes.size();

        vector <long long> prefix(n,0);
        prefix[0]=runningCosts[0];
        for(int i=1;i<n;i++){
            prefix[i]+=prefix[i-1]+runningCosts[i];
        }
        
        long long cost=0;
        long long p=0,q=0;
        priority_queue <pair<long long,int>> pq;
        
        while(q<n){
            while(q<n){
                pq.push({chargeTimes[q],q});
                if(p==0){
                    cost=prefix[q]*(q-p+1)+pq.top().first;
                }
                else{
                    cost=(prefix[q]-prefix[p-1])*(q-p+1)+pq.top().first;
                }
                
                if(cost<=budget){
                    if(ans<q-p+1){
                     ans=q-p+1;
                   }
                }
                else 
                    break;
                q++;
            }
            
            if(q>=n){
                break;
            }
            
            if(p<q){
                p++;
            }
            else{
                p++;
                q++;
            }
            
            while(!pq.empty() && pq.top().second<p){
                pq.pop();
            }
        }
        
        return ans;
    }
};