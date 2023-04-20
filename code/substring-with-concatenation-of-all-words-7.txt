typedef struct trie {
    uint16_t count;
    uint16_t used;
    struct trie *t[26];
} Trie;

void FreeTrie(Trie *trie)
{    
    for (int i = 0; i < 26; i++) {
        if (trie->t[i] != NULL) {
            FreeTrie(trie->t[i]);
            free(trie->t[i]);
        }
    }
}

void ClearUsedTrie(Trie *trie)
{
    // trie->count implies it is a leaf node
    if (!trie->count) {
        for (int i = 0; i < 26; i++) {
            if (trie->t[i] != NULL) {
                ClearUsedTrie(trie->t[i]);
            }
        }
    }
    trie->used = 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSubstring(char * s, char ** words, int wordsSize, int* returnSize){
    int* ret = calloc(1, sizeof(int));
    int rCount = 0;
    Trie head = { 0, 0, { NULL } };
    const int wlen = strlen(words[0]);
    
    *returnSize = 1;
    for (int i = 0; i < wordsSize; i++) {
        Trie *cur = &head;

        for (int j = 0; j < wlen; j++) {
            const uint8_t idx = words[i][j] - 'a';

            if (cur->t[idx] == NULL) {
                cur->t[idx] = calloc(1, sizeof(Trie));
            }
            cur = cur->t[idx];
        }
        cur->count++;
    }
    
    {
        const int len = strlen(s);
        
        for (int i = 0; i <= (len - wlen*wordsSize); i++) {
            Trie* cur = &head;
            int count = 0;

            for (int j = i; j < len; j++) {
                const uint8_t idx = s[j] - 'a';
                
                if (cur->t[idx] == NULL) {
                    break;
                } else {
                    const bool endOfWord = ((j - i) % wlen) == (wlen - 1);

                    cur = cur->t[idx];
                    if (endOfWord) {
                        if (cur->used < cur->count) {
                            cur->used++;
                            count++;
                            if (count == wordsSize) {
                                break;
                            }
                        } else {
                            break;
                        }

                        cur = &head;
                    }
                }
            }
            
            if (count == wordsSize) {
                if (rCount == *returnSize) {
                    *returnSize *= 2;
                    ret = realloc(ret, *returnSize*sizeof(int));
                }
                ret[rCount++] = i;
            }
            if (count != 0) {
                ClearUsedTrie(&head);
            }
        }
    }
    
    FreeTrie(&head);
    
    if (rCount != *returnSize) {
        ret = realloc(ret, rCount*sizeof(int));
        *returnSize = rCount;
    }
    
    return ret;
}