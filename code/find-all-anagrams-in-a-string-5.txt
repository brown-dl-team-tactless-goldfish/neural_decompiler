/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int sump, sums, pos;
int lutp[26], luts[26];
int* result;

bool compare (void)
{
    for (int i = 0; i < 26; i++)
    {
        if (luts[i] != lutp[i])
            return 0;
    }
    return 1;
}

int* findAnagrams(char * s, char * p, int* returnSize)
{

    /* Algo:
        0. Init result array, lutp, luts, sump, sums.
        1. If lenp > lens, return empty array.
        2. Create a LUTp of frequency count for string p. Also save the
           sum of characters in sump. 
        3. Repeat step 2 for string s for the first lenp characters (i.e. 
           window of size lenp).
        4. Slide the window of size lenp towards right over string s.
        5. Check if sums == sump. If so, compare luts for both strings.
           If LUTs match, save the starting index in result array.
        6. Go to step 4 if end of window has not reached end of string s.
        7. return result array.

    */

    // 0

    int lens = strlen(s);
    int lenp = strlen(p);
    
    *returnSize = 0;

    // 1
    if (lenp > lens)
        return NULL;
    else
        result = (int*) malloc (sizeof(int) * (lens- lenp + 1));

    pos = 0;
    sump = sums = 0;
    memset (lutp, 0, sizeof(int) * 26);
    memset (luts, 0, sizeof(int) * 26);

    // 2
    char c;
    for (int i = 0; i < lenp; i++)
    {
        c = p[i] - 'a';
        sump += c;
        lutp[c]++;
    }

    for (int i = 0; i < lenp; i++)
    {
        c = s[i] - 'a';
        sums += c;
        luts[c]++;
    }

    int i = 0;
    while (1)
    {
        if (sums == sump)
        {
            if (compare ())
            {
                result[pos] = i;
                pos++;
            }
        }


        c = s[i] - 'a';
        sums -= c;
        luts[c]--;

        i++;
        if (i + lenp - 1 >= lens)
            break;
        c = s[i + lenp - 1] - 'a';
        luts[c]++;
        sums += c;
    }
    *returnSize = pos;
    return result;
}