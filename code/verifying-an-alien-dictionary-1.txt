
bool IsRawInOrder(char ** words, int wordsSize, int *translate, int deep)
{
    int i,j;
    for(i=0,j=0; i<wordsSize; i++)
    {
        if ((i+1) < wordsSize)
        {
            if (words[i][deep] == words[i+1][deep])
            {
                if (words[i][deep+1] == 0)
                {
                    if (j<i) return false;
                    else
                        j= i+1;
                }
                continue;
            }
            if (translate[words[i][deep]-'a']>translate[words[i+1][deep]-'a'])
                return false;
            
            if (!IsRawInOrder(words+j, i-j+1, translate, deep+1))
                return false;
            j=i+1;
        } 
        if (words[i][deep+1] == 0)
        {
            if (j<i) return false;
        }
        else
        {
            if (!IsRawInOrder(words+j, i-j+1, translate, deep+1))
              return false;
        }
        
        j=i+1;
    }
    return true;
}


bool isAlienSorted(char ** words, int wordsSize, char * order)
{
    int translate[26];
    int i;
    for (i=0; i<26; i++)
    {
        if (!order[i]) return 0;
        translate[order[i]-'a'] = i;
    }
    if (order[i]) return 0;
    
    if (!IsRawInOrder(words, wordsSize, translate, 0))
        return false;

    return true;

}
