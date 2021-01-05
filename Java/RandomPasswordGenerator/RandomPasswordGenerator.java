import java.util.Random;
import java.util.Scanner;

public class RandomPasswordGenerator {
	public static String generatePassword(int len) {
		//String containing alphanumeric characters i.e [a-z and A-Z and 0-9]
		String str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
		//Random class to generate random idex value of the alphanumeric string
		Random random = new Random();
		//StringBuilder is used to append the random alphanumeric characters
		StringBuilder sb = new StringBuilder();
		for(int i=0;i<len;i++) {
			sb.append(str.charAt(random.nextInt(str.length())));
		}
		//Converting StringBuilder to String and returning the randomly generated password
		return sb.toString();
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int len;
		System.out.println("Enter the length of the password to be generated:");
		len = sc.nextInt();
		System.out.println(generatePassword(len));

	}

}
