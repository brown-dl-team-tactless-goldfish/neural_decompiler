#define newArray(type, size) ((type*)calloc(size, sizeof(type)))
#define resizeArray(ptr, type, size) ((type*)realloc(ptr, (size) * sizeof(type)))

int *pushback(int *array, int *size, int value) {
    int *output = resizeArray(array, int, *size + 1);
    output[(*size)++] = value;
    return output;
}

typedef struct {
    char *word;
    int occurs;
} wordEntry;

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSubstring(char* s, char** words, int wordsSize, int* returnSize) {
    int *result = NULL;
    *returnSize = 0;

    // edge conditions
    if (wordsSize <= 0)
        return result;
    int slength = strlen(s), wlength = strlen(words[0]);
    if (slength < wlength * wordsSize)
        return result;

    // handle words, count the duplicates.
    wordEntry *ws = newArray(wordEntry, wordsSize);
    int wsSize = 0, i, j, k;
    for (i = 0; i < wordsSize; ++i) {
        char *word = words[i];
        for (k = -1, j = 0; k < 0 && j < wsSize; ++j)
            if (strcmp(ws[j].word, word) == 0)
                k = j;
        if (k < 0)
            k = wsSize++;
        ws[k].word = word;
        ws[k].occurs++;
    }

    // calulate word matched at each position.
    slength -= wlength - 1;
    int *ms = newArray(int, slength);
    for (i = 0; i < slength; ++i) {
        for (k = -1, j = 0; k < 0 && j < wsSize; ++j)
            if (strncmp(s + i, ws[j].word, wlength) == 0)
                k = j;
        // store matched index in word list without duplicates.
        ms[i] = k;
    }

    // scan all possible chains, cached word indices stored in os.
    int *os = newArray(int, wordsSize);
    for (i = 0; i < wlength; ++i) {
        int start = i, found = 0;
        for (j = i; j < slength; j += wlength) {
            int windex = ms[j];
            if (windex < 0) {
                // no matched word here, simply reset the marker,
                // and write back all cached words.
                start = j + wlength;
                while (found > 0) {
                    ws[os[--found]].occurs++;
                }
                continue;
            }
            // move the matched word from word list to cache,
            // write back the leading cached words if necessary.
            if (ws[windex].occurs == 0) {
                for (k = 0; k < found; ++k) {
                    ws[os[k]].occurs++;
                    start += wlength;
                    if (os[k] == windex) {
                        ++k;
                        break;
                    }
                }
                found -= k;
                if (found)
                    memmove(os, os + k, found * sizeof(*os));
            }
            ws[windex].occurs--;
            os[found++] = windex;
            // push the marker position if matched all words.
            if (found == wordsSize)
                result = pushback(result, returnSize, start);
        }
        // after scanning, write back all cached words.
        while (found > 0) {
            ws[os[--found]].occurs++;
        }
    }

    free(ws);
    free(ms);
    free(os);

    return result;
}