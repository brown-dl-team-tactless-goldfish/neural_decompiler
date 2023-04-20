class Solution {
public:
    int findKthSorted(int n,int m,int k){
        // int m=matrix.size(),n=matrix[0].size();
        
        int low=1,high=m*n;
        while(low<high){
            int mid=low+(high-low)/2;
            // cout<<low<<" "<<mid<<" "<<high<<endl;
            int val=0;
            for(int i=0;i<m;i++){
                val+=(mid/(i+1))>=n?n:mid/(i+1);
            }
            // cout<<val<<endl;
            if(val>=k){
                high=mid;
            }
            // else if(val==k){
            //     return mid;
            // }
            else{
                low=mid+1;
            }
            
        }
        return low;
    }
    int findKthNumber(int m, int n, int k) {
        
        return findKthSorted(n,m,k);
        
    }
};