void next(int* nums, int numsSize, int k, int* i, int time){
    int now = 0;
    *i += 1;
    while( *i < numsSize ){
        if (k > nums[*i]){
            now++;
            next( nums, numsSize, nums[*i], i, now);
            if (now == time){
                return;
            }
        } else {
            return;
        }
    }
}

int totalSteps(int* nums, int numsSize){
    int ans = 0;
    int time = 0;
    int k = nums[0];
    int i = 1;
    while( i < numsSize ){
        if (k > nums[i]){
            time++;
            next(nums, numsSize, nums[i], &i, time);
        } else {
            if (time > ans){
                ans = time;
            }
            time = 0;
            k = nums[i];
            i++;
        }
    }
    if (time > ans){
        ans = time;
    }
    return ans;
}