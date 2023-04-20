int gcd(int a, int b)
{
    return b == 0 ? a : gcd(b, a % b);
}

int nthMagicalNumber(int n, int a, int b){
    long temp = a * b/ gcd(a, b), left = 2, right = 1e14, Mod = 1e9 + 7;
    while(left < right)
    {
        long mid = (left + right) / 2;
        if(mid/a + mid/b - mid/temp < n)
            left = mid + 1;
        else right = mid;
    }
    return right % Mod;
}