class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        map<int,double>line;
        for(int i=0;i<position.size();i++){
            //we write -pos[i] since we want to traverse backwards while calculating count
            line[-position[i]]=(double)(target-position[i])/speed[i];
        }
        int count =0;
        double latest_time=0;
        for(auto i : line){
            if(i.second>latest_time){
                count++;
                latest_time=i.second;
            }
        }
        return count;
    }
};