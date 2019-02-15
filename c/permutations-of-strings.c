#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const void *a, const void *b) {
    const char **ia = (const char **)a;
    const char **ib = (const char **)b;
    return strcmp(*ia, *ib);
}

/* A utility function two swap two strings a and b */
void swap(char **a, char **b) {
    char *t = *a;
    *a = *b;
    *b = t;
}
 
/*
 * This function finds the index of the smallest string
 * which is greater than 'first' and is present in s[l..h]
 */
int find_ceil(char **s, char *first, int l, int h) {
    /* initialize index of ceiling element */
    int ceil_index = l;
 
    /*
     * Now iterate through rest of the elements and find
     * the smallest character greater than 'first'
     */
    
    for (int i = l+1; i <= h; i++)
        if ((strcmp(s[i], first) > 0) && (strcmp(s[i], s[ceil_index]) < 0))
            ceil_index = i;
 
    return ceil_index;
}

int next_permutation(int n, char **s) {
    int theres_more = 1;
    int i;
    
    /*
     * Find the rightmost string which is smaller than its next
     * character. Let us call it 'first str'
    */
    for (i = n-2; i >= 0; i--)
        if (strcmp(s[i], s[i+1]) < 0)
            break;

    /*
     * If there is no such string, all are sorted in decreasing order,
     * means we just found the last permutation and we are done.
     */
    if (i == -1) {
        theres_more = 0;
    } else {
        /*
         * Find the ceil of 'first char' in right of first character.
         * Ceil of a character is the smallest character greater than it
         */
        int ceil_index = find_ceil(s, s[i], i + 1, n - 1);
        
        /* Swap first and second strings */
        swap(&s[i], &s[ceil_index]);

        /* Sort the string on right of 'first char' */
        qsort(s + i + 1, n - i - 1, sizeof(s[0]), lexicographic_sort);
    }
    
    return theres_more;
}