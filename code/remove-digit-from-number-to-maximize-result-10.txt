class Solution {
public:
    string removeDigit(string number, char digit) {
        
        int n=number.length(),i;
        for(i=0;i<n-1;i++){
            if(number[i]==digit){
               if(number[i]<number[i+1]){
                   number.erase(number.begin()+i);
                   return number;
               }
            }
        }
        
        while(1){
            if(number[i]==digit){
                number.erase(number.begin()+i);
                break;
            }
            i--;
        }
        return number;
        
    }
};