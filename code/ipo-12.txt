class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& p, vector<int>& c) {
        int n=p.size(),ans=0,it=0,nn=0,ma=0,mb=0,sz=0,sq[101][101]={};
        for(int i=0;i<n;++i)
            if(c[i]<=w){
                sq[p[i]/100][p[i]%100]++;
                sq[p[i]/100][100]++;
                ma=max(ma,p[i]);
                sz++;
            }
        mb=ma/100;
        pair <int,int> a[max(n-sz,1)];
        for(int i=0;i<n;++i)
            if(c[i]>w)
                a[nn++]={c[i],p[i]};
        for(sort(a,a+nn);k--&&sz;){
            if(sq[mb][ma%100]==0){
                while(sq[mb][100]==0)--mb;
                ma=99;
                while(sq[mb][ma]==0)--ma;
                ma+=mb*100;
            }
            w+=ma;
            sq[mb][ma%100]--;
            sq[mb][100]--;
            sz--;
            for(;it<nn;++it){
                if(a[it].first>w)break;
                sq[a[it].second/100][a[it].second%100]++;
                sq[a[it].second/100][100]++;
                sz++;
                if(a[it].second>=ma){
                    ma=a[it].second;
                    mb=ma/100;
                }
            }
        }
        return w;
    }
};