int cmp(const void* a, const void* b) {
    return *(const int*) a > *(const int*) b;
}

int findContentChildren(int* g, int gSize, int* s, int sSize) {
    qsort(g, gSize, sizeof(int), cmp);
    qsort(s, sSize, sizeof(int), cmp);
    
    int sidx = 0, gidx = 0, cnt = 0;
    while(sidx < sSize && gidx < gSize) {
        if(s[sidx] < g[gidx]) {
            sidx++;
        } else {
            sidx++;
            gidx++;
            cnt++;
        }
    }
    return cnt;
}