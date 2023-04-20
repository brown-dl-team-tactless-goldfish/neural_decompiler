class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
        vector<int>temp;
        for(auto i:cards){
            temp.push_back(i);
        }
        bool c = false;
        sort(temp.begin(),temp.end());
        for(int i=1;i<temp.size();i++){
            if(temp[i-1]==temp[i])
                c = true;
        }
        if(c==false){
            return -1;
        }
        unordered_map<int,int>mp;
        int ans=-1;
        for(int i=0;i<cards.size();i++){
            if(mp.find(cards[i])==mp.end())
                mp[cards[i]]=i;
            else{
                int temp = i-mp[cards[i]];
                mp[cards[i]]=i;
                if(temp<ans || ans==-1){
                    ans = temp;
                }
            }
        }
        return ans+1;
    }
};