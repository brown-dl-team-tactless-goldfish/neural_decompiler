typedef struct {
    int* dayPrice;/*[ 31-16 bits|15 - 0 bits] = [day | price] for saving space */
    int curIdx;
} StockSpanner;


StockSpanner* stockSpannerCreate() {
    StockSpanner* stock = (StockSpanner*)calloc(1, sizeof(StockSpanner));
    stock->dayPrice = (int*)calloc(1000, sizeof(int));
    return stock;
}

int stockSpannerNext(StockSpanner* obj, int price) {
    int dayCnt = 1;
    if(obj->dayPrice[obj->curIdx] == 0)
        obj->dayPrice[obj->curIdx] = (dayCnt << 16) | price;

    while(obj->curIdx && (price >= (obj->dayPrice[obj->curIdx - 1] & 0x0000FFFF)))
    {
        dayCnt = (obj->dayPrice[obj->curIdx - 1] >> 16) + (obj->dayPrice[obj->curIdx] >> 16);
        obj->dayPrice[obj->curIdx - 1] = (dayCnt << 16) | price;
        obj->dayPrice[obj->curIdx--] = 0;
    }
    obj->curIdx++;
    return dayCnt;
}

void stockSpannerFree(StockSpanner* obj) {
    free(obj->dayPrice);
    free(obj);
}