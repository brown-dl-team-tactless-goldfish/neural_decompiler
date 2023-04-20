

int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration)
{
    int total = 0;
    
    int start_time = 0;
    int end_time = 0;
    
    int i=0;
    for(i=0; i<timeSeriesSize; i++)
    {
        start_time = timeSeries[i];
        
        if(start_time >= end_time)
        {
            end_time   = timeSeries[i] + duration;
            total      += end_time - start_time;     
        }
        else
        {
            total -= (end_time - start_time);
            end_time = timeSeries[i] + duration;
            total += end_time - start_time;
        }
        
    }
    return total;
}