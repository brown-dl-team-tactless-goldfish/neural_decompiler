class Solution {
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        int h = *max_element(nums.begin(),nums.end()); // max bag size
        int l = 1;
        while(l<h)
        {
            int c = 0;
            int mid = (l+h)/2;                          // mid of size
            for(int x : nums)                   
                c += (x - 1)/mid;                       // cout no of operatin 
            if(c > maxOperations)                       // if size is small large no of operations 
                l = mid +1;                             // neglect range of small size 
            else
                h = mid;                                // set higher bound to mid obtain optimal sol
        }
        return l;
    }
};