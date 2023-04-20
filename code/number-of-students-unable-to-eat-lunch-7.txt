void merge(int arr[], int low, int mid, int high)
{
    int * ret_arr = (int *)malloc(sizeof(int) * (high - low + 1));
    int ret_arr_index = 0;
    
    int i=low, j=mid+1;
    for(i=low, j=mid+1; i<=mid && j<=high; )
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
    
    memcpy(&arr[low], ret_arr, sizeof(int) * (high - low + 1));
    free(ret_arr);
}


void merge_sort(int arr[], int low, int high)
{
    if(low<high)
    {
        int mid = (low + high)/2;
        merge_sort(arr, low, mid);
        merge_sort(arr, mid+1, high);
        merge(arr, low, mid, high);
    }
}

int countStudents(int* students, int studentsSize, int* sandwiches, int sandwichesSize)
{
    merge_sort(students, 0, studentsSize-1);
    
    int start_index = 0;
    int end_index = studentsSize-1;
    
    int i=0;
    for(i=0; i<sandwichesSize; i++)
    {
        if(sandwiches[i] == students[start_index])
        {
            start_index++;
        }
        else if(sandwiches[i] == students[end_index])
        {
            end_index--;
        }
        else
        {
            break;
        }
    }
    int count = 0;
    if(start_index <= end_index)
        count = (end_index - start_index + 1);
    
    return count;
        
}