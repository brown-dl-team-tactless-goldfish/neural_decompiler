class Solution {
public:
    int shortestSubarray(vector<int>& A, int k) {
        int n = A.size();
        int ans = n+1;
        vector<long long> nums(n);
        deque<int> Pre;
        for(int i = 0 ; i < n ; i++){
            nums[i] = A[i];
            if(i) nums[i] += nums[i-1];
            //if sum if greater than or equal to answer mean we found the answer.
            if(nums[i] >= k){
                ans = min(ans,i+1);
            }
            //neagitive elements can be there at the front of dequeue
            //that's why we have to remove the elements from the front of the queue irrespective of 
            //the sum is greater than k or not because there can be a case such that sum is not greater than
            //k but excluding the front element of the queue making the sum greater than k.
            while(!Pre.empty() && nums[i] - nums[Pre.front()] >= k){
                ans = min(ans,i-Pre.front());
                Pre.pop_front();
            }
            //find where to insert the current sum till position i.
            while(!Pre.empty() && nums[Pre.back()] >= nums[i]){
                Pre.pop_back();
            }
            //insert the sum into the stack.
            Pre.push_back(i);
        }
        return (ans == n+1)?-1:ans;
    }
};