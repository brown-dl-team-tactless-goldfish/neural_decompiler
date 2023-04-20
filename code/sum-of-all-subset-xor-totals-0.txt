void backtrack(int* nums, int numsSize, int tar, int idx, int* cnt) {
    if (idx == numsSize) {
        return;
    } else {
        for (int i = idx; i < numsSize; i++) {
            tar ^= nums[i];
            (*cnt) += tar;
            dfs(nums, numsSize, tar, i + 1, cnt);
            tar ^= nums[i];
        }
    }
}

int subsetXORSum(int* nums, int numsSize) {
    int cnt = 0;
    for (int i = 0; i < numsSize; i++) {
        cnt += nums[i];
        backtrack(nums, numsSize, nums[i], i + 1, &cnt);
    }
    return cnt;
}