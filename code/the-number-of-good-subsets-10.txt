class Solution {
public:
    int power(long long x,  int y, int p)
{
    int res = 1;     // Initialize result
 
    x = x % p; // Update x if it is more than or
                // equal to p
  
    if (x == 0) return 0; // In case x is divisible by p;
 
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;
 
        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;
    }
    return res;
}
    vector<int> primes={2,3,5,7,11,13,17,19,23,29};
    int help(int a){
        int ans=0;
        for(int i=0;i<primes.size();i++){
            if(a%primes[i]!=0){
                continue;
            }
            a/=primes[i];
            ans=ans | (1<<(primes[i]));
            if(a%primes[i]==0){
                return -1;
            }
        }
        return ans;
    }
    long long ans=0;
    int mod=1000000007;
    void help(int i, long long product,int mask, vector<int> &res, vector<int> &arr, vector<int>& bitmask,vector<int>& freq){
        
        if(i==arr.size()){
            
            if(res.size()==0){
                
                return;
            }
            
            long long l=1;
            for(int k=0;k<res.size();k++){
                l=(l%mod * (freq[res[k]]%mod))%mod;
            }
            ans=(ans%mod + l%mod)%mod;
            return;
        }
        help(i+1,product,mask,res,arr,bitmask,freq);
        long long curr=arr[i];
        if((bitmask[curr]&mask)!=0){
            return;
        }
        product=(product%mod * (curr%mod))%mod;
        mask = mask | (bitmask[curr]);
        res.push_back(curr);
        help(i+1,product,mask,res,arr,bitmask,freq);
        res.pop_back();
        
        
        
    }
    int numberOfGoodSubsets(vector<int>& nums) {
        vector<int> freq(31 , 0);
        vector<int> arr;
        vector<int> bitmask(31 , 0);
        for(int i=0;i<nums.size();i++){
            int temp=help(nums[i]);
            if(freq[nums[i]]==0 && temp!=-1 && nums[i]!=1){
                arr.push_back(nums[i]);
                bitmask[nums[i]]=temp;
            }
            freq[nums[i]]++;
        }
        
        vector<int> res;
        
        help(0,1,0,res,arr,bitmask,freq);
        
        ans=((ans%mod)*(power(2,freq[1],mod))%mod)%mod;
        return ans;
        
        
    }
};