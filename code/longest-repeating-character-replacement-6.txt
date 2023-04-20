int hash_table[26] = {0};

/*
*   The logic of this problem - You need to keep a track of frquency of characters in hashtable.
*   Subract the window length and most frequent character, if its less than k, slide the end index, else slide the start index.
*/

int characterReplacement(char * s, int k)
{
    memset(hash_table, 0x00, sizeof(hash_table));
    int start_index = 0;
    int end_index = 0;
    
    int replacement_count = 0;
    int max_len = INT_MIN;
    int count = 0;
    bool slide_end = true;
    
    while(s[end_index] != '\0')
    {
        if(slide_end)
        {
            hash_table[s[end_index]-'A'] += 1;
        }
        
        int most_frequent_char = 0;
        int i=0;
        for(i=0; i<26; i++)
        {
            if(hash_table[i] >= most_frequent_char)
            {
                most_frequent_char = hash_table[i];
            }
        }

        replacement_count = (end_index - start_index + 1) - most_frequent_char;
        
        if(replacement_count <= k)
        {
            slide_end = true;
            count++;
            end_index++;
        }
        else
        {
            slide_end = false;
            hash_table[s[start_index]-'A'] -= 1;
            count--;
            start_index++;
        }
        
        if(count >= max_len)
        {
            max_len = count;
        }
    }
    
    
    return max_len;
}