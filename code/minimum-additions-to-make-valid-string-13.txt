class Solution {
public:
    int addMinimum(string word) {
        string val = "abc";
        int n = word.length(),i=0,c=0;
        string str1,str2;
        
        while(i<n){
            if(i+2<n)
                str1 = word.substr(i,3);
            if(i+1<n)
                str2 = word.substr(i,2);
            
            if(i+2 < n && str1 == "abc"){
                i+=3;
            }
            else if(i+1<n  &&  (( str2 == "ab") || (str2 == "bc") || (str2== "ac") )  ){
                    i+=2;
                    c++;
            }
            else{
                c+=2;
                i++;
            }
        }
        return c;
    }
};