#include<stdio.h>
//<stdio.h> header file used for Standard input and output.
#include<stdlib.h>
/*<stdlib.h>  is the header file used for General Purpose Standard Library of C Programming language which declares avariety of utility function for type of coversions, memory allcoation,process control and other similar tasks.*/
#include<time.h>
/*<time.h> header file used for Provide Standardized access to time/date manipulation and formatting*/

int main()
{ 
    int Number,guess,ng=1;
    //ng used for numer of Guesses
 srand(time(0));
//***It Genrates the Random numbers  From 1 To 100***

 Number = rand()%100+1; 
 // The loop is running countiues till the Number is guessed 
 
 do{
    printf("Guess a Number BtW 1 To 100\n");
    scanf("%d",&guess);
    if(guess > Number)
    {
        printf("Lower Number Please!!\n");
    
    }
    else if (guess < Number)
    {
        printf("Higher The Number Please!!\n");
    }
    else
    {
        printf("You Guessed it in %d attemps \n",ng);
    }
    ng++;
 } while (guess!=Number);
 
 return 0;
 
 
}