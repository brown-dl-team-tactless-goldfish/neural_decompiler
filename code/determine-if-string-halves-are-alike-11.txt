

bool halvesAreAlike(char * s)
{
    int len = strlen(s);
    
    int a = 0;
    int b = (len/2);
    
    int no_of_vowels_in_a = 0;
    int no_of_vowels_in_b = 0;
    
    int i=0, j=0;
    
    for(i=a,j=b; (i<b) && (j<len); i++, j++)
    {
        if( (s[i] == 'a') || (s[i] == 'e') || (s[i] == 'i') || (s[i] == 'o') || (s[i] == 'u') || \
            (s[i] == 'A') || (s[i] == 'E') || (s[i] == 'I') || (s[i] == 'O') || (s[i] == 'U'))
        {
            no_of_vowels_in_a++;
        }
        
        if( (s[j] == 'a') || (s[j] == 'e') || (s[j] == 'i') || (s[j] == 'o') || (s[j] == 'u') || \
            (s[j] == 'A') || (s[j] == 'E') || (s[j] == 'I') || (s[j] == 'O') || (s[j] == 'U'))
        {
            no_of_vowels_in_b++;
        }
    }
    
    if(no_of_vowels_in_a == no_of_vowels_in_b)
        return true;
    else 
        return false;
    
    
}