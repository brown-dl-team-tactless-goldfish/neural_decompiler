class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int P) {
        sort(tokens.begin(), tokens.end());
        int score = 0, max_score = 0, low = 0, high = tokens.size()-1;
        while (low <= high) {
            
            if (tokens[low] <= P) {
                P -= tokens[low];
                score++;
                max_score = max(max_score, score);
                low++;
            }
            
            else if (score >= 1) {
                P += tokens[high];
                score--;
                high--;
            }
            else
                break;
        }
        return max_score;
    }
};