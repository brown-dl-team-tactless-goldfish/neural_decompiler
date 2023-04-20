

int longestOnes(int* nums, int numsSize, int k)
{
    
    int start_index = 0;
    int end_index = 0;
    int max = INT_MIN;
    
    if(k==0)
    {
        //Calculate no of consecutive 1's
        while(end_index < numsSize)
        {
            if(nums[end_index] == 1)
            {
                end_index++;
            }
            else
            {
                start_index++;
                if(start_index > end_index)
                {
                    end_index = start_index;
                }
            }
            
            if(end_index - start_index >= max)
            {
                max = (end_index - start_index);
            }
        }
        return max;
    }
    
    int no_of_flips = 0;
    int * index_arr = (int *)malloc(sizeof(int) * k);
    int index_arr_index = 0;
    int cur_check_index = 0;
    
    while(end_index<numsSize)
    {
        if(nums[end_index] == 1)
        {
            end_index++;
            
        }
        
        else if(nums[end_index] == 0)
        {
            if(no_of_flips < k)
            {
                no_of_flips++;
                index_arr[index_arr_index++] = end_index;
                end_index++;    
                
            }
            else
            {
                if(start_index != index_arr[cur_check_index])
                {
                    start_index++;
                }
                else if(start_index == index_arr[cur_check_index])
                {
                    cur_check_index++;
                    if(cur_check_index == k)
                    {
                        cur_check_index = 0;
                    }
                    no_of_flips--;
                    
                    if(index_arr_index == k)
                    {
                        index_arr_index = 0;
                    }
                    start_index++;
                    
                }
            }
            
        }
        
        if(end_index - start_index > max)
        {
            max = end_index - start_index;
        }      
    }
    free(index_arr);
    return max;
}