class Solution {
public:
    using ll = long long ;
    int n ;
    vector<ll>score ;
    int edgeScore(vector<int>& edges) {
        n = edges.size() ;
        score.resize(n,0) ;
        
        for(int i = 0 ; i < n ; ++i ) score[edges[i]] += i*1LL ;
        ll target = *max_element(begin(score),end(score)) ;
        for(int i = 0 ; i < n ; ++i ) if(score[i] == target) return i ;
        
        
        return -1 ;
    }
};