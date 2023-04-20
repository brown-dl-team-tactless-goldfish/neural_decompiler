#define MAX_SIZE 1000001
int hashtable[MAX_SIZE] = {-1};

void insert_heap(int heap[], int element, int n)
{    
    int i = n;   
    while(i>1 && element > heap[i/2])
    {
        heap[i] = heap[i/2];
        i = i/2;
    }
    heap[i] = element;
}

int delete_heap(int heap[], int * heap_index)
{
    int tmp = heap[*heap_index];
    int del_element = heap[1];

    heap[1] = tmp;
    
    *heap_index = *heap_index - 1;
    int i = 1;
    int j = i*2;
    while(j <= *heap_index)
    {
        
        if(j+1 <= *heap_index)
        {   

            if(heap[j+1] > heap[j]) //Compare both the childs of root
            {
                j = j+1;
            }
        }
        
        if(heap[j] > tmp)   //Adjust the tmp
        {

            int tmp_element = heap[i];
            heap[i] = heap[j];
            heap[j] = tmp;
            i = j;
            j = i*2;
        }
        else
        {

            break;
        }
        
        
    }    
    return del_element;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** findRelativeRanks(int* score, int scoreSize, int* returnSize)
{
    memset(hashtable, -1, sizeof(hashtable));
    
    int * heap = (int *)malloc(sizeof(int) * (scoreSize + 1));
    
    heap[0] = 0;
    heap[1] = score[0];
    hashtable[score[0]] = 0;
   
    int i=0;
    for(i=1; i<scoreSize; i++)
    {
        insert_heap(heap, score[i], i+1);
        hashtable[score[i]] = i;
    }
    
    char ** ret_arr = (char **)malloc(sizeof(char *) * scoreSize);
    int ret_arr_index = 0;
    int heap_index = scoreSize;
    
    for(i=1; i<scoreSize+1; i++)
    {
        //printf("del_element : %d \r\n", delete_heap(heap, &heap_index));

        if(i == 1)
        {
            int len = strlen("Gold Medal");
            char * tmp_arr = (char *)malloc(sizeof(char) * (len + 1));
            int delete_element = delete_heap(heap, &heap_index);
            
            int index = hashtable[delete_element];
            ret_arr[index] = tmp_arr;
            memcpy(tmp_arr, "Gold Medal", sizeof(char) * len);
            tmp_arr[len] = '\0';
        }
        else if(i == 2)
        {
            int len = strlen("Silver Medal");
            char * tmp_arr = (char *)malloc(sizeof(char) * (len + 1));
            int delete_element = delete_heap(heap, &heap_index);
            
            int index = hashtable[delete_element];
            ret_arr[index] = tmp_arr;
            memcpy(tmp_arr, "Silver Medal", sizeof(char) * len);
            tmp_arr[len] = '\0';
        }
        else if(i == 3)
        {
            int len = strlen("Bronze Medal");
            char * tmp_arr = (char *)malloc(sizeof(char) * (len + 1));
            int delete_element = delete_heap(heap, &heap_index);
            
            int index = hashtable[delete_element];
            ret_arr[index] = tmp_arr;
            memcpy(tmp_arr, "Bronze Medal", sizeof(char) * len);
            tmp_arr[len] = '\0';
        }
        else
        {
            char tmp_buf[10] = {'\0'};
            sprintf(tmp_buf, "%d", i);
            int len = strlen(tmp_buf);
            char * tmp_arr = (char *)malloc(sizeof(char) * (len + 1));
            int delete_element = delete_heap(heap, &heap_index);
            
            int index = hashtable[delete_element];
            ret_arr[index] = tmp_arr;
            memcpy(tmp_arr, tmp_buf, sizeof(char) * len);
            tmp_arr[len] = '\0';
        }
        
    }

    
    *returnSize = scoreSize;
    return ret_arr;
    
}