class Solution {
public:
    int maxEqualFreq(vector<int>& nums) {
        map<int,int>mp;
        int n=nums.size();
        
        if(n==1)
            return 0;
        
        //remove exactly 1 number 
        //try to store maxfreq-1 freq also
        int maxfreq=0,freq=0,maxfreq2=0,freq2=0;
        int ans=0;
        for(int i=0; i<n; i++)
        {
            mp[nums[i]]++;
            
            if(mp[nums[i]]>maxfreq)
            {
                freq2=freq;
                maxfreq2=mp[nums[i]]-1;
                
                maxfreq=mp[nums[i]];
                freq=1;
            }
            else if(mp[nums[i]]==maxfreq)
            {
                freq++;
            }
            else if(mp[nums[i]]==maxfreq2)
            {
                freq2++;
            }
            
            //cout<<maxfreq<<" "<<freq<<" "<<maxfreq2<<" "<<freq2<<endl;
            if(maxfreq2*freq2==i)
            {
                ans=max(ans,i+1);
            }
            if(maxfreq*freq==i)
            {
                ans=max(ans,i+1);
            }
            if(maxfreq==1 && maxfreq*freq==i+1)
            {
                ans=max(ans,i+1);                
            }
        }
        return ans;
    }
};