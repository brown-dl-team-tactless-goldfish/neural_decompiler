class TweetCounts {
    unordered_map<string,multiset<int>>m;
public:
    TweetCounts() {
        
    }
    
    void recordTweet(string tweetName, int time) {
        m[tweetName].insert(time);
    }
    
    vector<int> getTweetCountsPerFrequency(string freq, string tweetName, int start, int end) {
        int count =freq=="minute"?60:freq=="hour"?3600:86400;
        int prev=0;
        vector<int>ans;
        while(true){
            int val=0;
            for(auto it=m[tweetName].lower_bound(min(end,start));it!=m[tweetName].upper_bound(min(end,start+count-1));it++){
                val++;
            }
            ans.push_back(val);
            prev=val;
            start+=count;
            if(start>end){
                break;
            }
        }
        return ans;
    }
};

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts* obj = new TweetCounts();
 * obj->recordTweet(tweetName,time);
 * vector<int> param_2 = obj->getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */