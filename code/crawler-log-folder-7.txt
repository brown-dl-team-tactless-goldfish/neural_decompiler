int minOperations(char ** logs, int logsSize)
{
    int count = 0;
    
    int i=0;
    for(i=0; i<logsSize; i++)
    {
        if(strcmp(logs[i], "../") == 0)
        {
            if(count > 0)
                count--;
        }
        else if(strcmp(logs[i], "./") == 0)
        {
            
        }
        else
        {
            count++;
        }
    }
    
    if(count < 0)
        count = 0;
    return count;
}