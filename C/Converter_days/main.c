#include<stdio.h>
#include<stdlib.h>
void find(int total_days) {
   int year, weeks, days;
   year = total_days / 365;
   weeks = (total_days % 365) / 7;
   days = (total_days % 365) % 7;
   printf("years = %d",year);
   printf("\nweeks = %d", weeks);
   printf("\ndays = %d ",days);
}
int main()
 {
   int total_days;
   printf("Enter the number of days:");
   scanf("%d",&total_days);
   find(total_days);
   return 0;
}