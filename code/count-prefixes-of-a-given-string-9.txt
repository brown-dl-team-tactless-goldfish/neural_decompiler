int countPrefixes(char ** words, int wordsSize, char * s){

    int count = 0; 
    int sLen = strlen(s); 
    for(int i=0; i<wordsSize; i++)
    {
        int wordLen = strlen(words[i]);
        if (wordLen > sLen)
        {
            continue; 
        }
        else if (memcmp(words[i], s, wordLen) == 0)
        {
            count++;
        }
    }
    return count; 
}