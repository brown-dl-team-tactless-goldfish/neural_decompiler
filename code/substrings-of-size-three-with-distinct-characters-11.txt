int hashtable[26] = {0};

int countGoodSubstrings(char * s)
{
    memset(hashtable, 0x00, sizeof(hashtable));
    
    int length = 3;
    int i=0;
    int start_index = 0;
    int end_index = 0;
    int max = 0;
    
    while(s[end_index]!='\0')
    {
        if(end_index - start_index < length-1)
        {
            hashtable[s[end_index] - 'a'] += 1;
        }
        else if (end_index - start_index >= length-1)
        {
            hashtable[s[end_index] - 'a'] += 1;
            
            int i=0;
            bool flag = true;
            
            for(i=0; i<26; i++)
            {
                if(hashtable[i] > 1)
                {
                    flag = false;
                    break;
                }
            }
            
            if(flag)
            {
                max++;
            }
            
            hashtable[s[start_index] - 'a'] -= 1;
            start_index++;   
        }
        end_index++;
    }
    
    return max;
}