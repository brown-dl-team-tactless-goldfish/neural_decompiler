class Solution {
public:
    long long ans = 0;
    int dfs(vector<vector<int>>& nums,vector<int>& val,vector<long long>& sum,int in,int p){
        sum[in] = val[in];
        long long re = 0;
        for(int i = 0; i<(int)nums[in].size();++i){
            int j = nums[in][i];
            if(j!=p){
                long long k = dfs(nums,val,sum,j,in);
                re = max(re,k);
            }
        }
        return sum[in] = sum[in]+re;
    }
    void dfs2(vector<vector<int>> &nums,vector<int>& val,vector<long long>& sum,int in,int p,long long psum){
        psum+=val[in];
        ans = max(ans,max(psum,sum[in])-val[in]);
        priority_queue<pair<long long,long long>> q;
        for(int i = 0; i<nums[in].size();++i){
            int j = nums[in][i];
            if(j!=p){
                q.push({val[in]+sum[j],j});
            }
        }
        for(int i = 0; i<nums[in].size();++i){
            int j = nums[in][i];
            if(j!=p && q.size()){
                long long k = psum;
                if(q.top().second==j){
                    pair<int,int> p = q.top(); q.pop();
                    if(q.size()) k = max(k,q.top().first);
                    q.push(p);
                }
                else k = max(k,q.top().first);
                dfs2(nums,val,sum,j,in,k);
            }
        }
    }
    long long maxOutput(int n, vector<vector<int>>& arr, vector<int>& cost) {
        vector<vector<int>> nums(n+1);
        for(int i = 0; i<arr.size(); ++i){
            nums[arr[i][0]].push_back(arr[i][1]);
            nums[arr[i][1]].push_back(arr[i][0]);
        }
        vector<long long> dp(n+1,0);
        dfs(nums,cost,dp,0,-1);
        dfs2(nums,cost,dp,0,-1,0);
        return ans;
    }
};