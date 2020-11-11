package FileCounter;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.*;
public class duplicate {
public static int countDirectory=0;
 public static void removeduplicate(File directory) throws Exception{
	 ArrayList<String> fileList = new ArrayList<>();

     for (File file : directory.listFiles())  {
    	 File file1 = new File(file.getAbsolutePath());
    	 FileReader fr = new FileReader(file1);
    	 BufferedReader reader = new BufferedReader(fr);
    	 StringBuilder stringBuilder = new StringBuilder();
    	 String line = null;
    	 String ls = System.getProperty("line.separator");
    	 while ((line = reader.readLine()) != null) {
    	 	stringBuilder.append(line);
    	 	stringBuilder.append(ls);
    	 }
    	 stringBuilder.deleteCharAt(stringBuilder.length() - 1);
    	 String content = stringBuilder.toString();

    	 if(fileList.contains(content)) {
    		 System.out.println("The file "+ file.getName()+" is a duplicate file");
	  		 System.out.println(file.getName()+ " Removed");
         file1.delete();
	  		 System.out.println("");
    	 }
    	 else {
    		 fileList.add(content);
    	 }
    	 reader.close();

     }

 }
  public static void main(String args[]) throws Exception {
	    Scanner s = new Scanner(System.in);
	    System.out.println("Enter the Path of your directory : ");
	    String path = s.next();
	 	File file = new File(path);
		duplicate.removeduplicate(file);
		System.out.println("All Duplicates File Removed");
		s.close();
		}
}
