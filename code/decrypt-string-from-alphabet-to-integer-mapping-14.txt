char hash_table[17] = {'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                       'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};


char * freqAlphabets(char * s)
{
    int i=0;
    int len = strlen(s);
    
    char * ret_str = (char *)malloc(sizeof(char)*(len+1));
    int ret_str_index = 0;
    
    int start_index = 0;
    if( (len == 0) || (len == 1) || (len == 2))
    {
        while(start_index < len)
        {
            ret_str[ret_str_index++] = (s[start_index] - '1' + 'a');
            start_index++;
        }
        ret_str[ret_str_index] = '\0';
        return ret_str;
    }
    
    
    int end_index   = 2;
    
    while((end_index < len) && (start_index < len))
    {
        if(s[end_index] == '#')
        {
            int num = 0;
            num = (s[start_index] - '0')*10 + (s[start_index+1] - '0');
            ret_str[ret_str_index++] = hash_table[num - 10];
            
            start_index += 3;
            end_index += 3;
        }
        else
        {
            ret_str[ret_str_index++] = (s[start_index] - '1' + 'a');
            start_index++;
            end_index++;
        }
    }
    
    if((start_index>=len) && (end_index>=len))
    {
        ret_str[ret_str_index] = '\0';
    }
    else if((start_index<len) && (end_index >= len))
    {
        while(start_index < len)
        {
            ret_str[ret_str_index++] = (s[start_index] - '1' + 'a');
            start_index++;
        }
        ret_str[ret_str_index] = '\0';    
    }
    return ret_str;
}