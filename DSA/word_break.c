//determine if a string can be segmented into words from a given dictionary

#include <string.h>
#include <stdbool.h>

bool wordBreak(char * s, char ** wordDict, int wordDictSize){
    int len = strlen(s);
    bool dp[len + 1];
    for (int i = 0; i <= len; i++) dp[i] = false;
    dp[0] = true;

    for (int i = 1; i <= len; i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j]) {
                for (int k = 0; k < wordDictSize; k++) {
                    int wordLen = strlen(wordDict[k]);
                    if (i - j == wordLen && strncmp(&s[j], wordDict[k], wordLen) == 0) {
                        dp[i] = true;
                        break;
                    }
                }
            }
            if (dp[i]) break;
        }
    }
    return dp[len];
}
