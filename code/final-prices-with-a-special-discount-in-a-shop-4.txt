

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* finalPrices(int* prices, int pricesSize, int* returnSize){
    int j;
    int discElement;
    *returnSize = pricesSize;
    int *result = (int*)malloc(sizeof(int)*pricesSize);
    for(int i=0; i<pricesSize-1; i++){
        for(j=i+1; j<pricesSize; j++){
            if(prices[j]<=prices[i]){
                result[i] = prices[i]-prices[j];
                break;
            }
            else{
                result[i] = prices[i];
                result[pricesSize-1]= prices[pricesSize-1];
            }
        }
    }
    return result;
}