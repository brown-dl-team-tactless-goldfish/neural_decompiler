class Solution {
public:
 

       
       //1.finfd first dip 
        
        //skipping last 
      
       //Jab tak age wala bda ho piche wala se incresing sequence ho tb tk i--
        
        
           //limit crossed koi number nhi mila return -1
        //find just next greater 
       //chlo abhi find krenge just next greater elemnt that previously find dip element 

        
   //swap krdo i j ko
   
      // i to j concatenate 
       
            
        
        ///piche se concatenate kro cause reverse is needed 

      
    
     int nextGreaterElement(int n) {
        string num = to_string(n);
        if (next_permutation(num.begin(), num.end())) {
            long res = stol(num);
            return res > INT_MAX ? -1 : res;
        } else {
            return -1;
        }
    }
};