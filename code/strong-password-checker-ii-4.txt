bool strongPasswordCheckerII(char * password){

    int len = strlen(password);
    if(len < 8)
    {
        return false; 
    }
    
    bool    lowercase   = false, 
            uppercase   = false, 
            digit       = false, 
            character   = false;
    
    for(int i=0; i<len; i++)
    {
        if ((i != 0) && (password[i-1] == password[i]))
        {
            return false; 
        }
        else if(lowercase == false && password[i] >= 'a' && password[i] <= 'z')
        {
            lowercase = true; 
        }
        else if(uppercase == false && password[i] >= 'A' && password[i] <= 'Z')
        {
            uppercase = true; 
        }
        else if(digit == false && password[i] >= '0' && password[i] <= '9')
        {
            digit = true; 
        }
        else if((character == false) &&
           (
               (password[i] == '!') ||
               (password[i] == '@') ||
               (password[i] == '#') ||
               (password[i] == '$') ||
               (password[i] == '%') ||
               (password[i] == '^') ||
               (password[i] == '&') ||
               (password[i] == '*') ||
               (password[i] == '(') ||
               (password[i] == ')') ||
               (password[i] == '+') ||
               (password[i] == '-')
            )
          )
        {
            character = true; 
        }
    }
    return ((lowercase == true) && (uppercase == true) && (digit == true) && (character == true));
}