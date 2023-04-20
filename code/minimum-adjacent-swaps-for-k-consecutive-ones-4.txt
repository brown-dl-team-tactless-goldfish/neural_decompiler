class Solution {
public:
    int solveOdd(vector<int>&a, int k, vector<long long>&pref){
        int n=a.size();
        long long res=INT_MAX;
        for(int l=0,r=k-1; r<n ; l++,r++){
            int mid=(l+r)/2;
            int radius=mid-l;
            
            long long right=pref[r]-pref[mid];
            long long left=(mid==0 ? 0: pref[mid-1])-(l==0 ? 0: pref[l-1]);
            long long minus=(radius+1)*radius;
            
            res=min(res,right-left-minus);
        }
        return res;
    }
    
    int solveEven(vector<int>&a, int k, vector<long long>&pref){
        int n=a.size();
        long long res=INT_MAX;
        for(int l=0,r=k-1; r<n ; l++,r++){
            int mid=(l+r)/2;
            int radius=mid-l;
            
            long long right=pref[r]-pref[mid];
            long long left=(mid==0 ? 0: pref[mid-1])-(l==0 ? 0: pref[l-1]);
            long long minus=(radius+1)*radius + (radius+1) + a[mid];
            
            res=min(res,right-left-minus);
        }
        return res;
    }
    
    int minMoves(vector<int>& nums, int k) {
        int n=nums.size();
        vector<int>a;
        for(int i=0;i<n;i++){
            if(nums[i]==1)
                a.push_back(i);
        }
        vector<long long>pref(a.size(),0);
        pref[0]=a[0];
        for(int i=1;i<a.size();i++){
            pref[i]=pref[i-1]+a[i];
        }
        int ans=0;
        if(k%2==0)
            ans=solveEven(a,k,pref);
        else
            ans=solveOdd(a,k,pref);
        return ans;
    }
};