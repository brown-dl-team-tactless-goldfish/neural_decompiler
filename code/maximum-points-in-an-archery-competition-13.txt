class Solution {
public:
    vector<int> maximumBobPoints(int numArrows, vector<int>& aliceArrows) {
        vector<int>v;
        int maxi=0;
        for(int i=0; i<(1<<12); i++){
            int n=numArrows, cnt=0;
            vector<int>temp(12, 0);
            for(int j=11; j>=0; j--){
                if(i&(1<<j)){
                    if(n>aliceArrows[j]){
                        n-=(aliceArrows[j]+1);
                        temp[j]=(aliceArrows[j]+1);
                    }
                }
            }
            for(int j=0; j<12; j++){
                if(i&(1<<j)){
                    temp[j]+=n;
                    break;
                }
            }
            for(int j=0; j<12; j++){
                if(temp[j]>aliceArrows[j]){cnt+=j;}
            }
            if(cnt>maxi){
                maxi=cnt;
                v=temp;
            }
        }
        return v;
    }
};