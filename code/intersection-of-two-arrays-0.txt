typedef struct{ int key; bool intersect; UT_hash_handle hh;} Map;

int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    Map *map = NULL, *element, *tmp;
    int *result, len = 0;
    
    *returnSize = nums1Size < nums2Size? nums1Size: nums2Size;
    result = malloc(*returnSize * sizeof(int));
    
    for(int i=0; i < nums1Size; i++){
        element = malloc(sizeof(Map));
        element->key = nums1[i];
        element->intersect = false;
        HASH_ADD_INT(map, key, element);
    }
    
    for(int i=0; i < nums2Size; i++){
        element = NULL;
        HASH_FIND_INT(map, &nums2[i], element);
        if (element)
            element->intersect = true;
    }
    
    HASH_ITER(hh, map, element, tmp){
        if (element->intersect){
            result[len++] = element->key;
        }
    }
    
    *returnSize = len;
    return realloc(result, sizeof(int) * len);
}