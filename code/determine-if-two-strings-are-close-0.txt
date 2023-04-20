int cmp(const void* a, const void* b){
    return *(int*)a - *(int*)b;
}
bool closeStrings(char * word1, char * word2){
    int n1 = strlen(word1);
    int n2 = strlen(word2);
    if(n1 != n2)
        return false;
    int* alph1 = calloc(26, sizeof(int));
    int* alph2 = calloc(26, sizeof(int));
    for(int i = 0; i < n1; i++){
        alph1[word1[i] - 'a']++;
        alph2[word2[i] - 'a']++;
    }
    for(int i = 0; i < 26; i++){
        if(alph1[i]== 0 && alph2[i]!= 0)
            return false;
        if(alph2[i]== 0 && alph1[i]!= 0)
            return false;
    }
    qsort(alph1, 26, sizeof(int), cmp);
    qsort(alph2, 26, sizeof(int), cmp);
    for(int i = 0; i < 26; i++){
        if(alph1[i] != alph2[i])
            return false;
    }
    return true;
}