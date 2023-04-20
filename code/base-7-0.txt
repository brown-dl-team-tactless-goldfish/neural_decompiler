char * convertToBase7(int num){
    if(num == 0) return "0";
    char * result = (char *)malloc(12*sizeof(char));
    int count = 0;
    bool checkNeg = num < 0 ? true : false;
    if(num < 0) num = abs(num);
    while(num > 0)
    { 
        result[count++] = num % 7 + '0';
        num /= 7;
    }
    if(checkNeg) result[count++] = '-';
    for(int i=0; i<count/2; i++)
    {
        int temp = result[i];
        result[i] = result[count-i-1];
        result[count-i-1] = temp;
    }
    result[count] = 0;
    return result;
}