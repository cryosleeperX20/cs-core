/*
Input:
order = "cba"
s = "abcd"

Output:
"cbad" or "cbda" (as long as 'c', 'b', 'a' are in that order)
*/

#include <stdio.h>
#include <string.h>

char* customSortString(char* order, char* s) {
    int freq[128] = {0}; 

    // Step 1: Count frequency of each character in s
    for (int i = 0; s[i] != '\0'; i++) {
        freq[(int)s[i]]++;
    }

    // Step 2: Allocate enough space for result
    char* result = (char*)malloc(strlen(s) + 1);
    int k = 0;

    // Step 3: Add characters from 'order' to result
    for (int i = 0; order[i] != '\0'; i++) {
        char ch = order[i];
        while (freq[(int)ch] > 0) {
            result[k++] = ch;
            freq[(int)ch]--;
        }
    }

    // Step 4: Add remaining characters not in 'order'
    for (int i = 0; i < 128; i++) {
        while (freq[i] > 0) {
            result[k++] = (char)i;
            freq[i]--;
        }
    }

    result[k] = '\0';
    return result;
}

int main() {
    char order[] = "cba";
    char s[] = "abcd";

    char* sorted = customSortString(order, s);
    printf("Sorted string: %s\n", sorted);
    free(sorted);
    return 0;
}
