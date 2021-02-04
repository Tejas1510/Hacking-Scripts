# <p align = "center"> Website Blocker using PC Hosts files </p>
## Introduction: 
This is a script that aims to implement a website blocking utility for Windows-based systems. It makes use of the computer's hosts files and runs it as a background process, preventing access to the sites entered by the user in array format.
## Third-party libraries required:
The project requires Python's datetime library only
## Importing the Libraries:
Open Command Prompt on your computer and type the following:
On the script's console, type: <br>
`import time` <br>
`from datetime import datetime as dt`

## Running the Script:
After opening the script in your Python IDE, execute the code so that you get the console output window. Open your browser and try to visit the websites you blocked. When the script runs successfully, you will see `This site can't be reached` error on the browser.

**Note:**
> In some systems, access to the computers's hosts files maybe denied by default to prevent malware attacks. So the script while executing may show an error while modifying the hosts files. 
> Please visit [here](https://www.technipages.com/windows-access-denied-when-modifying-hosts-or-lmhosts-file) for a brief readup on how to solve the issue.

> *Recommended:* Please revert to the original access settings after testing the script to prevent any future compromise

## Output:
#### The output console will print this everytime you visit/refresh a blocked webpage:
![Output1](https://i.pinimg.com/originals/f2/ef/48/f2ef48144df31db5abdb497e3eaa3751.png)
#### This is how the browser acts when you try to visit the website that you blocked:
![Output2](https://i.pinimg.com/originals/ea/2b/cf/ea2bcfbc1240f17ff2c45087728ff500.png)