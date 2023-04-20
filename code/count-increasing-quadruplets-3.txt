class Solution {
public:
    class BIT {
    int n;
    vector<long long> v;
public:
    BIT(int sz) {
        n = sz;
        v.resize(n + 1);
    }
    long long sum(int k) {
        //sum till index k
        long long sum = 0;
        while (k > 0) {
            sum += v[k];
            k -= k & -k;
        }

        return sum;
    }
   void add(int k , int x) {

        while (k <= n) {
            v[k] += x;
            k += k & -k;
        }
    }

};
    long long countQuadruplets(vector<int>& nums) {
        int n=nums.size();
        
        long long ans=0;
        BIT t1(4005);
        for(int j=0;j<n;j++){
            BIT t2(4005);
            //intitally add all the elements from k to end so that we can later remove them while iterating
            for(int k = j+1;k<n;k++) t2.add(nums[k],+1);

            for(int k=j+1;k<n;k++){
                //fix the current k and remove it from the fenwick tree
                t2.add(nums[k],-1);
                if(nums[j] > nums[k]){
                    //calulate elements less than nums[k]
                    long long left = t1.sum(nums[k]);
                    //calculate elements greater than nums[j]
                    long long right = t2.sum(4002) - t2.sum(nums[j]);               

                    ans += left * right;
                }
            }
            //add nums[j] in tree so that we consider it when j moves to right
            t1.add(nums[j],+1);
        }

        return ans;
    }
};