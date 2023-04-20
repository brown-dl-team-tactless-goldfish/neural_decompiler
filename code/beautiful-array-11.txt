class Solution {
public:
    vector<int> beautifulArray(int n) {
        vector<int> ff = {1};
        int n1 = 2;
        while((int)(ff.size()) < n){
            vector<int> odd;
            vector<int> even;
            // compute odd
            for(int i=0;i<(int)ff.size();i++){
                if((2*ff[i]) - 1 <= n1){
                    odd.push_back(2*(ff[i])-1);  
                }
            }
            // compute even
            for(int i=0;i<(int)ff.size();i++){
                if((2*ff[i]) <= n1){
                    even.push_back(2*(ff[i]));  
                }
            }
            // add both
            ff.clear();
            for(auto it : odd){
                ff.push_back(it);
            }
            for(auto it : even){
                ff.push_back(it);
            }
            n1+=1;
        }
        return ff;
    }
};