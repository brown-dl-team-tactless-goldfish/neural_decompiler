#define SIZE 50
#define MAX(a, b) (((a) > (b)) ? (a) : (b))
typedef struct {
    int val1;
    int val2;
} Queue_Data;
Queue_Data queue[SIZE * SIZE];
Queue_Data EMPTY = {-2147483647, -2147483647};

typedef struct {
    Queue_Data *val;
    int head, tail, entries, size;
} Queue_struct;

int init_queue(Queue_struct *q, int size) {
    q->val = &queue[0];
    q->size = size;
    q->entries = q->head = q->tail = 0;
    return 1;
}

int queue_empty(Queue_struct *q) { return (q->entries == 0); }
int queue_full(Queue_struct *q) { return (q->entries == q->size); }

int enQueue(Queue_struct *q, int data1, int data2) {
    if (queue_full(q)) return -1;
    q->val[q->tail].val1 = data1;
    q->val[q->tail].val2 = data2;
    q->tail = (q->tail + 1) % q->size;
    q->entries++;
    return 1;
}

Queue_Data deQueue(Queue_struct *q) {
    if (queue_empty(q)) return EMPTY;
    Queue_Data data = {q->val[q->head].val1, q->val[q->head].val2};
    q->head = (q->head + 1) % q->size;
    q->entries--;
    return data;
}

int maxAreaOfIsland(int **grid, int gridSize, int *gridColSize) {
    int path[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    Queue_struct Q;
    init_queue(&Q, *gridColSize * gridSize);
    int ans = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < *gridColSize; j++) {
            if (grid[i][j] != 1) continue;
            int count = 1;
            enQueue(&Q, i, j);
            grid[i][j] = 0;
            while (!queue_empty(&Q)) {
                Queue_Data data = deQueue(&Q);
                for (int g = 0; g < 4; g++) {
                    int R = data.val1 + path[g][0], C = data.val2 + path[g][1];
                    if (R < gridSize && C < *gridColSize && R >= 0 && C >= 0 &&
                        grid[R][C] == 1) {
                        count++;
                        enQueue(&Q, R, C);
                        grid[R][C] = 0;
                    }
                }
            }
            ans = MAX(ans, count);
        }
    }
    return ans;
}