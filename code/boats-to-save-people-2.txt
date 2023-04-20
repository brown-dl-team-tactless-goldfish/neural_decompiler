int cmp(const void* a, const void* b) {
    return *(const int*) a - *(const int*) b;
}

int numRescueBoats(int* people, int peopleSize, int limit) {
    qsort(people, peopleSize, sizeof(int), cmp);
    int start = 0, end = peopleSize - 1, cnt = 0;
    while(start <= end) {
        cnt++;
        start = (people[start] + people[end] <= limit) ? start + 1 : start;
        end--;
    }
    return cnt;
}