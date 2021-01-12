import java.util.Arrays;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class MorseCode_Generator{
    
    static int z;

    public static void main(String[] args)
    
    {
        String[] morse = { ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",

                ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",

                "...-", ".--", "-..-", "-.--", "--..",
                "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."," ", "\\s", "   ", "\\s\\s\\s"};
        String[] alphabet = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "","", "\\s", " "};

       //Pattern englishPatt = Pattern.compile();

        System.out.println("Welcome to translator!");
        System.out.println("");
        System.out.println("Enter -1 to exit. ");
        Scanner input = new Scanner(System.in);
        String userInput = input.nextLine();

        if (userInput.toUpperCase().contains("A") || userInput.toUpperCase().contains("B") || userInput.toUpperCase().contains("C") || userInput.toUpperCase().contains("D") || userInput.toUpperCase().contains("E") || userInput.toUpperCase().contains("F") || userInput.toUpperCase().contains("G") || userInput.toUpperCase().contains("H") || userInput.toUpperCase().contains("I") || userInput.toUpperCase().contains("J") || userInput.toUpperCase().contains("K") || userInput.toUpperCase().contains("L") || userInput.toUpperCase().contains("M") || userInput.toUpperCase().contains("N") || userInput.toUpperCase().contains("O") || userInput.toUpperCase().contains("P") || userInput.toUpperCase().contains("Q") || userInput.toUpperCase().contains("R") || userInput.toUpperCase().contains("S") || userInput.toUpperCase().contains("T") || userInput.toUpperCase().contains("U") || userInput.toUpperCase().contains("V") || userInput.toUpperCase().contains("W") || userInput.toUpperCase().contains("X") || userInput.toUpperCase().contains("Y") || userInput.toUpperCase().contains("Z") || userInput.toUpperCase().contains("0") || userInput.toUpperCase().contains("1") || userInput.toUpperCase().contains("2") || userInput.toUpperCase().contains("3") || userInput.toUpperCase().contains("4") || userInput.toUpperCase().contains("5") || userInput.toUpperCase().contains("6") || userInput.toUpperCase().contains("7") || userInput.toUpperCase().contains("8") || userInput.toUpperCase().contains("9"))
        {
            z=2;
        }
        else
        {
            z=1;
        }
        switch (z)
        {
        case 2:
        {
            System.out.println("Language detected: English");
            userInput = userInput.toUpperCase();
            
            for (int i = 0; i < userInput.length(); i++)
            {
                char x = userInput.charAt(i);
                if (x == ' ') System.out.print("  ");
                else System.out.print(morse[x - 'A'] + " ");
                
            }
            System.out.println("");
            System.out.println("");
            System.out.println("Good bye!");
            break;
        }
        case 1:
        {
            System.out.println("Language detected: Morse");
            Pattern morsePatt = Pattern.compile("[\\.-]++");
            Matcher morseMatch = morsePatt.matcher(userInput);
            while (morseMatch.find()) 
            {
            int x;

            x = Arrays.asList(morse).indexOf(morseMatch.group());
            System.out.printf(alphabet[x]);
             
            }
            }
            System.out.println("");
            System.out.println("");
            System.out.println("Good bye!");
            break;
        default:
            System.out.println("?");
        }
        
        }
    }

