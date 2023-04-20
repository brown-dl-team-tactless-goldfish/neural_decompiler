void swap(char *left, char *right)
{
    char temp= *left;
    *left = *right;
    *right = temp;
}

char * reverseWords(char * s){
    char *left = s;
    char *space;
    char *right;
    while(*left!='\0' )
    {
        space = strchr(left, ' ');
        if(space)
            right = space-1;
        else
             right = left + strlen(left)-1;
        while(left<right)
        {
            swap(left,right);
            left ++;
            right -- ;
        }
        //printf("\nString is %s",s);
        if(space !=NULL)
            left = space +1;
        else
            break;
        
    }
    return s;
}