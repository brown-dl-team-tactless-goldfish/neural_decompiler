class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        priority_queue<pair<int,int>> nums2_max;
        // lets push all the elements of nums2 along with idxs into priority queue to get largest elements of nums2
        for(int i=0;i<n;i++){
            nums2_max.push({nums2[i] , i});
        }
        long long curr_sum = 0 , mini = INT_MAX , ans = 0;
        priority_queue<int,vector<int>,greater<int>>temp;
        // 'temp' priority queue stores the elements of nums1 that are contibuting curr_sum
        
        // let's get the top k elements from nums2 and the minimum of those elements will be stored in 'mini'
        // also the sum of corresponding element's nums1 we will store in 'curr_sum'
        while(k--){
            auto top = nums2_max.top();
            nums2_max.pop();
            mini = top.first;
            curr_sum+= nums1[top.second];
            temp.push( nums1[top.second]);
        }
        ans = curr_sum*mini; // setting the curr_sum*mini as answer considering k top indices of nums2        
        // Now we will remove that element/index which is contributing least in sum
        // and add a element which will be corresponding the next(k+1 for first iteration) element
        while(nums2_max.size()){
            curr_sum-=temp.top();    temp.pop();       // removing a element which is contributing least to curr_sum
            auto top = nums2_max.top();     nums2_max.pop();
            mini = top.first;
            curr_sum+= nums1[top.second];
            ans = max(ans , curr_sum*mini);
            temp.push(nums1[top.second]);
        }
        return ans;
    }
};