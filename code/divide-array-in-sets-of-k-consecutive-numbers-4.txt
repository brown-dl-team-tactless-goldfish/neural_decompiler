class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) 
    {
        if(nums.size()%k!=0)
            return false;
        map<int,int> count;
        map<int,int>::iterator it;
        int freq;
        for(int &i:nums)			//Store the count of all numbers sorted.
            count[i]++;
        for(it=count.begin();it!=count.end();it++)	//Start with the smallest number.
            if(it->second)		//If the count of smallest integer is non 0 check if next k numbers exist and have atleast same frequency.
            {
                freq=it->second;
                for(int i=0;i<k;i++)				//Checks for the next k-1 numbers.
                    if(count[it->first+i]<freq) //We are unable to find ith consecutive number to the smallest(starting number) with atleast same frequency.
                        return false;
                    else
                        count[it->first+i]-=freq;       //Reduce the count of the numbers used.
            }
        return true;
    }
};