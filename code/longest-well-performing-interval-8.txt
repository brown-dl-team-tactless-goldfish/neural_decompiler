class Solution {
public:
    int longestWPI(vector<int>& hours) {
        unordered_map<int,int> m;
        int res=0;
        int sum=0;
        for(int i=0;i<hours.size();i++)
        {
		//we are basically converting it into a maximum subarray with positive product
            sum+=(hours[i]>8) ? 1 : -1;
            if(sum>0){
                //from starting we have found a largest positive product
                res=i+1;
            }
            else{
                //we check if there is a prefix sum of sum-1
                //becoz from that index to curr index we have subarray of sum 1
                if(m.find(sum-1)!=m.end())
                {
                    res=max(res,i-m[sum-1]);
                }
                //we need to have the first index where we got sum
                //bcoz it  leads to the largest length
                if(m.find(sum)==m.end())
                {
                    m[sum]=i;
                }
            }
        }
        return res;
    }
};