

int maxVowels(char * s, int k)
{
    int max_vowels = 0;
    int current_vowels = 0;
    
    int start_index = 0;
    int end_index=0;
    
    while(s[end_index]!='\0')
    {
        if((s[end_index] == 'a') || (s[end_index] == 'e') || (s[end_index] == 'i') || (s[end_index] == 'o') || (s[end_index] == 'u'))
        {
            current_vowels += 1;
        }
        
        if(current_vowels >= max_vowels)
        {
            max_vowels = current_vowels;
        }
        
        if(end_index - start_index +1 == k)
        {   
            if((s[start_index] == 'a') || (s[start_index] == 'e') || (s[start_index] == 'i') || (s[start_index] == 'o') || (s[start_index] == 'u'))
            {
                current_vowels -= 1;
            }
            start_index++;
            
        }
        end_index++;    
    }
    return max_vowels;
}