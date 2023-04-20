// This is for leetcode #30

// NOTE
// 1. Words are all [a-z]+
// 2. Words have under 30 characters
//    NOTE
//      1. [a-z] -> 26 options which fits inside 5 bits, so we need 160 bits total, which is 3 unit64_t's
//         meaning we can more or less fit a hash in registers
// 3. There are no more than 5000 words
// 4. Words have THE SAME LENGTH

// Optimizations (only needed 1 and 3 apparently)
// 1. Don't scan beyond where you could not find something: DONE
// 2. Sort the words or keep them in a Trie so we can immediately discard things that don't match
//    (or use somthing like Robin Karp to "guard" the words so to speak): Not necessary
// 3. Store the words in a counter by equality: DONE
// 4. ... Not necessary

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <stdint.h>

#ifndef NULL
#define NULL 0
#endif

#ifndef true
#define true 1
#endif
#ifndef false
#define false 0
#endif

#ifndef bool
#define bool int
#endif

struct ExampleSt {
    char* s;
    char** words;
    int wordsSize;
};
typedef struct ExampleSt Example;

#define _MAX_WORD_LEN 50

Example example1() {
    // Input: s = "barfoothefoobarman", words = ["foo","bar"]
    // Output: [0,9]
    Example ex;
    ex.s = malloc(_MAX_WORD_LEN * sizeof(char));
    memset(ex.s, 0, _MAX_WORD_LEN * sizeof(char));
    sprintf(ex.s, "barfoothefoobarman");
    ex.wordsSize = 2;
    ex.words = malloc(ex.wordsSize * sizeof(char*));
    for (int i = 0; i < ex.wordsSize; i++) {
        ex.words[i] = (char*)malloc(_MAX_WORD_LEN * sizeof(char));
        memset(ex.words[i], 0, _MAX_WORD_LEN * sizeof(char));
    }
    sprintf(ex.words[0], "foo");
    sprintf(ex.words[1], "bar");
    return ex;
}

Example example2() {
    // Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    // Output: []
    Example ex;
    // TODO
    return ex;
}

Example example3() {
    // Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    // Output: [6,9,12]
    Example ex;
    // TODO
    return ex;
}

Example example4() {
    // Input: s = "thethethethe", words = ["foo","foo","the","man"]
    // Output: []
    Example ex;
    ex.s = malloc(_MAX_WORD_LEN * sizeof(char));
    memset(ex.s, 0, _MAX_WORD_LEN * sizeof(char));
    sprintf(ex.s, "thethethethe");
    ex.wordsSize = 4;
    ex.words = malloc(ex.wordsSize * sizeof(char*));
    for (int i = 0; i < ex.wordsSize; i++) {
        ex.words[i] = (char*)malloc(_MAX_WORD_LEN * sizeof(char));
        memset(ex.words[i], 0, _MAX_WORD_LEN * sizeof(char));
    }
    sprintf(ex.words[0], "foo");
    sprintf(ex.words[1], "foo");
    sprintf(ex.words[2], "the");
    sprintf(ex.words[3], "man");
    return ex;
}

struct WordEntryStruct {
    int avail;
    char* word;
};

typedef struct WordEntryStruct WordEntry;

struct WordSetStruct {
    WordEntry* words;
    int numWords;
    int numUniqueWords;
    int numAvailWords;
};
typedef struct WordSetStruct WordSet;

// Linear check for equality
bool weq(char* w1, char* w2) {
    assert(strlen(w1) > 0);
    assert(strlen(w2) > 0);
    int i = 0;
    int j = 0;
    while (w1[i] != '\0' && w2[j] != '\0' && w1[i] == w2[j]) {
        i++;
        j++;
    }
    return w1[i] == '\0' && w2[j] == '\0';
}

WordSet make(char** words, int numWords) {
    WordSet ws;
    ws.words = malloc(numWords * sizeof(WordEntry));

    int uniques = 0;
    // NOTE Quadratic... we could probably do better...
    // but this shouldn't be the bottleneck because ther are only 5000 words
    for (int i = 0; i < numWords; i++) {
        bool found = false;
        for (int j = 0; j < uniques; j++) {
            if (weq(ws.words[j].word, words[i])) {
                ws.words[j].avail ++;
                found = true;
                break;
            }
        }
        if (!found) {
            WordEntry e;
            e.word = words[i];
            e.avail = 1;
            ws.words[uniques] = e;

            uniques ++;
        }
    }
    ws.numWords = numWords;
    ws.numUniqueWords = uniques;
    ws.numAvailWords = numWords;
    return ws;
}

// Boolean function to return whether we can find a match at the beginning of `s`
int find(char* s, WordSet ws) {
    if (ws.numAvailWords == 0) {
        return true;
    }
    bool matched = false;
    for (int i = 0; i < ws.numUniqueWords && !matched; i++) {
        if (ws.words[i].avail > 0) {
            ws.numAvailWords --;
            ws.words[i].avail --;

            char* word = ws.words[i].word;
            int j = 0;
            // NOTE we guarantee no overflow by calling it on s prefixes of the right length ONLY
            while (word[j] != '\0' && word[j] == s[j]) {
                j++;
            }

            matched = word[j] == '\0' && find(s + j, ws);
            ws.numAvailWords ++;
            ws.words[i].avail ++;
         }
    }
    return matched;
}

int* findSubstring(char * s, char ** words, int wordsSize, int* returnSize) {
    int len = strlen(s);
    int totalWordsSize = 0;
    for (int i = 0; i < wordsSize; i++) {
        totalWordsSize += strlen(words[i]);
    }

    // Create a set datastructure
    WordSet wordSet = make(words, wordsSize);

    // Fill our indices
    int* indices = malloc(len * sizeof(int));
    *returnSize = 0;
    for (int i = 0; i < (len - totalWordsSize + 1); i++) {
        if (find(s + i, wordSet)) {
            indices[*returnSize] = i;
            *returnSize += 1;
        }
    }
    return indices;
}

int main() {
    #define NUM_EXAMPLES 2
    Example examples[NUM_EXAMPLES] = {example1(), example4()};
    for (int i = 0; i < NUM_EXAMPLES; i++) {
        // Run algorithm
        int returnSize = -1;
        int* indices = findSubstring(examples[i].s, examples[i].words, examples[i].wordsSize, &returnSize);
        assert(returnSize != -1);
        printf("*************************\n");

        // Print results
        for (int j = 0; j < returnSize - 1; j++) {
            printf("%d ", indices[j]);
        }
        if (returnSize > 0) {
            printf("%d", indices[returnSize - 1]);
        }
        printf("\n");

        // Cleanup
        free(indices);
        free(examples[i].s);
        for (int j = 0; j < examples[i].wordsSize; j++) {
            free(examples[i].words[j]);
        }
        free(examples[i].words);
    }
    return 0;
}