int hashtable[101] = {0};

int maximumPopulation(int** logs, int logsSize, int* logsColSize)
{
    memset(hashtable, 0x00, sizeof(hashtable));
    
    int i=0;
    for(i=0; i<logsSize; i++)
    {
        int birth_year = logs[i][0];
        int death_year = logs[i][1];
        
        int j=0;
        for(j=birth_year; j<death_year; j++)
        {
            hashtable[j - 1950] += 1;
        }
    }
    
    int max = 0;
    int max_pop_year = 0;
    
    for(i=100; i>=0; i--)
    {
        if(hashtable[i] >= max)
        {
            max = hashtable[i];
            max_pop_year = i + 1950;
        }
    }
    return max_pop_year;
}