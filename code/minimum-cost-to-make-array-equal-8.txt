class Solution {
public:
    long long mini(long long a,long long b){
        if(a<=b)return a;
        return b;
    }
    
    long long caldist(int n,vector<int>& nums,vector<int>& cost){
        long long ans=0;
        for(int i=0;i<nums.size();i++){
            ans+=(long long)((long long)abs(nums[i]-n)*(long long)cost[i]);
        }
        return ans;
    }
    
    long long minCost(vector<int>& nums, vector<int>& cost) {
        int mn=1e9,mx=0;
        for(int i=0;i<nums.size();i++){
            mn=min(mn,nums[i]);
            mx=max(mx,nums[i]);
        }
        if(mn==mx)return 0;
        
    
        int s=mn,e=mx;
        int mid=s+(e-s)/2;
        long long ans=1e18+1;
        while(e>=s){
           
            long long c1=caldist(mid,nums,cost);
            long long c2=1e18+1,c3=1e18+1;
            if(mid>mn)
             c2=caldist(mid-1,nums,cost);
            if(mid<mx)
             c3=caldist(mid+1,nums,cost);
             //cout<<mid<<" "<<c<<endl;
            
            if(c1<c2 and c1<c3)return c1;
            
            if(c1<c2)s=mid+1;
            else e=mid-1;
            ans=c1;
            mid=s+(e-s)/2;
        }
        return ans;
    }
};