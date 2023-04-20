class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();
        map<int,int> allsums;  //Count all sums 
        for(int i=0;i<nums.size()/2;i++){
            allsums[nums[i]+nums[n-i-1]]++;
        }
        vector<int> omove(2*limit+2,0),tmove(2*limit+2,0);  //Maximum sum possible is 2*limit and minimum sum = 2
        
        for(int i=0;i<n/2;i++){
            int mis = min(nums[i],nums[n-i-1]) + 1;  // If pair is 2,3 and limit=5 - In one move this pair can acheive sum from 3 to 8
            int mas = max(nums[i],nums[n-i-1]) + limit;  // mis = 3, mas = 8
            omove[mis]++;      // mark omove[3]=1 and 
            omove[mas+1]--;    // omove[9] = -1 
            tmove[mas+1]++;     //Now rest of the range takes 2 moves always no matter what
            tmove[2*limit+1]--; // i.e 2 to 2 and 9 to 10(2*limit)
            tmove[2]++;      // Do the same in tmove
            tmove[mis]--;
        }        
        //Continuing with above ex, omove[3]=1 and omove[9] = -1
        // Cummulative sum will make all elements from 3 to 8 as 1 i.e there is one pair which will make this sum
        // In summary every element of the array will tell how many pairs require one move to get required sum in omove
        // Same in tmove (i.e 2 moves)
        for(int i=1;i<omove.size();i++){
            omove[i]+=omove[i-1];
            tmove[i]+=tmove[i-1];
        }
        // In omove we have to remove sums that have already been acheived i.e in omove we have counted 5 (2+3). Remove that
        for(auto i:allsums){            
            omove[i.first]-=i.second;
        }                
        int mm=INT_MAX;
        // min(Sum of omve and 2*tmove) is answer :)
        for(int i=2;i<omove.size()-1;i++){            
            mm = min(omove[i]+2*tmove[i],mm);
        }
        return mm;
    }
};