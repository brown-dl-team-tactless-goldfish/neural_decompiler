#define max(a,b) ((a)>(b)?(a):(b))
typedef struct  {
    int *begin, *end, size, *front, *back;
} queue;
int maxsize;
queue *que_create(void);
void que_push(queue*, int);
int que_pop(queue*);
int que_isempty(queue*);
void que_resize(queue*);
int que_front(queue*);
queue *que_create(void){
    queue *que = malloc(sizeof(queue));
    que->size = 24;
    que->begin = malloc(sizeof(int) * que->size);
    que->end = que->begin + que->size;
    que->front = que->back = que->begin;
    return que;
}

void que_push(queue* que, int val) {
    *((que->back)++) = val;
    if (que->back == que->end)
        que->back = que->begin;
    if (que->back == que->front)
        que_resize(que);
}

int que_pop(queue* que) {
    int tmp = *(que->front);
    if (++(que->front) == que->end)
        que->front = que->begin;
    return tmp;
}

int que_isempty(queue* que) {
    return que->front == que-> back;
}

void que_resize(queue* que) {
    int frontdis = que->front - que->begin;
    que->begin = realloc(que->begin, sizeof(int) * ((que->size) *= 2));
    que->end = que->begin + que->size;
    que->front = que->begin + frontdis;
    int *s, *t;
    for (s = que->begin, t = s + (que->size / 2); s != que->front;)
        *(t++) = *(s++);
    que->back = t;
}

int que_front(queue* que) {
    return *(que->front);
}
int isnear(char *a, char *b) {
    int count = 0;
    while (*a)
        if (*a++ != *b++)
            ++count;
    return count == 1;
}

typedef struct a{
    int val;
    struct a *next;
}node;

void add_node(node **a,int val) {
    while (*a)
        a = &((*a)->next);
    *a = malloc(sizeof(node));
    (*a)->val = val;
    (*a)->next = NULL;
}
void add_to_list(int ***list, int *listSize, int len, int onesol[]) {
    *list = realloc(*list, sizeof(int*) * (*listSize + 1));
    int *now = (*list)[*listSize] = malloc(sizeof(int) * len);
    for (int i = 0; i < len; ++i)
        now[i] = onesol[i];
    ++(*listSize);
}
void dfs(node **next, int now, int dep, int final, int ***list, int *listSize, int onesol[]) {
    onesol[dep-1] = now; 
    if (dep == final) {
        add_to_list(list, listSize, final, onesol);
        return;
    }
    node * cur= next[now];
    while (cur) {
        dfs(next, cur->val, dep+1, final, list, listSize, onesol);
        cur = cur->next;
    }
}

void push_ans(char****res, char *beginWord, char **words, int wordsSize, int *returnSize, int **returnColomnSizes, int * newsolution, int solen) {
    //resize everything
    if (maxsize == *returnSize + 1) {
        maxsize *= 2;
    *res = realloc(*res, sizeof(char**) * maxsize);
    *returnColomnSizes = realloc(*returnColomnSizes, sizeof(int) * maxsize+100);    
     }
    (*returnColomnSizes)[*returnSize] = solen;
    char **now = (*res)[*returnSize] = malloc(sizeof(char *) * solen);
    now[0] = beginWord;
    for (int i = 1; i<solen; i++)
        now[i] = words[newsolution[i-1]];
    ++(*returnSize);
}

void gene_ans(char****res, char *beginWord, char **words, int wordsSize, int *returnSize, int **returnColomnSizes,
              int l, int lsize, int r, int rsize, node **next) {
    int **listl=NULL, **listr=NULL, listlSize = 0, listrSize = 0;
    int *onesol = malloc(sizeof(int) * max(lsize,rsize));
    int *newsolution = malloc(sizeof(int) * (lsize+rsize));
    dfs(next, l, 1, lsize, &listl, &listlSize, onesol);
    dfs(next, r, 1, rsize, &listr, &listrSize, onesol);
    for (int i = 0; i < listlSize; ++i)
        for (int j = 0; j < listrSize; ++j) {
            int pos = 0;
            for (int k = lsize-1; k>=0; --k,++pos)
                newsolution[pos] = listl[i][k];
            for (int k = 0; k < rsize; ++k,++pos)
                newsolution[pos] = listr[j][k];
            push_ans(res, beginWord, words, wordsSize, returnSize, returnColomnSizes, newsolution, lsize+rsize+1);
        }
    free(onesol); free(newsolution);
}
char *** findLadders(char * beginWord, char * endWord, char ** words, int wordsSize, int* returnSize, int** returnColumnSizes){
    maxsize = 1;
    char ***res = malloc(0);
    *returnColumnSizes = malloc(0);
    *returnSize = 0;
    // find terminate
    int terminate = -1;
    for (int i = 0; i < wordsSize; ++i)
        if (strcmp(words[i], endWord) == 0)
            terminate = i;
    if (terminate == -1)
        return res;
    // list (result)
    node ** next = calloc(wordsSize , sizeof(node*));
    // direct result
    if (isnear(beginWord, endWord)) {
        int *tmp = malloc(sizeof(int));
        tmp[0] = terminate;
        push_ans(&res, beginWord, words, wordsSize, returnSize, returnColumnSizes,tmp,2);
        return res;
    }
    // creatqueue;
    queue *que1 = que_create(), *que2 = que_create();
    // status (1 for l, 2 for r, 3 for encounter)
    int *stat = calloc(wordsSize, sizeof(int));
    int *lock = calloc(wordsSize, sizeof(int));
    //push all node near beginword
    for (int i = 0; i < wordsSize; ++i)
        if (isnear(beginWord, words[i])) {
            que_push(que1, i);
            stat[i] = 1;
        }
    // push terminate to que2
    que_push(que2, terminate); stat[terminate] = 2;
    que_push(que1, -1); que_push(que2, -1);
    int cur, enconter = 0, lenl = 1, lenr = 1; 
    //till encounter or no path
    while (que_front(que1) != -1 && que_front(que2) != -1) {
        //deal que2
        while ((cur = que_pop(que2)) != -1)  {
            for (int i = 0; i < wordsSize; ++i)
                if (isnear(words[i],words[cur])) {
                    if (stat[i]==0) {
                        if (!lock[i]) {que_push(que2, i); lock[i] = 1;}
                        add_node(&next[i], cur);
                    }
                    else if (stat[i] == 1) {
                        enconter = 1;
                        gene_ans(&res, beginWord, words, wordsSize, returnSize, returnColumnSizes, i, lenl, cur, lenr, next);
                    }
                }
        }
        que_push(que2, -1);
        ++lenr;
        if (enconter)
            return res;
         while ((cur = que_pop(que2))!= -1) {
            stat[cur] = 2;
            que_push(que2, cur);
        }
        que_push(que2, -1);
        //deal que1
        while ((cur = que_pop(que1)) != -1)  {
            for (int i = 0; i < wordsSize; ++i)
                if (isnear(words[i],words[cur])) {
                    if (stat[i]==0) {
                        if (!lock[i]) {que_push(que1, i); lock[i] = 1;}
                        add_node(&next[i], cur);
                    }
                    else if (stat[i] == 2) {
                        enconter = 1;
                        gene_ans(&res, beginWord, words, wordsSize, returnSize, returnColumnSizes, cur, lenl, i, lenr, next);
                        if (*returnSize == 10)
                            return res;
                    }
                }
        }
        que_push(que1, -1);
        ++lenl;
        while ((cur = que_pop(que1))!= -1) {
            stat[cur] = 1;
            que_push(que1, cur);
        }
        if (enconter)
            return res;
        que_push(que1, -1);
    }
    return res;
}