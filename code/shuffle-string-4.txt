#include <stdlib.h>

char * restoreString(char * s, int* indices, int indicesSize) {
    char *result = (char*)malloc(sizeof(char) * (indicesSize + 1));
    for (int i =0; i <indicesSize; i++) {
        int index_value = indices[i];
        result[index_value] = s[i];
    }

    result[indicesSize] = '\0';
    return result;
}