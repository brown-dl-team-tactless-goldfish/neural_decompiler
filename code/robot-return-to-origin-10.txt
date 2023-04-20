bool judgeCircle(char * moves){
    int a=0,b=0,c=0,d=0;
    for(int i=0;i<strlen(moves);i++){
        if(moves[i]=='U'){
            a++;
        }
        if(moves[i]=='D'){
            b++;
        }
        if(moves[i]=='L'){
            c++;
        }
        if(moves[i]=='R'){
            d++;
        }
       
        
    }
     if((a==b)&&(c==d)){
            return true;
        }
    return false;

}