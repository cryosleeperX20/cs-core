
// Implement a program for Binary to Decimal Conversion and Decimal to Binary Conversion.

#include <stdio.h>
#include <math.h>

int binaryToDecimal(int n)
{
    int decimal = 0, i = 0, remainder;
    while (n != 0)
    {
        remainder = n % 10;
        n /= 10;
        decimal += remainder * pow(2, i);
        ++i;
    }
    return decimal;
}

int decimalToBinary(int n)
{
    int binary = 0, i = 1, remainder;
    while (n != 0)
    {
        remainder = n % 2;
        n /= 2;
        binary += remainder * i;
        i *= 10;
    }
    return binary;
}

int main()
{
    printf("MENU\n");
    printf("1. Binary to Decimal Conversion\n");
    printf("2. Decimal to Binary Conversion\n");
    printf("Enter your choice: ");
    int choice;
    scanf("%d", &choice);
    switch (choice)
    {
    case 1:
    {
        int binary;
        printf("Enter a binary number: ");
        scanf("%d", &binary);
        printf("Decimal: %d\n", binaryToDecimal(binary));
        break;
    }
    case 2:
    {
        int decimal;
        printf("Enter a decimal number: ");
        scanf("%d", &decimal);
        printf("Binary: %d\n", decimalToBinary(decimal));
        break;
    }
    default:
        printf("Invalid choice\n");
    }
    return 0;
}
