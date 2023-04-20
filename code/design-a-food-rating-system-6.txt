class FoodRatings {
    map<string,int> rat;
    map<string,string> cusi;
    map<string,map<int,set<string>,greater<int>>> mp;
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        int n = foods.size();
        
        for(int i = 0 ; i < n ;i++){
            mp[cuisines[i]][ratings[i]].insert(foods[i]);
            rat[foods[i]] = ratings[i];
            cusi[foods[i]] = cuisines[i];
        }
    }
    
    void changeRating(string food, int newRating) {
        string cu = cusi[food];
        mp[cu][newRating].insert(food);
        mp[cu][rat[food]].erase(food);
        rat[food] = newRating;
    }
    
    string highestRated(string cuisine) {
        for(auto x : mp[cuisine]){
            for(auto z : x.second){
                return z;
            }
        }
        return "a";
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */