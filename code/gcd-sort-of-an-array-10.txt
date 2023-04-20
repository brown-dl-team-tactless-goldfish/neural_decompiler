class Solution {
public:
    int find(int a, vector<int> &p){
        if(p[a]<0){
            return a;
        }
        int x=find(p[a],p);
        p[a]=x;
        return x;
    }
    void merge(int a, int b, vector<int>&p){
        int x=find(a,p);
        int y=find(b,p);
        if(x==y){
            return ;
        }
        if(p[x]<=p[y]){
            p[x]+=p[y];
            p[y]=x;
        }
        else{
            p[y]+=p[x];
            p[x]=y;
        }
    }
    bool gcdSort(vector<int>& nums) {
        int n=nums.size();
        vector<int> p(100002 , -1);
        
        for(int i=0;i<n;i++){
            int curr=nums[i];
            for(int j=2;j*j<=curr;j++){
                if(curr%j!=0){
                    continue;
                }
                merge(curr,j,p);
                merge(curr,curr/j,p);
            }
        }
        vector<int> temp=nums;
        sort(temp.begin(),temp.end());
        for(int i=0;i<n;i++){
            if(find(temp[i],p)!=find(nums[i],p)){
                return false;
            }
        }
        return true;
    }
};