class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        sort(tasks.begin(), tasks.end()); 
        sort(workers.begin(), workers.end()); 
        
        auto fn = [&](int k) {
            int p = pills; 
            multiset<int> st(workers.end()-k, workers.end()); 
            for (int i = k-1; i >= 0; --i) {
                int task = tasks[i]; 
                if (task <= *(st.rbegin())) st.erase(prev(st.end())); 
                else if (task <= *st.rbegin() + strength && p) {
                    --p; 
                    auto it = st.lower_bound(task - strength); 
                    st.erase(it); 
                } 
                else return false; 
            }
            return true; 
        }; 
        
        int lo = 0, hi = min((int)tasks.size(), (int)workers.size()); 
        while (lo < hi) {
            int mid = lo + (hi - lo + 1)/2; 
            if (fn(mid)) lo = mid; 
            else hi = mid - 1; 
        }
        return lo; 
    }
};