#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int main()
{
    int weight;
    float height;
    printf("Enter weight in kg : ");
    scanf("%d",&weight);
    printf("Enter height in cm : ");
    scanf("%f",& height);
    float BMI=((weight)/(height*height))*10000;
    printf("Your Body Mass Index is : %f", BMI);
    if(BMI>0)
    {
        if(BMI<=16)
         printf("\nYou are severly underweight ");
         else if(BMI<=18.5)
         printf("\nYou are underweight");
         else if(BMI<=25)
         printf("\nYou are healthy");
         else if(BMI<=30)
         printf("\nYou are overweight");
         else 
         printf("\nYou are severely overweight ");
    }
    else
    printf("Enter valid details");
return 0;
}