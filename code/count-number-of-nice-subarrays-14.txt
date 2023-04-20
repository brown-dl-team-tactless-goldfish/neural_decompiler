class Solution {
public:
    int numberOfSubarrays(vector<int>& a, int k) {
        int n = a.size();
        vector<int>left(n,0);
        vector<int>right(n,0);
        int c = 0;
        for(int i=0;i<n;i++) {
            if(a[i]%2==0) c++;
            else {right[i]=c; c=0;}
        }
        c = 0;
        for(int i=n-1;i>=0;i--) {
            if(a[i]%2==0) c++;
            else {left[i]=c; c=0;}
        }
        // for(int i=0;i<n;i++) cout<<left[i]<<" ";
        // cout<<endl;
        // for(int i=0;i<n;i++) cout<<right[i]<<" ";
        
        int i = 0;
        int j = 0;
        int x = 0;
        int ans = 0;
        while(j<n) {
            if(j<n && a[j]%2!=0) x++;
            if(x>k) {
                while(x>k) {
                    if(i<n && a[i]%2!=0) x--;
                    i++;
                }
            }
            else if(x==k) {
                while(i<n && a[i]%2==0) {
                    i++;
                }
                cout<<ans<<" ";
                ans+=(right[i]+1)*(left[j]+1);
                if(a[i]%2!=0) x--;
                i++;
            }
            
            j++;
        }
        return ans;
    }
};