int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size,
                  int* returnSize) {
  int* map = malloc(sizeof(int) * 1000);
  int* res = malloc(sizeof(int) * 1000);
  int cnt = 0;

  for (int i = 0; i < nums1Size; i++) {
    map[nums1[i]] = 1;
  }
  for (int i = 0; i < nums2Size; i++) {
    if (map[nums2[i]] == 1) {
      res[cnt++] = nums2[i];
      map[nums2[i]] = 0;
    }
  }
  *returnSize = cnt;
  return res;
}