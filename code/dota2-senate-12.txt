class Solution {
public:
    string predictPartyVictory(string senate) {
        int erase_R = 0;
        int erase_D = 0;
        int count_R = 0;
        int count_D = 0;
        for(auto& s : senate){
            if(s == 'R') count_R++;
            else count_D++;
        }
        while(count_D && count_R){ 
            for(int i = 0;i < senate.size();i++){
                if(erase_R != 0 && senate[i] == 'R'){
                    erase_R--;
                    count_R--;
                    senate[i] = ' ';
                }else if(erase_D != 0 && senate[i] == 'D'){
                    erase_D--;
                    count_D--;
                    senate[i] = ' ';
                }else if(senate[i] == 'R'){
                    erase_D++;
                }else if(senate[i] == 'D'){
                    erase_R++;
                }
            }
        }
        if(count_D == 0) return "Radiant";
        return "Dire";
    }
};