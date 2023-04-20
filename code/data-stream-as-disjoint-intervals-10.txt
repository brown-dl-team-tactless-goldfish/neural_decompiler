class SummaryRanges {
    map<int,int> start,end;
    unordered_map<int,int> mp;
public:
    SummaryRanges() {
    }
    
    void addNum(int i) {
        if(mp.find(i)!=mp.end()) return;
        int st = i,en = i;
        if(end.find(i-1)!=end.end()){
            st = end[i-1]; 
            end.erase(i-1); start.erase(st);
        }
        if(start.find(i+1)!=start.end()){
            en = start[i+1]; 
            end.erase(en); start.erase(i+1);
        }
        start[st] = en; end[en] = st; mp[i]++;
    }
    
    vector<vector<int>> getIntervals() {
         vector<vector<int>> re;
         for(auto&[x,y]:start) re.push_back({x,y});
        return re;
    }
};