<h1 align="center"> Apple Store </h1>
<hr>

<h2>Introduction:</h2>

- The script is divided into many parts
- First is the market package
	- It contains the python files __init__, forms, models and routes
		- The __init__ file initializes the databse, the login users and password bcrypt 
		- The forms is used for creating the user login, registration, buying and selling forms
		- The models is used for creating the classes of tables present in the databse, password and email verification and the budget
		- The routes is used for routing the user to different pages
	- It also contains various html files like base, home, login, market, register and a directory containing the html files items_modals and owned_items_modals
		- The base file contains the base proforma of the website, which the rest of the webpages extends
		- The home file is used for designing the home page
		- The login file is used for designing the login page
		- The register fiAle is used for designing the register page
		- The market file is used for designing the market page
		- The item_modals and owned_items_modals contains the design of the buying and selling part
	- The run file is used to run the entire program 
<hr>
<h2>Third-Party Libraries Required:</h2>

- Flask
- SqlAlchemy

<hr>
<h2>How to install the above Library:</h2>

- pip install Flask
- pip install SqlAlchemy

<hr>
<h2>How to use:</h2>

- Need to install both SqlAlchemy and Flask through the terminal
- Then use set FLASK_APP=run
- flask run

## Output
![Image](Images/front_page.jpg)
![Image](Images/register_page.jpg)
![Image](Images/market_page.jpg)
![Image](Images/transaction.jpg)

<hr>

<h2>Input</h2>

![Image](Images/login_page.jpg)
![Image](Images/purchase_item.jpg)

