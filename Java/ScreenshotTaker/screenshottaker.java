/* 
Java Program to take a screenshot of the screen
*/
import java.awt.image.BufferedImage; 
import java.io.File; 
import java.awt.Rectangle; 
import java.awt.Toolkit; 
import java.awt.Robot; 
import javax.imageio.ImageIO; 

public class screenshottaker { 
    public static final long serialVersionUID = 1L; 
    public static void main(String[] args) 
    { 
        try 
        {
            Thread.sleep(120); //sleeping the main thread for 120 ms
            Robot r = new Robot(); 

            //to save the screen shot to a specific location
            String path = "D:// Screenshot.jpg";
            
            //Getting the screen size
            Rectangle capture =  new Rectangle(Toolkit.getDefaultToolkit().getScreenSize()); 
            //capturing the image
            BufferedImage Image = r.createScreenCapture(capture); 
            ImageIO.write(Image, "jpg", new File(path)); 
            System.out.println("Screenshot saved"); 
        } 
        catch (Exception exception) 
        { 
            System.out.println("Error: "+exception); 
        } 
    } 
} 