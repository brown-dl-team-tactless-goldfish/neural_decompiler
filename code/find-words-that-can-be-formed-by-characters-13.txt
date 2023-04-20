int original_hashtable[26] = {0};
int cur_hashtable[26] = {0};

int countCharacters(char ** words, int wordsSize, char * chars)
{
    memset(original_hashtable, 0x00, sizeof(original_hashtable));
    
    //Build hashtable, the value being the freq of characters
    int i=0;
    while(chars[i] != '\0')
    {
        original_hashtable[chars[i] - 'a'] += 1;
        i++;
    }
    
    
    int count = 0;
    for(i=0; i<wordsSize; i++)
    {
        memcpy(cur_hashtable, original_hashtable, sizeof(original_hashtable));
        int j=0;
        bool match = true;
        while(words[i][j] != '\0')
        {
            int freq = cur_hashtable[words[i][j] - 'a'];
            if(freq > 0)
            {
                cur_hashtable[words[i][j] - 'a'] -= 1;
            }
            
            if(freq == 0)
            {
                match = false;
            }
            j++;
        }
        
        if(match)
        {
            count += strlen(words[i]);
        }
    }
    return count;
}