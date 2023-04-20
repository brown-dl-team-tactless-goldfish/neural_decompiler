char * removeStars(char * s){
    int i = 0, j = 0;
        while (s[i]!='\0') {
            if(s[i]!='*')
               s[j++]=s[i];
            else
               j--;
            i++;
        }
        s[j]='\0';
        return s;
}