class Solution {
public:
    int minCapability(vector<int>& arr, int k) {
        int low=*min_element(arr.begin(),arr.end());
        int high=*max_element(arr.begin(),arr.end());
        int n=arr.size();
        while(low<=high){
            int mid=low+(high-low)/2;
            int taken=0;
            for(int i=0;i<n;i++)
               if(mid>=arr[i])taken++,i++;
             if(taken<k)low=mid+1;
            else high=mid-1;
        }
        return low;
    }
};