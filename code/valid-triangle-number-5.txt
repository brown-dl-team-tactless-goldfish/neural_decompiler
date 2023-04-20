class Solution {
public:
    int triangleNumber(vector<int>& a) {
        sort(a.begin(),a.end());
        int n=a.size(),c=0;
        if(n<3)return 0;
        for(int i=0;i+2<n;i++){
            for(int j=i+1;j<n&&a[i]>0;j++){
                int k;
                auto it = lower_bound(a.begin(),a.end(),a[i]+a[j]);
                k = it-a.begin();
                c += (k-j-1);
            }
        }
        return c;
    }
};