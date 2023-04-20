class FoodRatings
{
public:
    typedef pair<int, string> pi;
    unordered_map<string, set<pi>> mp;
    unordered_map<string, string> cs;
    unordered_map<string, int> rt;
    FoodRatings(vector<string> &foods, vector<string> &cuisines, vector<int> &ratings)
    {
        int n = foods.size();
        for (int i = 0; i < n; i++)
        {
            mp[cuisines[i]].insert({-ratings[i], foods[i]});
            cs[foods[i]] = cuisines[i];
            rt[foods[i]] = -ratings[i];
        }
    }

    void changeRating(string food, int newRating)
    {
        string c = cs[food];
        int r = rt[food];
        mp[c].erase({r, food});
        mp[c].insert({-newRating, food});
        rt[food] = -newRating;
    }

    string highestRated(string cuisine)
    {
        auto p = begin(mp[cuisine]);
        return p->second;
    }
};