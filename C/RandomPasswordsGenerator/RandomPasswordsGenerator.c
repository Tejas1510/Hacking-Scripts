#include <time.h>
#include <stdio.h>
#include <stdlib.h>
 
int main(void)
{
    /* Length of the password */
    int length;
    int num;
    int temp;
    printf("Enter the length of the password: ");
    scanf("%d", &length);
    printf("\nEnter the number of passwords you want: ");
    scanf("%d", &num);
    /* Seed number for rand() */
    srand((unsigned int) time(0) + getpid());
 
    while(num--)
    {
        temp = length;
        printf("\n");
        while(temp--) {
            putchar(rand() % 56 + 65);
            srand(rand());
        }
 
        temp = length;
    }
 
    printf("\n");
 
    return EXIT_SUCCESS;
}