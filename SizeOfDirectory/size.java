package FileCounter;
import java.io.File;
import java.util.*;
public class filecounter {
public static int countDirectory=0;
 public static long countsize(File directory){
     long dictsize=0;
     for (File file : directory.listFiles()) {
         if (file.isFile()) {
        	 dictsize=dictsize+file.length();
         }
         if (file.isDirectory()) {
        	 dictsize += countsize(file);
         }
     }
    return dictsize;
 }
  public static void main(String args[]) {
	    Scanner s = new Scanner(System.in);
	    System.out.println("Enter the Path of your directory : ");
	    String path = s.next();
	 	File file = new File(path);
		long dictsize = filecounter.countsize(file);
		System.out.println("The size of entered Directory in Bytes is : "+dictsize+" Bytes");
		System.out.println("The size of entered Directory in Kilo Bytes(KB) is : "+dictsize/1024+" KiloBytes");
		System.out.println("The size of entered Directory in Mega Bytes(MB) is : "+dictsize/(1024*1024)+" MegaBytes");
		}
}
