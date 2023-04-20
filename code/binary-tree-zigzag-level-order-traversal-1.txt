/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct Pair {
    struct TreeNode* node;
    int level;
};

struct Queue {
    struct Pair data[3000];
    int size;
    int i;
    int j;
};

void qpush(struct Queue* q, struct Pair p) {
    q->size ++;
    q->data[q->j] = p;
    q->j=(q->j+1)%3000;
}

struct Pair qpop(struct Queue* q) {
    struct Pair r;
    q->size--;
    r = q->data[q->i];
    q->i=(q->i+1)%3000;
    return r;
}

int qempty(struct Queue* q) {
    return q->size==0;
}

struct Result {
    int** r;
    int* cols;
    int size;
    int cap;
    
    int* cur;
    int cur_size;
    int cur_cap;
};

void flush(struct Result* r) {
    if (r->cur == NULL) {
        return;
    }
    if (r->size >= r->cap) {
        r->cap = (r->cap+1)*2;
        r->r = realloc(r->r, r->cap*sizeof(int*));
        r->cols = realloc(r->cols, r->cap*sizeof(int));
    }
    r->r[r->size] = r->cur;
    r->cols[r->size] = r->cur_size;
    r->size++;
    r->cur = NULL;
    r->cur_size = r->cur_cap = 0;
}

void add(struct Result* r, int x) {
    if (r->cur_size >= r->cur_cap) {
        r->cur_cap = (r->cur_cap+1)*2;
        r->cur = realloc(r->cur, r->cur_cap*sizeof(int));
    }
    r->cur[r->cur_size++] = x;
}

void reverse(int* data, int size) {
    int i;
    for (i = 0; i < size/2; i++) {
        int t = data[i]; data[i] = data[size-i-1]; data[size-i-1] = t;
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** zigzagLevelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes){
    struct Queue q;
    struct Result r;
    int level = 0, i;
    struct Pair c = {root, level};
    memset(&q, 0, sizeof(q));
    memset(&r, 0, sizeof(r));
    if (root) {
        qpush(&q, c);
    }
    while (!qempty(&q)) {
        struct Pair cur = qpop(&q);
        if (cur.level != level) {
            flush(&r);
        }
        add(&r, cur.node->val);
        if (cur.node->left) {
            struct Pair n = {cur.node->left, cur.level+1};
            qpush(&q, n);
        }
        if (cur.node->right) {
            struct Pair n = {cur.node->right, cur.level+1};
            qpush(&q, n);
        }
        level = cur.level;
    }
    flush(&r);
    
    *returnColumnSizes = r.cols;
    *returnSize = r.size;
    for (i = 1; i < r.size; i += 2) {
        reverse(r.r[i], r.cols[i]);
    }
    return r.r;
}