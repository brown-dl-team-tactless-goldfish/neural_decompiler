int maxProfit(int* prices, int pricesSize) {
    int cumulativeGain = 0;
    int lastVal = prices[0];
    for (int i = 1; i < pricesSize; i++) {
        if (prices[i] > lastVal) {
            cumulativeGain += prices[i] - lastVal;
        }
        lastVal = prices[i];
    }
    return cumulativeGain;
}