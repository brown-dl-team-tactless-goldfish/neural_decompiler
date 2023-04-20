class Solution {
public:
    vector<int> minOperations(string boxes) {
        int left=0,right=0;
        int n=boxes.length();
        int distance=0;
        for(int i=0;i<n;i++)
        {
            if(boxes[i]=='1')
            {   distance+=i;
                if(i==0)
                {
                    left+=1;
                    
                }
                else
                {
                    right+=1;
                }
            }
        }
        vector<int>result;
        result.push_back(distance);
        for(int i=1;i<n;i++)
        {
            result.push_back(result[i-1]+left-right);
            if(boxes[i]=='1')
            {
                left+=1;
                right-=1;
            }
            
        }
        return result;
        
    }
};