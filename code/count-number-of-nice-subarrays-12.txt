class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {

        int n = nums.size();

        // total number of calid subarray
        int res = 0;
        
        // count the odd numbers in the window
        int cnt = 0;
        
        // first and last pointer of sliding window
        int i = 0;
        int j = 0;
        while(j<n)
        {
            // update count of the odd number in window
            if((nums[j++]&1)==1)cnt++;            
            
            // shrink window until odd number count == k
            while(cnt>k)if((nums[i++]&1)==1)cnt--;      
            
            // if odd number count == k then we found our main subarray
            if(cnt==k)
            {
                int lc = 0, rc = 0;
                
                // shrink window from left till any odd number found
                // means, count number of even number at the left of first odd number in window, EL
                while(j<n && (nums[j]&1)==0)j++,rc++;

                // expand window to right till any odd number found
                // means, count number of even number at the right of last odd number in window, ER
                while(i<n && (nums[i]&1)==0)i++,lc++;
                
                // based on probability formula the total possible subarray inclusing all odd numbers
                // of the main subarray window is (EL + 1) * (ER + 1)
                res+= ((lc+1) * (rc+1));
            }
        }
        
        return res;
    }
};