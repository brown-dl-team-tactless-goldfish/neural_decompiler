typedef struct BrowserHistory{
    char *val;
    struct BrowserHistory *next,*prev;
} BrowserHistory;

BrowserHistory *curr;

BrowserHistory* browserHistoryCreate(char * homepage) {
    BrowserHistory *p=(BrowserHistory*)malloc(sizeof(BrowserHistory));
    p->val=homepage;
    p->prev=p->next=NULL;
    return curr=p;
}

void browserHistoryVisit(BrowserHistory* obj, char * url) {
    obj=curr,obj->next=browserHistoryCreate(url),obj->next->prev=obj;
}

char * browserHistoryBack(BrowserHistory* obj, int steps) {
    while(steps--) curr=(curr->prev==NULL)?curr:curr->prev;
    return curr->val;
}

char * browserHistoryForward(BrowserHistory* obj, int steps) {
    while(steps--) curr=(curr->next==NULL)?curr:curr->next;
    return curr->val;
}

void browserHistoryFree(BrowserHistory* obj) {
    free(obj);
}