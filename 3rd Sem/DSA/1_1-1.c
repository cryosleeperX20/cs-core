//1.1 Perform the following operations on Array
//Read and Display an array

#include <stdio.h>

int main(){
    int n;
    printf("Enter Value of N:");
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        printf("Enter Value at Index %d : ",i);
        scanf("%d",&arr[i]);
    }
    for(int i = 0; i<n;i++)
    {
        printf("Value at Index %d : %d \n ",i,arr[i]);
    }
}