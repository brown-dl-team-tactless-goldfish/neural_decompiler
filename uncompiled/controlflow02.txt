//! -O1

long f(const int* v, int n) {
    long sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += *((char*)v + i * sizeof(int));
    }
    return sum;
}
