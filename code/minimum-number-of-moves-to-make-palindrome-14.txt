class Solution {
public:
    int minMovesToMakePalindrome(string s) {
        int count=0,te=0,counter=0;
        for(int j=0;j<s.length()/2;j++){
            int c=0;
            char temp=s[j];
            for(int i=s.size()-1-j;i>j;i--){
                if(s[i]==temp){
                    char t=s[i];
                    s.erase(s.size()-1-c-j,1);
                    s.insert(s.end()-j,t);
                    count+=c;
                    break;
                }else if(i==(j+1)){
                    te=j;
                    s.erase(s.begin()+j);
                    j--;
                    counter++;
                    break;
                }
              c++;
            }
         }
        if(counter!=0){
            count+=(s.size()/2)-te;
        }    
        return count;
    }
};