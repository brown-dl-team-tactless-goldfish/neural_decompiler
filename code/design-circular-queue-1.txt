typedef struct {
    int front;
    int rear;
    int size;
	
    int *data;
} MyCircularQueue;

bool myCircularQueueIsFull(MyCircularQueue* obj);
bool myCircularQueueIsEmpty(MyCircularQueue* obj);
MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue *res = (MyCircularQueue*)malloc(sizeof(MyCircularQueue));
    res->front = 0;
    res->rear = 0;
    res->size = k+1;
    res->data = (int*)malloc(sizeof(int)*(k+1));
    
    return res;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if(myCircularQueueIsFull(obj)) return false; //가득참
    
    obj->data[++(obj->rear)%obj->size] = value;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if(myCircularQueueIsEmpty(obj)) return false;
    
    obj->front +=1;
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    return myCircularQueueIsEmpty(obj)? -1 : obj->data[(obj->front+1)%obj->size];
}

int myCircularQueueRear(MyCircularQueue* obj) {
    return myCircularQueueIsEmpty(obj)? -1 : obj->data[obj->rear%obj->size];
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    return obj->front%obj->size==obj->rear%obj->size;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    return obj->front%obj->size==(obj->rear+1)%obj->size;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    free(obj->data);
    free(obj);
}