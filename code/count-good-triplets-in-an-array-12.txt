class Solution {
public:
    #define ll long long
    vector<ll>inv;
    vector<pair<int,int>>v;
    void merge(int l,int mid,int h)
    {
        int i=l,j=mid+1;
        while(i<=mid || j<=h)
        {
            if(i>mid)
                break;
            else if(j>h)
            {
                int ind=v[i].second;
                inv[ind]+=(j-mid-1);
                i++;
            }
            else if(v[i].first<v[j].first)
            {
                int ind=v[i].second;
                inv[ind]+=(j-mid-1);
                i++;
            }
            else
                j++;
        }
        sort(v.begin()+l,v.begin()+h+1);
    }
    void mergesort(int l,int h)
    {
        if(l<h)
        {
            int mid=(l+h)/2;
            mergesort(l,mid);
            mergesort(mid+1,h);
            merge(l,mid,h);
        }
    }
    long long goodTriplets(vector<int>& nums1, vector<int>& nums2) 
    {
        //Map each val in nums2 with corresponding index in nums1
        //Then find no. of pairs nums2[i]<nums2[j]<nums2[k] where i<j<k
        
        int n=nums1.size();
        vector<int>mp(n);
        for(int i=0;i<n;i++)
            mp[nums1[i]]=i;
        for(int i=0;i<n;i++)
        {
            nums2[i]=mp[nums2[i]];
            v.push_back({nums2[i],i});
        }
        
        //First count inversion for each element in nums2 after maping
        inv.resize(n,0);
        mergesort(0,n-1);
        
        //left[i] ->count of no. of elements less than nums2[i] in left
        //right[i] ->count of no. of elements greater than nums2[i] in right 
        ll res=0;
        for(int i=0;i<n;i++)
        {
            ll right=(n-i-1)-inv[i];
            ll left=nums2[i]-inv[i];
            res+=(left*right);
        }
        return res;
    }
};