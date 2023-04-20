#define WORD_LEN 100

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** commonChars(char ** A, int ASize, int* returnSize){
  int table[WORD_LEN][26] = {0};

  // allocate memory for output string array
  char **result = malloc(WORD_LEN * sizeof(char *));
  for (int i = 0; i < WORD_LEN; ++i)
    // room for each character and null terminator
    result[i] = malloc(2 * sizeof(char));

  // count each character count in each word
  for (int i = 0; i < ASize; ++i)
    for (int j = 0; A[i][j]; ++j)
      table[i][A[i][j] - 'a']++;

  int count = 0;
  // for each lowercase character
  for (int i = 0; i < 26; ++i) {
    int c = 0;
    int min = WORD_LEN + 1;
    for (int j = 0; j < ASize; ++j) {
      if (table[j][i] > 0) {
        // if character count greater than zero
        // we increment `c`, so, if character occurs
        // in each word, after ending in this inner 
        // cycle, `c` should be equal to WORDs length i.e. ASize
        ++c;
        if (table[j][i] < min)
          min = table[j][i];
      }
    }

    if (c == ASize && min != WORD_LEN + 1) {
      for (int j = 0; j < min; ++j) {
        result[count][0] = (char) (i + 'a');
        result[count][1] = '\0';
        ++count;
      }
    }
  }

  *returnSize = count;
  return result;
}