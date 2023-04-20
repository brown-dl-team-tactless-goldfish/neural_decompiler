

int numUniqueEmails(char ** emails, int emailsSize){
    //char *target;
    //int *hashValue = calloc(1,sizeof(int) * emailsSize);
    //int **cleanEmail = calloc(1,sizeof(char*) * emailsSize);
     char * domain;
     char * dot;
     char * plus;
    //int hashSum;
    int uniqueCount = 1;
    for(int i=0;i<emailsSize;i++)
    {
        //target = emails[i];
        //cleanEmail[i]=calloc(1, sizeof(char)*strlen(emails[i]));
        domain = strchr(emails[i], '@');
        dot =  strchr(emails[i], '.');
        plus = strchr(emails[i],'+');
        char *dest = emails[i];
        char * source = emails[i];
        bool crossedDomain = false;
        //hashSum = 0;
        for(;*source!='\0';)
        {
        
            if(*source == '@')
              crossedDomain = true;
            if(*source == '+' && crossedDomain == false)
            {
                source = domain;
                crossedDomain = true;
            }

            else if(*source == '.' && crossedDomain == false)
            {
                source ++;
                continue;
            }

            *dest = *source;
            //hashSum +=cleanEmail[i][j] ;
            source++;
            dest ++;
        }
        *dest = '\0';       
        printf("\nemail %d after processing is %s", i, emails[i]);
        if(i>=1)
        {
            int l = i-1;
            for(;l>=0;l--)
            {
                if(!(strcmp(emails[l], emails[i] )))
                   break;
            }
            if(l==-1)
                   uniqueCount++;
        }
    
    }
    // hash all the emails is done return unique hashSums now.
    return uniqueCount;


}