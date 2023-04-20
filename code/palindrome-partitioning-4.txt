bool isPalin(char* s, int end);
void helper(char* s, char*** ret, int** colS, int* retS, char** cur, int k );

char*** partition(char* s, int** colS, int* retS)
{
  *retS = 0;
  if(s == NULL || !strcmp(s, "")) return NULL;

  /* I know ... I hate static mem alloc as well */
  *colS = (int*)malloc(sizeof(int)*500);
  char*** ret = (char***)malloc(sizeof(char**) * 500);
  int len = strlen(s)+1;

  char** cur = (char**)malloc(sizeof(char*) * 500);
  for(int i = 0; i<500; i++)
    cur[i] = (char*)malloc(len);

  /* backtracking starting from s[0] */
  helper(s, ret, colS, retS, cur, 0);

  return ret;
}

void helper(char* s, char*** ret, int** colS, int* retS, char** cur, int k )
{
  /* termination if already at the end of string s
     we found a partition */
  if(*s == 0)
  {
    ret[*retS] = (char**)malloc(sizeof(char*)*k);
    for(int i = 0; i<k; i++)
    {
      ret[*retS][i] = (char*)malloc(strlen(cur[i]) + 1);
      strcpy(ret[*retS][i], cur[i]);      
    }
    (*colS)[(*retS)++] = k;
    return;
  }

  /* explore next */
  int len = strlen(s);
  for(int i = 0; i < len; i++)
  {
    if(isPalin(s, i))
    {
      /* put it into the cur list  */
      strncpy(cur[k], s, i+1);
      cur[k][i+1] = '\0';
      
      /* backtracking */
      helper(s+i+1, ret, colS, retS, cur, k+1);
    }
  }
}

bool isPalin(char* s, int end)
{
  /* printf("error: start %d, end %d\n", start, end); */
  if(end < 0)          return false;
  int start = 0;
  while(end > start)
  {
    if(s[start] != s[end]) return false;
    start++;   end--;
  }
  return true;
}