
/*

Special button are : F1 to F10
other not special

*/

#include<stdio.h>

int main()
{
	while(1)
	{
		char pressed_keyboard_button; // variable defined to get the presses key
		
		printf("\nPress any keyboard button : ");
		pressed_keyboard_button = getch();
		
		printf("\nASCII code of pressed keyboard button is %d.\n",pressed_keyboard_button);
		
		if(pressed_keyboard_button==0)// for F1 to F10 (for function keys)
		{
			pressed_keyboard_button = getch();
			printf("Some FUNCTION KEY is pressed, therefore ASCII code is 0.\n");
			printf("Scan Code for that this FUNCTION KEY is %d.\n\n",pressed_keyboard_button);
		}
		else
		{
			printf("Key other than FUNCTION KEY is pressed, therefore ASCII code is not 0.\n");
			printf("Scan Code for this KEY is same as ASCII character.\n\n");
		}
		getch();
	}
	return 0;
}
