struct hash_map
{
  int key;                   /* key */
  int value;                 /* value */
  UT_hash_handle hh;         /* makes this structure hashable */
};
typedef struct hash_map map;
map* ht = NULL;                 /* a NULL struct for hash map initialization */

void htAdd(int key, int value)
{
  map* s;
  HASH_FIND_INT(ht, &key, s);  /* id already in the hash? */
  if (s==NULL)
  {
    s = (map*)malloc(sizeof(map));
    s->key = key;
    HASH_ADD_INT(ht, key, s);  /* id: name of key field */
  }
  s->value = value;
}

map* htFind(int key)
{
    map* s;
    HASH_FIND_INT(ht, &key, s);  /* s: output pointer */
    return s;
}

void htCleanup()
{
    map* cur, *tmp;
    HASH_ITER(hh, ht, cur, tmp)
    {
        HASH_DEL(ht, cur);  /* delete it (users advances to next) */
        free(cur);            /* free it */
    }
}

void htPrint() {
    map* s;
    for(s=ht; s != NULL; s=(map*)(s->hh.next))
        printf("key %d:  value %d\n", s->key, s->value);
}

int* twoSum(int* nums, int numsS, int target) {
  int i, *r;
  map* hRes; /* hash find result */
  ht = NULL; /* initialize the hash map  */
  r = (int*)malloc(2* sizeof(int));

  for(i = 0; i<numsS; i++)
    htAdd(nums[i], i);

  //htPrint();
  
  for(i = 0; i<numsS; i++)
  {
    hRes = htFind(target- nums[i]);
    if(hRes && hRes->value != i)
    {
      r[0] = i + 1;
      r[1] = hRes->value + 1;
      return r;
    }
  }

  htCleanup();
  return NULL;
}