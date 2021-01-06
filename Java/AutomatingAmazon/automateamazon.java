package AutomatingAmazon;

import java.util.Scanner;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;

public class automateamazon {
	
	//a "global" object of the webdriver class
	public static WebDriver driver = null;
	
	private static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub
		
		/*
		//setting the path for the Chrome Browser
		System.setProperty("webdriver.chrome.driver",".\\driver\\chromedriver.exe");
		
		//launching the driver for the Chrome Browser
		driver = new ChromeDriver();
		*/
		
		//setting the path for the Edge Browser
		System.setProperty("webdriver.edge.driver",".\\driver\\msedgedriver.exe");
				
		//launching the driver for the Edge Browser
		driver = new EdgeDriver();
		
		
		
		//here we are assuming that the user is already logged in
		
		driver.manage().timeouts().implicitlyWait(15,TimeUnit.SECONDS); 
		//implicitWait insures that the entire script waits for a duration till it identifies the required web element.
		//here we set the duration to 15 seconds
		//if implicitWait is not provided then it throws an error, No such element found if the webpage doesn't load immediately.
		
		//now we open the web application
		driver.navigate().to("https://amazon.in"); //here we are opening amazon.in
		driver.manage().window().maximize(); //to maximize the web browser
		
		String title = driver.getTitle();
		
		//comparing two strings(irrespective of the case- capital or small)
		if(title.equalsIgnoreCase("Amazon.in"))
			System.out.println("Title matches!");
		else
			System.out.println("Title mismatched! " + title);
		
		//now the amazon has been launched
		//now we locate the web element
		WebElement searchbox = driver.findElement(By.id("twotabsearchtextbox"));
		
		//now we type the below string in the text box
		searchbox.sendKeys("APJ Abdul Kalam");
		
		//then we click the search button
		driver.findElement(By.id("nav-search-submit-button")).click();
		
		//now we choose the book, then shift the control to the new tab from the old tab and then click on add to cart
		//searching the book
		driver.findElement(By.partialLinkText("Wings of Fire: An Autobiography of Abdul Kalam")).click();
		//using partial link text if the name we know is not complete
		Thread.sleep(2002);//giving a delay of 2 sec
		
		//shifting the tab control
		java.util.Set<String> handles = driver.getWindowHandles();
		//the above function is used to store the multiple tabs
		String winHandle1 = driver.getWindowHandle(); //identifies the present tab 
		handles.remove(winHandle1);//we dont need the present tab
		
		//choosing the specific tab using iterator function
		String winHandle = handles.iterator().next();
		String winHandle2 = " ";
		if(winHandle != winHandle1) {
			
			//to retrieve the handle of the second window
			winHandle2 = winHandle; //storing the handle of the second window handle
			//switch control to new tab
			driver.switchTo().window(winHandle2);
			System.out.println(winHandle2);
			
		}
		Thread.sleep(2000); //delay for the main thread
		
		//adding to cart
		try {
			driver.findElement(By.id("add-to-cart-button")).click();
		}
		catch(Exception e) {
			driver.findElement(By.id("add-to-ebooks-cart-button")).click();
		}
		
		Thread.sleep(3000);
		
		//scroll the web page to the end
		JavascriptExecutor js = (JavascriptExecutor) driver;
		js.executeScript("window.scrollTo(0,document.body.scrollHeight)");
		//Thread.sleep(3000);
		
		
		//the item has been added to cart
		System.out.println("The item has been added to the cart successfully!");
		
	}

}
