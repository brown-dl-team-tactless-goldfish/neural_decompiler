int maxProfit(int* prices, int pricesSize){
int ret = 0;
    for (int p = 1; p < pricesSize; ++p) 
      ret += prices[p] - prices[p - 1]>0?prices[p] - prices[p - 1]:0;    
    return ret;
}