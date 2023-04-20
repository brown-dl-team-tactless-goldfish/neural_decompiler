int myAtoi(char * s){
    int i = 0;
    while(s[i]!='\0' && s[i]==' ') i++;
    bool x = false;
    int ans = 0;
    int max = INT_MAX/10;
    if(s[i]=='-' || s[i]=='+'){
        x = (s[i++]=='-');
    }
    while(s[i]>='0' && s[i]<='9'){
        if(x && (-max>ans || (-max==ans && s[i]>='8'))) return INT_MIN;
        if(!x && (max<ans || (max==ans && s[i]>='7'))) return INT_MAX;
        ans = ans*10 + (s[i++]-'0')*(x?-1:1);
    }
    return ans;
}