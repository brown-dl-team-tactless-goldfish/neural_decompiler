void merge(int ** arr, int low, int mid, int high)
{

    int * ret_arr = (int *)malloc(sizeof(int) * ((high-low+1)*2));
    int ret_arr_index = 0;
    
    int i=low, j=mid+1;
    for(i=low, j=mid+1; i<=mid && j<=high;)
    {
        if(arr[i][1] <= arr[j][1])
        {
            *(ret_arr + ret_arr_index) = arr[i][0];
            ret_arr_index++;
            *(ret_arr + ret_arr_index) = arr[i][1];
            ret_arr_index++;
            i++;
        }
        else
        {
            *(ret_arr + ret_arr_index) = arr[j][0];
            ret_arr_index++;
            *(ret_arr + ret_arr_index) = arr[j][1];
            ret_arr_index++;
            j++;
        }
    }
    
    while(i<=mid)
    {
         *(ret_arr + ret_arr_index) = arr[i][0];
         ret_arr_index++;
         *(ret_arr + ret_arr_index) = arr[i][1];
         ret_arr_index++;
         i++;
    }
    
    while(j<=high)
    {
        *(ret_arr + ret_arr_index) = arr[j][0];
        ret_arr_index++;
        *(ret_arr + ret_arr_index) = arr[j][1];
        ret_arr_index++;
        j++;
    }

    
    int k=0;
    int z=0;
    for(k=low; k<=high; k++)
    {
        arr[k][0] = ret_arr[z++];
        arr[k][1] = ret_arr[z++];
    }
    
    free(ret_arr);

}


void merge_sort(int ** arr, int low, int high)
{
    if(low<high)
    {
        int mid = (low+high)/2;
        merge_sort(arr, low, mid);
        merge_sort(arr, mid+1, high);
        merge(arr, low, mid, high);
    }
}

int maximumUnits(int** boxTypes, int boxTypesSize, int* boxTypesColSize, int truckSize)
{
    int i=0;
    int remaining = 0;
    int total_box = 0;
    int ret = 0;
    bool flag = true;
    int j=0;
    
    //Sort on the basis of no of units (Merge Sort)
    merge_sort(boxTypes, 0, boxTypesSize-1); 
    
    for(i=boxTypesSize-1; i>=0; i--)
    {
        int box_type    = boxTypes[i][0];
        int no_of_units = boxTypes[i][1];

        
        if(total_box + box_type > truckSize)
        {
            box_type = truckSize - total_box;
            total_box += box_type;
            ret += (box_type * no_of_units);
            break;
        }
        else
        {
            total_box += boxTypes[i][0];
            ret += (box_type * no_of_units);
        }
    }
    return ret;
}