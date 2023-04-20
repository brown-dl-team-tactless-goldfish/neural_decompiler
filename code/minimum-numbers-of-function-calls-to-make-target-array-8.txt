class Solution {
public:
    int minOperations(vector<int>& nums) {
        int res=0;
        int n=nums.size();
		//Work backwards i.e.  go from nums to arr
        while(1){
            int count=0,countzero=0;
            for(int i=0;i<n;i++){
                if(nums[i]%2!=0){
                    nums[i]-=1; // decrease the odd number by one 
                    res++;
                }else{
                    count++;  // count the even numbers in array 
                } 
                if(nums[i]==0){
                    countzero++; // count the zeros in array 
                }
            }
			// if count of zeros is equal to length of array means that array come at intial condition i.e. [0,0....] thus simply return res
            if(countzero==n){
                return res;
            }
			// if count of even is equal to length of array means that array contains even numbers only so divide them by 2 and increase res by 1
            if(count==n){
                res++;
                for(int i = 0 ; i < n ; i++) 
                    nums[i]/=2;
            }
        }
        return res;
    }
};