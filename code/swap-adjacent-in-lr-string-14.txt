class Solution {
public:
   bool canTransform(string start, string end) {
       int n = start.size();
       int count = 0; //counting X, if they are different simply return false.
       for(int i = 0; i < n; i++){
           if(start[i] == 'X') count++;
           if(end[i] == 'X') count--;
       }
       if(count != 0) return false;
       
       int i = 0, j = 0;
       while(i < n && j < n){
           while(i < n && start[i] == 'X') i++;
           while(j < n && end[j] == 'X') j++;
           
           
           
           if(start[i] != end[j]) return false;
           if(start[i] == 'L' && i < j) return false;
           if(start[i] == 'R' && i > j) return false;
           i++;
           j++;
       }
       return true;
   }
};