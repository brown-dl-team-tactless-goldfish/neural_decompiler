char letters['A' + 62] = {
    ['A'] = 1,
    ['B'] = 1,
    ['C'] = 1,
    ['D'] = 1,
    ['E'] = 1,
    ['F'] = 1,
    ['G'] = 1,
    ['H'] = 1,
    ['I'] = 1,
    ['J'] = 1,
    ['K'] = 1,
    ['L'] = 1,
    ['M'] = 1,
    ['N'] = 1,
    ['O'] = 1,
    ['P'] = 1,
    ['Q'] = 1,
    ['R'] = 1,
    ['S'] = 1,
    ['T'] = 1,
    ['U'] = 1,
    ['V'] = 1,
    ['W'] = 1,
    ['X'] = 1,
    ['Y'] = 1,
    ['Z'] = 1,
    ['a'] = 2,
    ['b'] = 2,
    ['c'] = 2,
    ['d'] = 2,
    ['e'] = 2,
    ['f'] = 2,
    ['g'] = 2,
    ['h'] = 2,
    ['i'] = 2,
    ['j'] = 2,
    ['k'] = 2,
    ['l'] = 2,
    ['m'] = 2,
    ['n'] = 2,
    ['o'] = 2,
    ['p'] = 2,
    ['q'] = 2,
    ['r'] = 2,
    ['s'] = 2,
    ['t'] = 2,
    ['u'] = 2,
    ['v'] = 2,
    ['w'] = 2,
    ['x'] = 2,
    ['y'] = 2,
    ['z'] = 2,
    ['0'] = 3,
    ['1'] = 3,
    ['2'] = 3,
    ['3'] = 3,
    ['4'] = 3,
    ['5'] = 3,
    ['6'] = 3,
    ['7'] = 3,
    ['8'] = 3,
    ['9'] = 3,
};

int strongPasswordChecker(char * password){
    int length = strlen(password);
    int replace = 0;
    int one = 0;
    int two = 0;
    int cap = 1;
    int low = 1;
    int dig = 1;
    
    for(int i = 0; password[i]; i++){
        if(letters[password[i]] == 1){
            cap = 0;
        } else if(letters[password[i]] == 2) {
            low = 0;
        } else if(letters[password[i]] == 3) {
            dig = 0;
        }
        
        int repeat = 1;
        while(password[i] == password[i + 1]){
            i++;
            repeat += 1;
        }
        
        if(repeat > 2){
            replace += (repeat / 3);

            if(repeat % 3 == 0){
                one += 1;
            } else if(repeat % 3 == 1){
                two += 2;
            }
        }
    }
    
    if(length < 6){
        if(cap + low + dig > 6 - length){
            return cap + low + dig;
        } else {
            return 6 - length;
        }
    } else if(length <= 20){
        if(cap + low + dig > replace){
            return cap + low + dig;
        } else {
            return replace;
        }
    } else {
        int over = length - 20;
        
        if(one < over){
            replace -= one;
        } else {
            replace -= over;
        }
        
        if(over - one > 0){
            if(two < (over - one)){
                replace -= two / 2;
            } else {
                replace -= (over - one) / 2;
            }
        }
        
        if((over - one - two) > 0){
            replace -= (over - one - two) / 3;
        }
        
        if(cap + low + dig > replace){
            return over + cap + low + dig;
        } else {
            return over + replace;
        }
    }
}