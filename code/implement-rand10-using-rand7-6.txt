// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

int rand10() {
    int indx = 41;
    while (indx > 40){
        indx = (rand7() - 1) * 7 + rand7();
    }
    return ((indx - 1) % 10) + 1;
}