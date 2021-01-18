import java.util.Scanner;
import java.util.Random;

public class RollDice {

	private static Scanner userchoice;
	
	public static void main (String[] args)
	{
		//Start option for dice roll//
		System.out.println("Do you want to roll the dice? (Y/N)");
		userchoice = new Scanner(System.in);
		
		String choice;
		choice = userchoice.next();
		choice = choice.toLowerCase();
			
		while(true)
		{
			//If user does not use correct input for question//
			if (!choice.equals("y") && !choice.equals("n"))
			{
				System.out.println("Error. Please pick 'y' or 'n'.");
				userchoice = new Scanner(System.in);
				choice = userchoice.next();
				choice = choice.toLowerCase();
			}
			
			//If user chooses to roll the dice//
			else if (choice.equals("y"))
			{
				int faces;
				
				Random generator = new Random();
				faces = generator.nextInt(6) + 1;
				
				System.out.println("You rolled a " + faces + ".");
				System.out.println("Roll again?");
				userchoice = new Scanner(System.in);
				choice = userchoice.next();
				choice = choice.toLowerCase();
			}
			
			//If user chooses not to roll the dice//
			else if (choice.equals("n"))
			{
				System.out.println("Thank you for rolling!");
				break;
			}
		}	
		
	}
	
}