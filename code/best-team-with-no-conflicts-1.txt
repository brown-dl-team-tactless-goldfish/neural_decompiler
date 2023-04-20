#define max(a, b) a > b ? a : b
typedef struct {
    int score;
    int age;
} player;

int cmp(const void* a, const void* b) {
    player* pa = (player*)a;
    player* pb = (player*)b;
    if (pa->score != pb->score)
        return pa->score - pb->score;
    return pa->age - pb->age;
}

int bestTeamScore(int* scores, int scoresSize, int* ages, int agesSize) {
    int result = 0;
    int dp[scoresSize];
    memset(dp, 0, sizeof dp);
    player players[scoresSize];
    for (int i = 0; i < scoresSize; i++) 
    {
        players[i].score = scores[i];
        players[i].age = ages[i];
    }
    qsort(players, scoresSize, sizeof(player), cmp);
    for (int i = 0; i < scoresSize; i++) 
    {
        dp[i] = players[i].score;
        for (int j = 0; j < i; j++) 
        {
            if (players[j].age <= players[i].age)
                dp[i] = max(dp[i], dp[j] + players[i].score);
        }
        result = max(result, dp[i]);
    }
    return result;
}