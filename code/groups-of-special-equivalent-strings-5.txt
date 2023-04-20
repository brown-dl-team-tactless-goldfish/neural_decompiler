#define NO_OF_WORDS 1000
char hashtable[1000][21] = {'\0'};
int  counttable[1000] = {0};

void merge(char arr[], int low, int mid, int high)
{
    char * ret_arr = (char *)malloc(sizeof(char) * (high - low + 1));
    int ret_arr_index = 0;
    
    int i=0,j=0;
    for(i=low, j=mid+1; i<=mid && j<=high;)
    {
        if(arr[i] <= arr[j])
        {
            ret_arr[ret_arr_index++] = arr[i++];
        }
        else
        {
            ret_arr[ret_arr_index++] = arr[j++];
        }
    }
    
    while(i<=mid)
    {
        ret_arr[ret_arr_index++] = arr[i++];
    }
    
    while(j<=high)
    {
        ret_arr[ret_arr_index++] = arr[j++];
    }

    
    memcpy(&arr[low], ret_arr, sizeof(char) * ret_arr_index);
    free(ret_arr);
}

void merge_sort(char arr[], int low, int high)
{
    if(low<high)
    {
        int mid = (low + high)/2;
        merge_sort(arr, 0, mid);
        merge_sort(arr, mid+1, high);
        merge(arr, 0, mid, high);
    }
}

int numSpecialEquivGroups(char ** words, int wordsSize)
{
    memset(hashtable, '\0', sizeof(char)*1000*21);
    memset(counttable, 0, sizeof(counttable));
    
    int count = 0;
    
    char ** odd = (char **)malloc(sizeof(char *) * wordsSize);
    int odd_index = 0;
    
    char ** even = (char **)malloc(sizeof(char *) * wordsSize);
    int even_index = 0;
    
    int rows = 0;
    for(rows=0; rows<wordsSize; rows++)
    {
        int i=0;
        int len = strlen(words[i]);
        
        //Put odd indexes in odd
        char * tmp_odd = (char *)malloc(sizeof(char) * (len+1));
        int tmp_odd_index = 0;
        for(i=1; i<len; i+=2)
        {   
            tmp_odd[tmp_odd_index++] = words[rows][i];
        }
        tmp_odd[tmp_odd_index] = '\0';
        odd[rows] = tmp_odd;
        
        //Put even indexes in even
        char * tmp_even = (char *)malloc(sizeof(char) * (len+1));
        int tmp_even_index = 0;
        for(i=0; i<len; i+=2)
        {      
            tmp_even[tmp_even_index++] = words[rows][i];
        }
        tmp_even[tmp_even_index] = '\0';
        even[rows] = tmp_even;
    }
    
    for(rows=0; rows<wordsSize; rows++)
    {
        int len = strlen(odd[rows]);
        merge_sort(odd[rows], 0, len-1);
        odd[rows][len] = '\0';
        
        len = strlen(even[rows]);
        merge_sort(even[rows], 0, len-1);
        
    }
    
    int i=0;
    for(rows=0; rows<wordsSize; rows++)
    {
        int len1 = strlen(odd[rows]);
        int len2 = strlen(even[rows]);
        
        char * tmp_arr = (char *)malloc(sizeof(char) * (len1 + len2 + 1));
        memcpy(&tmp_arr[0], odd[rows], sizeof(char) * len1);
        memcpy(&tmp_arr[len1], even[rows], sizeof(char) * len2);
        tmp_arr[len1 + len2] = '\0';
        
        for(i=0; i<1000; i++)
        {
           if(hashtable[i][0] == '\0')      //Hashtable Index Entry Empty, Insert it
           {
               memcpy(&hashtable[i][0], tmp_arr, sizeof(char) * (len1 + len2 + 1));
               counttable[i] += 1;
               break;
           }
            
           int diff = strcmp(hashtable[i], tmp_arr);
           if(diff == 0)
           {
               counttable[i] += 1;
               break;
           }
        }
    }
    
    for(i=0; i<1000; i++)
    {
        if(hashtable[i][0] != '\0')
        {
            count++;
        }
        else
        {
            break;
        }
    }
    return count;
    
}