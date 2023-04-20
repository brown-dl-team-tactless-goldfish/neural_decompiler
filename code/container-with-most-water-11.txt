int maxArea(int* height, int heightSize)
{
    int i = 0, j = heightSize - 1;
    int max = INT_MIN;
    while (i < j) {
        int cap = (j - i) * fmin(height[i], height[j]);     
        max = fmax(max, cap);        
        if (height[i] > height[j])
            j--;
        else
            i++;
    }
    return max;
}