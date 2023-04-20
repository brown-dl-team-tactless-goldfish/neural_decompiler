const int N=1e5+100;
class Solution {
public:
    int fa[N],sz[N],mx;bool vis[N];
	
    int find(int x){return x==fa[x]?x:fa[x]=find(fa[x]);}
	
    void merge(int x,int y){
        if(find(x)!=find(y)){
            sz[find(x)]+=sz[find(y)];
            mx=max(mx,sz[find(x)]);
            fa[find(y)]=find(x);
        }
    }
	
    int validSubarraySize(vector<int>& nums, int threshold) {
        for(int i=0;i<nums.size();i++)fa[i]=i,sz[i]=1,vis[i]=0;
        mx=1;
        vector<int>p(nums.size());iota(p.begin(),p.end(),0);
		
        sort(p.begin(),p.end(),[&](int i,int j){return nums[i]>nums[j];});
		
        for(auto x:p){
            if(x&&vis[x-1])merge(x,x-1);
            if(vis[x+1])merge(x,x+1);
            if(nums[x]>threshold/mx)return mx;
            vis[x]=1;
        }
        return -1;
    }
};