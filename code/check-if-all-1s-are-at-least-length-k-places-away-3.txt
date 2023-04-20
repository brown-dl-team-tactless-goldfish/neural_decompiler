

bool kLengthApart(int* nums, int numsSize, int k)
{
    int match = true;
    
    int start_index = 0;
    int end_index = 0;
    bool first = false;
    for(end_index=0; end_index<numsSize; )
    {    
        if(nums[end_index] == 0)
        {
            end_index++;
        }
        else if(nums[end_index] == 1)
        {
            if(first == false)
            {
                first = true;
                start_index = end_index;
                end_index++;
            }
            else if(end_index - start_index - 1 < k)
            {      
                match = false;
                break;
            }
            else
            {
                start_index = end_index;
                end_index++;
            }     
        }
    }
    return match;
}