
// Aim: Given coins of different denominations and an amount, return the minimum number of coins to make up that amount.
// If it cannot be made, return -1. (Unbounded Knapsack DP problem)

#include <stdio.h>
#include <stdlib.h>

int coinChange(int* coins, int coinsSize, int amount){
    int* dp = (int*)malloc((amount + 1) * sizeof(int));
    for (int i = 0; i <= amount; i++) dp[i] = amount + 1;
    dp[0] = 0;
    
    for (int i = 1; i <= amount; i++) {
        for (int j = 0; j < coinsSize; j++) {
            if (coins[j] <= i) {
                if (dp[i - coins[j]] + 1 < dp[i])
                    dp[i] = dp[i - coins[j]] + 1;
            }
        }
    }
    
    int res = (dp[amount] > amount) ? -1 : dp[amount];
    free(dp);
    return res;
}

int main() {
    int coins[] = {1, 2, 5};
    int amount = 11;
    int size = sizeof(coins)/sizeof(coins[0]);

    int ans = coinChange(coins, size, amount);
    printf("Minimum coins to make %d = %d\n", amount, ans);

    return 0;
}
