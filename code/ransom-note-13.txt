bool canConstruct(char * ransomNote, char * magazine){
    int n=strlen(ransomNote);
    int m=strlen(magazine);

    int freq1[26]={0};
    int freq2[26]={0};
    for(int i=0; i<n; i++){
        freq1[ransomNote[i]-'a']=freq1[ransomNote[i]-'a']+1;
    }
    for(int i=0; i<m; i++){
        freq2[magazine[i]-'a']=freq2[magazine[i]-'a']+1;
    }
    int sum=0;
    for(int i=0; i<26; i++){
        printf("%c %d %d\n",freq1[i]+'a', freq1[i], freq2[i]);
        if( freq1[i]!=0 || freq2[i]!=0){
            if(freq1[i]<=freq2[i]){
                sum=sum+freq1[i];
            }
        }
    }
    if(sum==n){
        return true;
    }
    return false;
    

}