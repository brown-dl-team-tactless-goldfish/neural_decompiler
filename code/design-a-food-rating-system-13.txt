class FoodRatings {
private:
    struct cmp{
        bool operator()(const pair<int,string> &p1,const pair<int,string> &p2) const{
            return p1.first == p2.first ? p1.second < p2.second : p1.first > p2.first;
        }
    };    
    
    unordered_map<string,unordered_map<string,int>> mp1; // cuisine -> {food, rating}
    unordered_map<string,set<pair<int,string>,cmp>> mp2; // cuisine -> {rating,food} - in decreasing order of rating and incr. order of name
    unordered_map<string,string> mp3; // food -> cuisine    
public:    
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for(int i=0;i<foods.size();i++){
            auto &mp = mp1[cuisines[i]];
            mp[foods[i]] = ratings[i];       
            
            auto &st = mp2[cuisines[i]];
            st.insert({ratings[i],foods[i]});            
            
            mp3[foods[i]] = cuisines[i];
        }
    }
    
    void changeRating(string food, int newRating) {
        auto &name = mp3[food];
        auto &rating = mp1[name][food];
        
        auto &st = mp2[name];
        st.erase({rating,food});
        st.insert({newRating,food});
        
        mp1[name][food] = newRating;
    }
    
    string highestRated(string cuisine) {
        return (*(mp2[cuisine].begin())).second;
    }
};