package FileCounter;


import java.io.File;
import java.util.*;

public class filecounter {


public static int countDirectory=0;

 public static int countFilesInDirectory(File directory){
     int countFile=0;
     for (File file : directory.listFiles()) {
         if (file.isFile()) {
             countFile++;
         }
         if (file.isDirectory()) {
        	 countDirectory++;
             countFile += countFilesInDirectory(file);
         }
     }

    return countFile;
 }

 public static void main(String args[]) {
	    Scanner s = new Scanner(System.in);
	    System.out.println("Enter the Path of your directory : ");
	    String path = s.next();
	 	File file = new File(path);
		int countFile = filecounter.countFilesInDirectory(file);
		System.out.println("The No of Files in entered Directory are : "+countFile);
		System.out.println("The No of Sub-Directory in entered Directory are : "+countDirectory);

 }
}
