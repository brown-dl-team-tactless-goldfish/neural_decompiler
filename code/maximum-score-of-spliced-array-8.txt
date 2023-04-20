class Solution {
public:
    int kadane(vector<int>& n1, vector<int>& n2){
        int s=accumulate(begin(n1),end(n1),0);
        int mx=0,mtn=0;
        for(int i=0;i<size(n1);++i){
            mx+=(n2[i]-n1[i]);
            if(mx<0)mx=0;
            if(mx>mtn)mtn=mx;
        }
        return s+mtn;            
    }
    int maximumsSplicedArray(vector<int>& n1, vector<int>& n2) {
        return max(kadane(n1,n2),kadane(n2,n1));
    }
};