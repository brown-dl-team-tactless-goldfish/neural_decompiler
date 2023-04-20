#define MAX_SIZE 10000

typedef struct {
    int* pingHistory;
    int head;
    int tail; 
} RecentCounter;

RecentCounter* recentCounterCreate() {
    RecentCounter* obj = malloc(sizeof(RecentCounter));
    obj -> pingHistory = calloc(10000, sizeof(int));
    obj -> head = 0;
    obj -> tail = 0;
    return obj;
}

int recentCounterPing(RecentCounter* obj, int t) {
    obj -> pingHistory[obj->head++] = t;
    
    for(; obj->tail < obj -> head; obj->tail++)
    {
        if((t-3000) <= obj -> pingHistory[obj->tail])
        {
            break;
        }
    }
    return obj->head-obj->tail;
}

void recentCounterFree(RecentCounter* obj) {
    free(obj->pingHistory);
    free(obj);
}