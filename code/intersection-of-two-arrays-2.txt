typedef struct { int key; bool intersect; UT_hash_handle hh; } Map;

int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    Map *map = NULL, *elem, *tmp;
    int *result, len = 0;
    
    // Get the size of the smaller list, since the intersection can never be
    // larger than the smaller list.
    *returnSize = nums1Size < nums2Size? nums1Size: nums2Size;
    result = malloc(*returnSize * sizeof(int));
    
    // Populate the elements of nums1 into the hash table.
    for (int i = 0; i < nums1Size; i++) {
        elem = malloc(sizeof(Map));
        elem->key = nums1[i];
        elem->intersect = false;
        HASH_ADD_INT(map, key, elem);
    }

    // Go through nums2 and mark the common elements (same value) as intersecting.
    for (int i = 0; i < nums2Size; i++) {
        elem = NULL;
        HASH_FIND_INT(map, &nums2[i], elem);
        if (elem) {
            elem->intersect = true;
        }
    }
    
    // Iterate the hash table, and return only the intersecting elements.
    HASH_ITER(hh, map, elem, tmp) {
        if (elem->intersect) {
            result[len++] = elem->key;
        }
    }
    
    // In case the number of intersecting elements is smaller than the original
    // allocated size, reduce the buffer size by calling realloc.
    *returnSize = len;
    return realloc(result, sizeof(int) * len);
}