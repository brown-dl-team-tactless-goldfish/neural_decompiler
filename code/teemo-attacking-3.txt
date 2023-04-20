int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration) {
    int res = 0, till = 0;
    for (int i = 0; i < timeSeriesSize; i++) {
        if (timeSeries[i] >= till)
            res += duration;
        else
            res += duration - (till - timeSeries[i]);
        till = timeSeries[i] + duration;
    }
    return res;
}