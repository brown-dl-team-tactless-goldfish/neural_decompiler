class Solution {
public:
    long long minimumDifference(vector<int>& A) {
      
      
      int N = A.size()/3;
      
        vector<long long>dp_left(A.size(),0);
        vector<long long>dp_right(A.size(),0);
        long long left_sum = 0;
        long long right_sum = 0;
        
        // Calculation for left
         priority_queue<int> pq_left;
        for (int i = 0; i < N; i++)
        {
            left_sum += A[i];
            pq_left.push(A[i]);
        }
        
        dp_left[N-1] = left_sum;
        
        for (int i = N; i < 2*N; i++)
        {
            int top = pq_left.top();
            int curr = A[i];
            
            if (curr < top)
            {
                pq_left.pop();
                pq_left.push(curr);
                left_sum -= top;
                left_sum += curr;
            }
            dp_left[i] = left_sum;
        }
        
        
        // calculation for right
        priority_queue<int,vector<int>,greater<int>> pq_right;
        for (int i = A.size()-1; i >=  2*N; i--)
        {
            right_sum += A[i];
            pq_right.push(A[i]);
        }
        
        dp_right[2*N] = right_sum;
        
        for (int i = 2*N-1; i >= N; i--)
        {
            int top = pq_right.top();
            int curr = A[i];
            
            if (curr > top)
            {
                pq_right.pop();
                pq_right.push(curr);
                right_sum -= top;
                right_sum += curr;
            }
            dp_right[i] = right_sum;
        }
        
        // Calculation of difference;
        
        // show_vector(dp_left);
        // show_vector(dp_right);
        long long answer = LLONG_MAX;
        for (int i = N-1; i < 2*N; i++ )
        {
            answer = min(answer,dp_left[i] - dp_right[i+1]);
        }
        
        return answer;
    }
};