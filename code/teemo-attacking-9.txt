int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration)
{
    int total = 0;
    for(int i = 0; i<timeSeriesSize-1; i++){
        if(timeSeries[i] + duration > timeSeries[i+1]) total += timeSeries[i+1] - timeSeries[i];
        else total += duration;
    }
    return total + duration;
}