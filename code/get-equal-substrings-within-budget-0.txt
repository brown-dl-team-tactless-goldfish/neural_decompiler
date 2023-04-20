int equalSubstring(char * s, char * t, int maxCost){
    int n = strlen(s);
    char* difference = malloc(n * sizeof(char));
    for(int i = 0; i < n; i++){
        difference[i] = abs(s[i] - t[i]);
    }
    
    int max = 0;
    int sum = 0;
    int l = 0, r;
    for(r = 0; r < n; r++){
        sum += difference[r];
        if(sum > maxCost){
            max = fmax(max, r - l);
            while(sum > maxCost){                
                sum -= difference[l];
                l++;
            }
        }
    }
    max = fmax(max, r - l);
    return max;
}