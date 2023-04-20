class Solution {
public:
    void addPrimeFactors(set<int>&st, int n)
    {
        int divisor = 2;
        long long ans = 0;
        while(n > 1)
        {
            if (n % divisor == 0) 
            {
                st.insert(divisor);
                n = n / divisor;
            }
            else divisor++;
        }
    }
    int distinctPrimeFactors(vector<int>& nums) 
    {
        set<int>st;
        for (int num : nums) addPrimeFactors(st, num);
        return st.size();
        
    }
};