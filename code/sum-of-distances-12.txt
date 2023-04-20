class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        unordered_map<int,vector<long long int>> mp;
        unordered_map<int,long long int> mp1;
        int i,n=nums.size();
        for(i = 0; i < n; i++){
            if(mp[nums[i]].size()==0){
                mp[nums[i]].push_back(i);
            }else{
                mp[nums[i]].push_back(i+mp[nums[i]].back());
            }
            mp1[nums[i]] += i;
        }
        vector<long long int> ans;
        unordered_map<int,int> mp2;
        for(i = 0; i < n; i++){
            mp2[nums[i]]++;
            if(mp2[nums[i]]==1){
                ans.push_back(mp1[nums[i]]-i*1LL*mp[nums[i]].size());
            }else{
                long long int a = i*1LL*mp2[nums[i]] - mp[nums[i]][mp2[nums[i]]-1];
                long long int b = mp1[nums[i]]-mp[nums[i]][mp2[nums[i]]-2]-(mp[nums[i]].size()-mp2[nums[i]]+1)*1LL*i;
                // cout<<a<<" "<<b<<endl;
                ans.push_back(a+b);
            }
        }
        return ans;
    }
};