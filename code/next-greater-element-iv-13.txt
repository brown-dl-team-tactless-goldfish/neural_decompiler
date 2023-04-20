 vector<int> secondGreaterElement(vector<int>& nums) {
       vector<int> ans(nums.size(),-1);
        
        stack<int> s1,s2,tmp;
        
        for(int i=0;i<nums.size();i++){
            //update ans
            while(!s2.empty() && nums[s2.top()]<nums[i]){
                ans[s2.top()]=nums[i];
                s2.pop();
            }
            //if find first max go for second so push it to the s2 
            while(!s1.empty() && nums[s1.top()]<nums[i]){
                tmp.push_back(s1.top());
                s1.pop();
            }
            //this while is becoz we want all elm in decresing order
            while(!tmp.empty()){
                s2.push_back(tmp.top());
                tmp.pop();
            }
            s1.push_back(i);
        }
        return ans;
    }
	//code by sachin