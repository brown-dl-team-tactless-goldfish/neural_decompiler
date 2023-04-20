

char slowestKey(int* releaseTimes, int releaseTimesSize, char * keysPressed)
{
    char max_key = 0;
    int max_duration = 0;
    
    int i=0;
    
    for(i=0; i<releaseTimesSize; i++)
    {
        int cur_duration;
        if(i==0)
        {
            cur_duration = releaseTimes[i] - 0;
        }
        else
        {
            cur_duration = releaseTimes[i] - releaseTimes[i - 1];
        }
        
        if(cur_duration == max_duration)
        {
            if(keysPressed[i] >= max_key)
            {
                max_key = keysPressed[i];
            }
            max_duration = cur_duration;
        }
        else if(cur_duration > max_duration)
        {
            max_key = keysPressed[i];
            max_duration = cur_duration;
        }
    }
    
    return max_key;
}