class Solution {
public:
    int subarrayBitwiseORs(vector<int>& A) {
        unordered_set<int> s;
        for(int i=0;i<A.size();i++){
            int j=i-1;
            int x=0,y=A[i];
            s.insert(y);
            while(j>=0 and x!=y){
                x|=A[j];
                y|=A[j];
                s.insert(y);
                j--;
            }
        }
        return s.size();
    }
};