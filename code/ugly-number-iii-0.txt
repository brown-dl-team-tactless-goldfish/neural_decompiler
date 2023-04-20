long gcd(long a, long b) {
    return a ? gcd(b % a, a) : b;
}

long lcm(long a, long b) {
    return a * b / gcd(a, b);
}

int uglyNumbers(long m, long a, long b, long c) {
    long lcmab = lcm(a, b);
    long lcmac = lcm(a, c);
    long lcmbc = lcm(b, c);
    long lcmabc = lcm(lcmab, c);
    return (int)(m / a + m / b + m /c - m / lcmab - m / lcmac - m / lcmbc + m / lcmabc);
}

int nthUglyNumber(int n, int a, int b, int c){
    int left = 1, right = 2e9;
    while(left < right) 
    {
        int mid = left + (right - left) / 2;
        if (uglyNumbers(mid, a, b, c) >= n)
            right = mid;
        else
            left = mid + 1;
    }
    return left;
}