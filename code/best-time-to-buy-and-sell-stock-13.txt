#include <limits.h>

#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))
#define MAX(X, Y) (((X) > (Y)) ? (X) : (Y))

int maxProfit(int *prices, int pricesSize)
{
    int max_price = 0;
    int min_price = INT_MAX;
    for (int i = 0; i < pricesSize; i++)
    {
        min_price = MIN(min_price, prices[i]);
        max_price = MAX(prices[i] - min_price, max_price);
    }
    return max_price;
}